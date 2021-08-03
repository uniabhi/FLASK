 ##Building url dynamically
##variable Rules and Url Building

from flask import Flask,redirect,url_for

app= Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to pycharm"

@app.route('/success/<int:score>')
def success(score):
    return "This person has passed and the marks is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "This person has failed and the marks is "+str(score)

##Result Checker
@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))



if __name__=="__main__":
    app.run(debug=True)