## 1. Flask Web API for Stocks Transactions

It's a Flask web application according to REST API that applies CRUD operations on a stock transaction to handle its basic details in MongoDB database.

### Functionalities

1. Create a stock transation
2. Update the transaction from BUY to SELL or vice-versa
3. Get transactions to read them
4. Delete any stock transaction that has been previoulsy created

### Installation Instructions

This application is written on Python and it uses MongoDB database.
After cloning this repository, go to the api folder:

```
cd api 
```

1. Create a virtual environment with the following command (Replace <envname> with the name you choose to give your virtual environment ):
```
conda create -n <envname> 
``` 
2. Activate your virtual environment:
```
conda activate <envname> 
```
3. Install all the packages needed for the application to run using 'pip' and the requirement.txt file:
```
pip install -r requirements.txt 
```
4. Install MongoDB on localhost or set up a MongoDB Atlas cluster in the cloud.


### Usage and Instructions

1. Run the application. From api folder, (where `app.py` file is located) run:

```
flask run
```

It will start a web server available in your browser at http://localhost:5000.

![Web Page](../images/FlaskWeb/Frontpage.png)

2. The first page displays a welcome message, then click on 'Start application'.
Create a stock transaction:

In Insert section, type e.g. 'TSLA' in Stock Symbol and 'BUY' in Side, then click on 'Submit'.

![Web Page1](images/FlaskWeb/curd.png)

A message of successful insert will be displayed:

![Web Page2](images/FlaskWeb/insertsuccessful.png)

Check your MongoDB Database if the record has been inserted correctly:

![Web Page3](images/FlaskWeb/MongoDBInsert.png)

You can check the same with UPDATE, READ and DELETE operations.

Press CTRL+C to stop the web server.

### Testing

I also performed functional tests.

Because of some import errors, I didn't move the test_functionalities.py file into a test folder.

Run the following command:

```
python -m pytest -v -s
```
A test session in the CLI will start and display results of passed and failed tests:

![Web Page4](images/Tests/pytest.png)


## 2. Deployment to Azure with application code:  

In this case, the startup app is not in the root directory, therefore, we tried to add a startup command such as **'gunicorn --bind=0.0.0.0 --timeout 600 --chdir api application:app'**, but, the required librairies will not be installed in the virtual environment at the deployment because **'requirements.txt'** is not in the root directory.

According to documentation, in this case, the **'requirements.txt'** should be moved to the root directory, which might not be convenient for some reasons (ReasonsToBeDeveloped).

To deploy the web app by keeping the **'requirements.txt'** in the subfolder, we have to update the existing workflow provided at the deployment of the Azure web app.
The modification will consist in adding the keyword and its value **'package: ./api'** in the deployment job at :

**'deploy->steps->name: 'Deploy to Azure Web App'->with->package: ./api'**

Having simultanesouly the startup command mentioned above and the keyword-value **'package: ./api'** in the deloyment job will result in this error: **'Error: can't chdir to 'api'**