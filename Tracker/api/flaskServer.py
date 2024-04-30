import time
import io
from flask import Flask, request, jsonify
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Response
from CurrHistMath import CurrHistMath
import base64

app = Flask(__name__)


@app.route('/time')
def get_current_time():
    return {'time': time.asctime(time.localtime())}


@app.route('/teaminfo')
def team_info():
    return {
        "names": "Zac, Kaiya, Nick, Bao",
        "about": "We are Computer Science students at the University of the Fraser Valley."
    }

@app.route('/comparechart/data')
def compare_chart():  
    
    return {
        "numcurrent": CurrHistMath.current_num_message(),
        "numhistorical": CurrHistMath.historical_num_message(),
        "message": CurrHistMath.compare_fire()
    }
@app.route('/comparechart/figure')
def generate_figure():
    fig = CurrHistMath.display_graph()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)  
    return Response(output.getvalue(), mimetype='image/png')

#Function posts the current and historical fires on the map
@app.route('/testpost', methods =['POST'])
def test_post():
    data = request.json
    lat = data.get('latitude')
    long = data.get('longitude')
    CurrHistMath.set_user_longlat(lat, long)
    
    #debug message
    #response_message = f"Latitude: {lat}, Longitude: {long}"
    #print(response_message, flush=True)

    l1 = CurrHistMath.firesInArea_test(lat,long)
    l2 = CurrHistMath.historicalfiresInArea_test(lat,long)
    dic = {'list1' : l1 , 'list2': l2}
    
    return jsonify(dic)




@app.route('/selectmarker', methods =['POST'])
def select():
    
    data = request.json
    lat = data.get('latitude')
    long = data.get('longitude')
    CurrHistMath.set_user_longlat(lat, long)

    return '', 204
