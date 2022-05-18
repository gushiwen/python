'''
In cmd or shell run: python app.py
D:\>python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
'''

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
'''
D:\>curl http://127.0.0.1:5000/
Hello, World!
'''

@app.route("/testGet")
def my_get():
    return "This is GET"
'''
D:\>curl http://127.0.0.1:5000/testGet
This is GET
'''

@app.route("/testGetParams")
def my_get_params():
    return request.args
'''
D:\>curl "http://127.0.0.1:5000/testGetParams?a=1&b=2"
{"a":"1","b":"2"}
'''

@app.route("/testPost", methods=["POST"])
def my_post():
    return "This is POST"
'''
D:\>curl -X POST "http://127.0.0.1:5000/testPost"
This is POST
'''


@app.route("/testPostJson", methods=["POST"])
def my_post_json():
    return request.json
'''
test.json
{
	"name": "dongfanger",
	"alias": "redsun"
}

D:\>curl -H "Content-Type: application/json" -d "@test.json" "http://127.0.0.1:5000/testPostJson"
{'name': 'dongfanger', 'alias': 'redsun'}
'''

# GET and POST
@app.route("/testGetPost", methods=["GET", "POST"])
def my_get_post():
    if request.method == "GET":
        return "This is GET"
    if request.method == "POST":
        return "This is POST"
'''
D:\>curl http://127.0.0.1:5000/testGetPost
This is GET
D:\>curl http://127.0.0.1:5000/testGetPost -X POST
This is POST
'''

@app.route("/testHeaders")
def my_headers():
    return str(request.headers)
'''
D:\>curl http://127.0.0.1:5000/testHeaders
Host: 127.0.0.1:5000
User-Agent: curl/7.55.1
Accept: */*
'''

if __name__ == "__main__":
    app.run()