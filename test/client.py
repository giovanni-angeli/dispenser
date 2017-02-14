import pprint
import requests

URL = 'http://localhost:5000/contents'
JSON_DATA = {"name": "Value"}

# ~ r = requests.post(URL, auth=('username', 'password'), verify=False, json=JSON_DATA)
r = requests.post(URL, json=JSON_DATA)
headers = {'Content-type': 'application/json'}
# ~ ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
pprint.pprint(r.content)
# ~ print(r.json())
print(r.status_code)


