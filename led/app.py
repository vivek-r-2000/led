from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
	return render_template('slider.html')

@app.route("/res",methods=["POST","GET"])
def res():
	val=request.form["myrange"]
	print(val)
	return val

if __name__=='__main__':
	app.run(debug=True)