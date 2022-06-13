from bottle import route, run, template
from requests import make_request
from parser import parse_single, parse_search
from cache import timed_lru_cache
from json import dumps 

@route('/')
def index():
    with open("docs.html", "r") as f:
        return f.read()

@route('/api/name/<name>')
@timed_lru_cache(seconds=60*60*3, maxsize=2048)
def get_name(name: str):
    html = make_request(f"/profile/{name}")
#    return html
    return parse_single(html)

@route('/api/3chars')
@timed_lru_cache(seconds=60*5)
def three_chars():
    html = make_request(f"/minecraft-names?length_op=eq&length=3")
    return parse_search(html)

@route('/api/searches/<searches:int>')
@timed_lru_cache(seconds=60*5)
def searches(searches: int):
    html = make_request(f"/minecraft-names?searches={searches}")
    return parse_search(html)

run(host='localhost', port=8080)
