import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
const Home = () => {





    return (
        <div>

            <h1>Brushfire Wildfire Tracker</h1>
            <p> Welcome to our wildfire tracker. To get started, click <Link to="/tracker">here</Link>, or use the navigation panel above. </p>
            
            <h2>About Us</h2>
            <p>Bonfire is a group of Computer Science Students from the University of the Fraser Valley.</p>
            <p>We created this wildfire tracker as a project in our COMP 370 class. Our goal is to provide information
            about ongoing and past wildfires in British Columbia, Canada, in a time efficient manner. </p>
            <h2>Source</h2>
            <p>Our information is sourced from the <a href='https://catalogue.data.gov.bc.ca/dataset/fire-locations-current'>Government of Bristish Columbia</a></p>

        </div>
    );
}
export default Home;
