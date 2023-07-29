from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/home")
def welcome():
    return "Welcome to the flask"

@app.route("/cal",methods=["GET"])
def math_operation():
    operation=request.json["operation"]
    num1=request.json["num1"]
    num2=request.json["num2"]
    
    if operation=="add":
        result=num1+num2
    elif operation=="multiply":
        result=num1*num2    
    elif operation=="dividion":
        result=num1/num2
    else:
        result=num1-num2
        
    return result  
                


if __name__=="__main__":
    app.run(debug=True)