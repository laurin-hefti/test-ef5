# api Handler, sends the request to the api and receaved the data

import requests

def get_data_from_api(datum, stock):
    url = "https://api.polygon.io/v2/aggs/ticker/"+stock+"/range/1/day/"+datum+"/"+datum+"?adjusted=true&sort=asc&limit=5000&apiKey=HNRmV2qK0iESHmTb_ikYsresXkZAS1ph"
    r = requests.get(url)
    data = r.json()
    return data