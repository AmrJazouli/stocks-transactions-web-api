

# import necessary modules
from flask import Flask, request, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import subprocess as sp
import re

# create a Flask app
app = Flask(__name__)

# load environment variables from .env file
load_dotenv()

# MongoDB class for interacting with MongoDB database
class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client.curd
        self.myCollection = self.db.myColl

    # Find all records in the collection
    def find_all(self):
        return self.myCollection.find()

    # Find records by symbol in the collection
    def find_by_symbol(self, symbol):
        return self.myCollection.find({"symbol": symbol})

    # Insert a new record into the collection
    def insert(self, symbol, side):
        myVal = {"symbol": symbol, "side": side}
        return self.myCollection.insert_one(myVal)

    # Delete a record from the collection by symbol
    def delete(self, symbol):
        myquery = {"symbol": symbol}
        return self.myCollection.delete_one(myquery)

    # Update a record in the collection by symbol with new side
    def update(self, symbol, new_side):
        myquery = {"symbol": symbol}
        newvalues = {"$set": {"side": new_side}}
        return self.myCollection.update_one(myquery, newvalues)

# Homepage class for rendering the homepage
class HomePage:
    def __init__(self):
        self.mongo = MongoDB()

    # Render the homepage template with the current date
    def render(self):
        date = sp.getoutput("date /t")
        return render_template("home.html", date=date)

# CurdPage class for rendering the CRUD page
class CurdPage:
    # Render the CRUD template
    def render(self):
        return render_template("curd.html")

# ReadPage class for rendering the read page
class ReadPage:
    def __init__(self):
        self.mongo = MongoDB()

    # Render the response template with all records in the collection
    def render(self):
        cursor = self.mongo.find_all()
        return render_template("response.html", res=cursor)

# InsertPage class for rendering the insert page
class InsertPage:
    def __init__(self):
        self.mongo = MongoDB()


    # Function to validate input values
    def validate_input(self, symbol, side):
        # Regular expression pattern to match string of 4 uppercase characters
        pattern1 = '^[A-Z]{4}$'
        # Regular expression pattern to match 'BUY' or 'SELL'
        pattern2 = '^(BUY|SELL)$'
        if not re.match(pattern1, symbol):
            # Return error message if symbol does not match pattern1
            return "Input Error: Symbol must be 4 uppercase characters"
        elif not re.match(pattern2, side):
            # Return error message if side does not match pattern2
            return "Input Error: Side must be 'BUY' or 'SELL'"
        else:
            # Return None if input values are valid
            return None


    # Retrieve the symbol and side from the query string parameters, validate the input values, insert new record into the collection if input values are valid, and render response template with success message or error message
    def render(self):
        symbol = request.form.get("symbol")
        side = request.form.get("side")
        # Validate input values
        error_message = self.validate_input(symbol, side)
        if error_message:
            # Render response template with error message if input values are invalid
            return render_template("response.html", res=error_message)
        else:
            # Insert new record into the collection if input values are valid
            self.mongo.insert(symbol, side)
            x = "Record inserted"
            # Render response template with success message
            return render_template("response.html", res=x)





# DeletePage class for rendering the delete page
class DeletePage:
    def __init__(self):
        self.mongo = MongoDB()

    # Retrieve the symbol from the query string parameters, delete matching record from the collection, and render response template with success message
    def render(self):
        # Retrieve the symbol from the query string parameters
        symbol = request.form.get("symbol")
        # Regular expression pattern to match string of 4 uppercase characters
        pattern = '^[A-Z]{4}$'
        # Input validation
        if not re.match(pattern, symbol):
            x = "Input Error: Invalid symbol. Symbol should be a string of 4 uppercase characters."
        else:
            # Delete the record with the matching symbol in MongoDB
            self.mongo.delete(symbol)
            # Create a response message
            x = "Record deleted"
        return render_template("response.html", res=x)





# Define the UpdatePage class
class UpdatePage:
    def __init__(self):
        # Initialize a new instance of MongoDB
        self.mongo = MongoDB()
  

    # Define the render function for UpdatePage
    def render(self):
        # Retrieve the symbol and new_side from the query string parameters
        symbol = request.form.get("symbol")
        new_side = request.form.get("new_side")
    
        # Regular expression pattern to match string of 4 uppercase characters
        pattern = '^[A-Z]{4}$'
        # Input validation
        if not re.match(pattern, symbol):
            x = "Input Error: Invalid symbol. Symbol should be a string of 4 uppercase characters."
        elif new_side not in ['BUY', 'SELL']:
            x = "Input Error: Invalid side. Side should be either 'BUY' or 'SELL'."
        else:
            # Update the record with the matching symbol in MongoDB with the new side
            self.mongo.update(symbol, new_side)
            # Create a response message
            x = "Record updated"
        # Render the response message in the response template
        return render_template("response.html", res=x)






# Define URL routes


# Define the route for the home page
@app.route("/")
def my_home():
    # Render the homepage
    return HomePage().render()


# Define the route for the curd page
@app.route("/curd")
def insert_val():
    # Render the curd page
    return CurdPage().render()


# Define the route for the read page
@app.route("/read")
def read():
    # Render the read page
    return ReadPage().render()


# Define the route for the insert page
@app.route("/insert", methods=["GET", "POST"])
def insert():
    # Render the insert page
    return InsertPage().render()


# Define the route for the delete page
@app.route("/delete", methods=["POST", "DELETE"])
def delete():
    # Render the delete page
    return DeletePage().render()


# Define the route for the update page
@app.route("/update", methods=["POST", "PUT"])
def update():
    # Render the update page
    return UpdatePage().render()




# Start the Flask application
if __name__ == "__main__":

    #app.run()
    app.run(host='0.0.0.0')



