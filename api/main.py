from config import Config
import requests
import json
import os


def get_token(urls: str, username: str, password: str) -> str:

    try:
        headers = {'content-type': 'application/json'}
        payload = {"username": username, "password": password}
        r = requests.post(url=urls, data=json.dumps(payload), headers=headers)
        token1 = f"JWT {r.json()['access_token']}"
        return token1
    except:
        print('Error Api Key')


def save_data(data_dir: str, process_date):

    current_dir = (os.path.join(data_dir, process_date))
    os.makedirs(current_dir, exist_ok=True)
    try:
        r = requests.get(url=url, data=json.dumps({"date": process_date}), headers=header)
        with open(file=os.path.join(current_dir, f'{process_date}.json'), mode='w+') as f:
            json.dump(r.json(), f)
    except:
        print('Error data')


if __name__ == '__main__':
    config = Config(path='./config.yaml')
    config_AUTH = config.get_config("AUTH")
    config_API = config.get_config("API")
    token = (get_token(urls=config_API["url"] + config_AUTH["endpoint"],
                       username=config_AUTH["payload"]["username"],
                       password=config_AUTH["payload"]["password"]))
    url = config_API["url"] + config_API["endpoint"]
    header = {'content-type': 'application/json', 'Authorization': token}
    data = config_API["payload"].values()
    for dt in data:
        save_data(data_dir='./result',
                  process_date=dt)
