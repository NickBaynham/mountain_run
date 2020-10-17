import requests
import json

from behave import *

url = 'https://mountain-run.com/post'
headers = {'Content-Type': 'application/json' }
payload = {'user': '001', 'time': '1010345', 'speed': '87.3', 'direction': 'NNE', 'long': '123434', 'lat': '134444' }
resp = ''

@given('I have a request to upload data')
def step_impl(context):
    print(url)

@when('I request service on the endpoint')
def step_impl(context):
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    
@then('I get a 200 OK response')
def step_impl(context):
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['url'] == url

    # print response full body as text
    print(resp.text)
