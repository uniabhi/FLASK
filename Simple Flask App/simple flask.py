from flask import Flask
app=Flask(__name__)

@app.route('/')
def welcome():
    return "hello world!"

@app.route('/python')
def abhi():
    return "python can be use for Data science"


if __name__=='__main__':
    app.run(debug=True)