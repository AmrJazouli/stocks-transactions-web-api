"""
Functional and integration tests for stocks web app 
"""

from app import app
import pytest
from pymongo import MongoClient
import os
from dotenv import load_dotenv



class TestApp:
    
      
    # This test method tests the behavior of the index route of the Flask app.  
    def test_index_route(self):
        response = app.test_client().get('/')

        assert response.status_code == 200
        assert 'Welcome to API for Stocks Transactions' in response.data.decode('utf-8')
        

    
    # This test method tests the behavior of the CRUD page route of the Flask app.
    def test_curd_page_route(self):
        response = app.test_client().get('/curd')

        assert response.status_code == 200
        assert 'Read' in response.data.decode('utf-8')
        assert 'Insert' in response.data.decode('utf-8')
        assert 'Delete' in response.data.decode('utf-8')
        assert 'Update' in response.data.decode('utf-8')
   
   
   
    # This test method tests the behavior of the insert page route of the Flask app.
    def test_insert_page_route(self):
       
        response1 = app.test_client().post('/insert', data={'symbol': 'TSLA', 'side': 'BUY'})
        response2 = app.test_client().post('/insert', data={'symbol': 'TS2LY', 'side': 'BUY'})
        response3 = app.test_client().post('/insert', data={'symbol': 'TSLA', 'side': 'Other'})


        # Test valid insertion
        assert response1.status_code == 200
        assert 'Record inserted' in response1.data.decode('utf-8')

        # Test input validation
        assert response2.status_code == 200
        assert 'Input Error' in response2.data.decode('utf-8')

        assert response3.status_code == 200
        assert 'Input Error' in response3.data.decode('utf-8')
                         
    



    # This test method tests the behavior of the update page route of the Flask app.
    def test_update_page_route(self):

        response1 = app.test_client().post('/insert', data={'symbol': 'APPL', 'side': 'BUY'})    
        response2 = app.test_client().put('/update', data={'symbol': 'APPL', 'new_side': 'SELL'})

        response3 = app.test_client().post('/insert', data={'symbol': 'COLA', 'side': 'BUY'})    
        response4 = app.test_client().put('/update', data={'symbol': 'C5O9L2A', 'new_side': 'SELL'})
        

        response5 = app.test_client().post('/insert', data={'symbol': 'COLA', 'side': 'BUY'})    
        response6 = app.test_client().put('/update', data={'symbol': 'COLA', 'new_side': 'Other'})


        # Test valid update                                  
        assert response2.status_code == 200
        assert 'Record updated' in response2.data.decode('utf-8')
        
        # Test input validation
        assert response4.status_code == 200
        assert 'Input Error' in response4.data.decode('utf-8')
    
        assert response6.status_code == 200
        assert 'Input Error' in response6.data.decode('utf-8')






    # This test method tests the behavior of the delete page route of the Flask app.
    def test_delete_page_route(self):
        
        response1 = app.test_client().post('/insert', data={'symbol': 'TSLA', 'side': 'BUY'})
        response2 = app.test_client().delete('/delete', data={'symbol': 'TSLA'})
        
        response3 = app.test_client().post('/insert', data={'symbol': 'TSLA', 'side': 'BUY'})
        response4 = app.test_client().delete('/delete', data={'symbol': 'TS2LY'})
        

        # Test valid delete
        assert response2.status_code == 200
        assert 'Record delete' in response2.data.decode('utf-8')     

       # Test input validation
        assert response4.status_code == 200
        assert 'Input Error' in response4.data.decode('utf-8') 