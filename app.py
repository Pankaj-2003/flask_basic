from flask import Flask,render_template, request,redirect, url_for,jsonify
# simple flask app

app = Flask(__name__)
@app.route("/",methods = ["GET"])

def welcome():
    return "<h1>welkme<h1>"

@app.route("/index",methods = ["GET"])
def index():
    return "<h2>welkhm to index page<h2>"

@app.route('/success/<float:score>')
def success(score):
    return "the person has passed and the score is: "+ str(score)
@app.route('/fail/<float:score>')
def fail(score):
    return "the student was not passed and the score is: "+str(score)

@app.route('/form',methods= ["GET","POST"])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        average_marks = (maths+science+history)/3
        res  =''
        if average_marks>= 50:
            res = 'success'
        else:
            res='fail'
        return redirect(url_for(res, score = average_marks))
        # return render_template('form.html',score = average_marks)
    
@app.route('/api',methods = ["POST"])
def calculate_sum():
   data = request.get_json()
   a_val = float(dict(data)['a'])
   b_val = float(dict(data)['b'])
   return jsonify(a_val+b_val)












if __name__ =="__main__":
    app.run(debug=True)