from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', message='')

@app.route('/', methods = ['GET', 'POST'])
def formhandler():
	scenario = request.form['scenario']
	message = "Showing maps for scenario " + scenario.replace('_','.') + ":"
	if scenario == "RCP2_6":
		map1 = "Logo-compact.jpg"
		map2 = "Logo-compact.jpg"
		map3 = "Logo-compact.jpg"
		map4 = "Logo-compact.jpg"
	elif scenario == "RCP8_5":
		map1 = "sst_rcp8.5.jpg"
		map2 = "ph_rcp8.5.jpg"
		map3 = "O2_rcp8.5.jpg"
		map4 = "productivity_rcp8.5.jpg"

	return render_template('index.html', message=message, 
		scenario=scenario,map1=map1,map2=map2, map3=map3, map4=map4)


if __name__ == '__main__':
   app.run(debug = True)