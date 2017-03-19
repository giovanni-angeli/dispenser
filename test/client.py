import pprint
import requests
import json
import uuid

URL = 'http://localhost:5000/api/contents/{}'.format(uuid.uuid4())
# ~ URL = 'http://giovanniangeli.pythonanywhere.com/contents'

JSON_DATA = {"one": "The pyjama people", "two": "are boring me to pieces"}

r = requests.get(URL, json=JSON_DATA, headers = {'Content-type': 'application/json'})

pprint.pprint(json.loads(r.content.decode("utf8")))

print(r.status_code)


