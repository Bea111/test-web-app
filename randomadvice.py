from flask import Flask, render_template
import json

app= Flask ("app2")

api_key = 'd7b14c3e0766a1536b684c52a84f6419'
api_url = 'https://favqs.com/api/qotd'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_key)}



def get_advice():
    endpoint= 'https://favqs.com/api/qotd'
    response=[]
    for advice in advice
     response.endpoint()

    return response.json()
