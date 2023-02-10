from flask import Flask, request
import joblib
import json as json
from flask_cors import CORS
model = joblib.load('mysite/billcal_gbr.pkl')


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/calculate',methods=['POST'])
def calculate():

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        bill=2
        type_of_HVAC= int(data['type_of_HVAC'])
        capacity_of_HVAC=float(data['capacity_of_HVAC'])
        size_of_building=int(data['size_of_building'])
        weather_conditions=int(data['weather_conditions'])
        working_hour=int(data['working_hour'])
        building_type=int(data['building_type'])
        consumption_rate=bill/(working_hour*size_of_building)

        try:
            a1 =model.predict([[ type_of_HVAC,capacity_of_HVAC,size_of_building,weather_conditions,working_hour,building_type,consumption_rate]])
            a1= a1 + 3000
            result = json.dumps(a1.tolist())
            return result
        except Exception as e:
            return str(e)

    else:
        return "Send The parameters in proper formate"





if __name__ == '__main__':
	app.run()
