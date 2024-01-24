from flask import Flask,request,render_template,jsonify
import json

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask"

@app.route('/cal',methods=['GET',"POST"])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    if operation=='add':
        result=int(number1)+int(number2)
    elif operation=='multiply':
        result=int(number1)*int(number2)
    elif operation=='division':
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    return jsonify(result)
        

if __name__=='__main__':
    app.run()