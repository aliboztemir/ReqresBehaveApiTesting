import json

import requests
from behave import *

from utils.configurations import getConfig
from utils.headers import Headers
from utils.params import Params
from utils.payload import *


@given('the API request')
def step_impl(context):
    config = getConfig()
    print(config)
    context.endpoint = config['API']['baseurl'] + config['ENDPOINT']['endpoint']

@when(u'we execute the GET API request with first id')
def step_impl(context):
    context.response = requests.get(url=context.endpoint,
                                    headers=Headers().get_content_json())


@then(u'check get api request')
def step_impl(context):
    context.json_response = context.response.json()
    print(f'The response :: {json.dumps(context.json_response, indent=2)}')
    assert context.json_response['data']['first_name'] == "George"
    assert context.json_response['data']['last_name'] == "Bluth"
    assert context.json_response['data']['email'] == "george.bluth@reqres.in"
    assert context.json_response['data']['id'] == 1