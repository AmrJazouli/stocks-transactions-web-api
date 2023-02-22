"""
Functional tests for stocks web app 
"""

from app import app
import pytest
from pymongo import MongoClient
import os
from dotenv import load_dotenv



class TestApp:
    
      
    def test_index_route(self):
        response = app.test_client().get('/')

        assert response.status_code == 200
        assert 'Welcome to API for Stocks Transactions' in response.data.decode('utf-8')
        


    def test_curd_page_route(self):
        response = app.test_client().get('/curd')

        assert response.status_code == 200
        assert 'Read' in response.data.decode('utf-8')
        assert 'Insert' in response.data.decode('utf-8')
        assert 'Delete' in response.data.decode('utf-8')
        assert 'Update' in response.data.decode('utf-8')
   
    
    def test_insert_page_route(self):
       
        response = app.test_client().get('/insert', data={'symbol': 'TSLA', 'side': 'BUY'})
      
        assert response.status_code == 200
        assert 'InsertOneResult' in response.data.decode('utf-8')
                         
    
    def test_update_page_route(self):

        response = app.test_client().get('/update', data={'symbol': 'TSLA', 'side': 'SELL'})
                                          
        assert response.status_code == 200
        assert 'Record updated' in response.data.decode('utf-8')
    

    def test_delete_page_route(self):

        response = app.test_client().get('/delete', data={'symbol': 'TSLA'})
                                          
        assert response.status_code == 200
        assert 'Record delete' in response.data.decode('utf-8')       