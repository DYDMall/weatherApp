from flask import Flask, render_template, request 
import requests
app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
	zipcode = request.form['zip']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=5dab208cf8e01187a7e50e6df2fc7ed2')
	json_object = r.json()
	temp_k = float(json_object['main']['temp'])
	temp_f = (temp_k - 273.15) * 1.8 + 32
	temp_f = '%.0f' % temp_f
	return render_template('temperature.html', temp=temp_f)

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)