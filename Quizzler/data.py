import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

data = requests.get("https://opentdb.com/api.php", parameters)
data.raise_for_status()
question_data = data.json()['results']
