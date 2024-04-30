import React, { useState, useEffect } from 'react';
import iconImg from '../images/icon.png';
import fireImg from '../images/fire.png';
import oldFireImg from '../images/oldfire.png';
import "leaflet/dist/leaflet.css"
import {MapContainer, TileLayer, Marker, useMapEvents, Popup } from "react-leaflet";
import { Icon } from 'leaflet';
import './chart.css';

const Tracker = () => {



 const [markers, setMarkers] = useState([]);
  const [triggerMessageUpdate, setTriggerMessageUpdate] = useState();

  const locIcon = new Icon({
    iconUrl:  iconImg,
    iconSize:[30,30]

  })

  const fireIcon = new Icon({
    iconUrl:  fireImg,
    iconSize:[30,30]

  })

  const oldFireIcon = new Icon({
    iconUrl:  oldFireImg,
    iconSize:[30,30]

  })


  //const [fireMarkers, setFireMarkers] = useState([])

  const [oldFireMarkers, setOldFireMarkers] = useState([])

  const [aboutUsData, setAboutUsData] = useState({
    names: "",
    about: "",
  });

  const [chart, setChart] = useState({
    current: "",
    historical: "",
    message: "",
  });

  const AddMarkerToClick = () => {
    const map = useMapEvents({
      dblclick(event) {
        const { lat, lng } = event.latlng;
        fetch('/testpost', {
         method: 'POST',
         headers: {
          'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            latitude: lat,
            longitude: lng,

          })

      })
      .then(response => response.json())
      .then(data =>
        fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat.toString()}&lon=${lng.toString()}&format=json`)
        .then(response => response.json())
        .then(locdata => setMarkers(prevMarkers => [...prevMarkers, { geocode: [lat, lng], popup: locdata.display_name, firedata: getFirePoints(data.list1), oldfiredata: getOldFirePoints(data.list2)}])));

      }
      
    });

    return null;
  };



  const deleteMarker = (index) => {
    setMarkers(prevMarkers => prevMarkers.filter((_,i) => i !== index));
  };

  const onMarkerClick = (index) => {
    //console.log('hi')
    const lat  = markers[index].geocode[0]
    const lng =markers[index].geocode[1]

    fetch('/selectmarker', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          latitude: lat,
          longitude: lng,
        })

      })
    setTriggerMessageUpdate(true);
      return null;

  }



  function getFirePoints(firedata) {

    const fires = JSON.parse(firedata)
    const fireCoords =[];

    fires.forEach(fire => {
          const { LATITUDE, LONGITUDE, GEO_DESC, FIRE_YEAR } = fire;
          fireCoords.push({geocode: [LATITUDE, LONGITUDE], popup: `${GEO_DESC}, ${FIRE_YEAR}`})
        });

    return fireCoords;

  }

  function getOldFirePoints(oldfiredata) {

    const oldfires = JSON.parse(oldfiredata)
    const oldfireCoords =[];

    oldfires.forEach(oldfire => {
          const { LATITUDE, LONGITUDE, Name, IGNITION_DATE } = oldfire;
          oldfireCoords.push({geocode: [LATITUDE, LONGITUDE], popup: `${Name}, ${IGNITION_DATE}`})
        });

    return oldfireCoords;

  }

  useEffect(() => {
    fetch('/comparechart/data')
      .then(res => res.json())
      .then(data => {
        setChart({
          current: data.numcurrent,
          historical: data.numhistorical,
          message: data.message,
        });
        //console.log(chart.current,chart.historical,chart.message )
      })
    setTriggerMessageUpdate(false);
  }, [markers, triggerMessageUpdate]);

  const [figure, setFigure] = useState(0);

  useEffect(() => {
    fetch('/comparechart/figure')
      .then(res => res.blob())
      .then(blob => {
        setFigure(URL.createObjectURL(blob));
      })
  }, [markers, triggerMessageUpdate]);




    return (
        <div className="Tracker">
        <div>

            <MapContainer center= {[49.2608724,-123.113952]} zoom ={13}>
          <TileLayer
            attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          <AddMarkerToClick />
          {markers.map((marker, index) => (
            <Marker key={index} position={marker.geocode} icon={locIcon} eventHandlers={{ click: () => onMarkerClick(index)}}>
              <Popup>
                <p>{marker.popup}</p>
                <button onClick={() => deleteMarker(index)}>Delete Pin</button>
              </Popup>
            </Marker>
          ))}
          {markers.map((marker, index) => (
            marker.firedata ? marker.firedata.map((fireMarker, fireIndex) => (
            <Marker key={`fire-${index}-${fireIndex}`} position={fireMarker.geocode} icon={fireIcon}>
              <Popup>
                <p>
                  {fireMarker.popup}
                </p>
              </Popup>
            </Marker>
            )) : []
          ))}

          
          {markers.map((marker, index) => (
            marker.oldfiredata ? marker.oldfiredata.map((fireMarker, fireIndex) => (
            <Marker key={`fire-${index}-${fireIndex}`} position={fireMarker.geocode} icon={oldFireIcon}>
              <Popup>
                <p>
                  {fireMarker.popup}
                </p>
              </Popup>
            </Marker>
            )) : []
          ))}
        </MapContainer>
        <div class="instructions">
        <h2>How To Use</h2>
        <p>1. Find desired location</p>
        <p>2. Double click on location to pin a marker on the map.</p>
        <p>3. Click on any fire marker to view details of fire.</p>
        <p>Note: Light Fires are On-going Fires, Dark Fires are Historical Fires</p>
        </div>

        
        <div class="container">
          {figure && <img src={figure}/>}
          <div class="text">
          <h2>Statistics</h2>
          <p>{chart.current}</p>
          <p>{chart.historical}</p>
          <p>{chart.message}</p>
          </div>
        </div>
        </div>

  </div>
    );
};
export default Tracker;
