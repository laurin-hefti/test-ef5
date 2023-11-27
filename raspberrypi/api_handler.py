def get_data_from_api():
    url = "https://api.polygon.io/v2/aggs/ticker/SMI/range/1/day/2023-01-09/2023-01-09?adjusted=true&sort=asc&limit=120&apiKey=HNRmV2qK0iESHmTb_ikYsresXkZAS1ph"
    r = requests.get(url)
    data = r.json()
    #print(data)
    return data