import requests

def get_data_from_api(datum):
    url = "https://api.polygon.io/v2/aggs/ticker/SMI/range/1/day/"+datum+"/"+datum+"?adjusted=true&sort=asc&limit=120&apiKey=HNRmV2qK0iESHmTb_ikYsresXkZAS1ph"
    print(url)
    r = requests.get(url)
    data = r.json()
    print(data)
    return data