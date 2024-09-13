Python
Note: You will automatically switch to the new branch. Make sure you name the branch
session-1, as this name will be used in our GitHub Actions later.
Adding Code to the Repository
1. From the repo’s code page, click the Add file or + sign button and create a new file.
2. Name the file app.py and paste the following code into it. Click the Commit changes
button to save the file.
from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class Home(Resource):
def get(self):
return {'version': '1.0'}
class ConvertTemp(Resource):
def get(self):
# Get arguments from query parameters
temp = float(request.args.get('temp'))
scale = request.args.get('scale').lower()
target_scale = request.args.get('target_scale').lower()
# Perform temperature conversion
converted_temp = self.convert_temperature(temp, scale, target_scale)
if converted_temp is None:
return {'error': 'Invalid scale or target scale'}, 400
return {'converted_temp': converted_temp, 'target_scale': target_scale}
def convert_temperature(self, temp, scale, target_scale):
# Conversion logic
if scale == target_scale:
return temp
if scale == 'celsius':
if target_scale == 'fahrenheit':
return temp * 9/5 + 32
elif target_scale == 'kelvin':
return temp + 273.15
elif scale == 'fahrenheit':
if target_scale == 'celsius':
return (temp - 32) * 5/9
elif target_scale == 'kelvin':
return (temp - 32) * 5/9 + 273.15
elif scale == 'kelvin':
if target_scale == 'celsius':
return temp - 273.15
elif target_scale == 'fahrenheit':
return (temp - 273.15) * 9/5 + 32
Python
Python
# If scales are invalid
return None
api.add_resource(Home, '/')
api.add_resource(ConvertTemp, '/convert-temp')
if __name__ == '__main__':
app.run(debug=True)
