import flask; print(flask.__version__)
from flask import Flask, render_template, request
import subprocess as sp
from pymongo import MongoClient
#import os
#from dotenv import load_dotenv




app = Flask(__name__)


#load_dotenv()


#client = MongoClient('mongodb://localhost:27017')

#client = MongoClient(os.getenv('MONGODB_HOST'))
#client = MongoClient(os.getenv('MONGOPASS'))

#client = MongoClient(os.getenv('MONGODB_CONNSTRING'))


#db = client.curd
#myCollection = db.myColl



#app.env = "development"
result = ""
print("I am in flask app")


@app.route("/")
def my_home():
    date = sp.getoutput("date /t")
    return render_template("home.html", date=date)



@app.route("/curd")
def insert_val():
    return render_template("curd.html")


'''
@app.route("/read")
def read():
    cursor = myCollection.find()
    for record in cursor:
        symbol = record["symbol"]
        print(record)
    return render_template("response.html", res=symbol)


def insert_sub(sym, sid):
    myVal = { "symbol": sym, "side": sid}

    return myCollection.insert_one(myVal) 


@app.route("/insert")
def insert():
    symbol = request.args.get("symbol")
    side = request.args.get("side")
    myVal = { "symbol": symbol, "side": side}
    #x = insert_sub(symbol, side)
    x = myCollection.insert_one(myVal)
    return render_template("response.html", res=x)
               

@app.route("/delete")
def delete():
    symbol = request.args.get("symbol")
    myquery = { "symbol": symbol }
    myCollection.delete_one(myquery)
    x = "Record delete"
    return render_template("response.html", res=x)


@app.route("/update")
def update():
    symbol = request.args.get("symbol")
    new_side = request.args.get("new_side")
    myquery = { "symbol": symbol }
    newvalues = { "$set" : { "side": new_side} }
    myCollection.update_one(myquery, newvalues)
    x = "Record updated"
    return render_template("response.html", res=x)

'''



if __name__=="__main__":
    
    #app.run(host="0.0.0.0", debug=True)
    app.run()
