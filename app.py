import os
import socket

from flask import Flask
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import request
from flask import send_from_directory

from stathatasync import StatHat

app = Flask(__name__)

KNOWN_MIMES = ('text/html', 'application/xhtml+xml', 'application/json', 'application/xml')
HEADER_BLACKLIST = ('Cookie', 'X-Heroku-Dynos-In-Use', 'X-Heroku-Queue-Depth', 'X-Heroku-Queue-Wait-Time', 'X-Request-Start', 'X-Varnish')

def getHeaders(req):
    result = dict()

    # clone flasks "dict like object" to be safe
    for key, value in req.headers.iteritems():
        if key in HEADER_BLACKLIST:
            continue

        result[key] = value

    result['X-Remote-Addr'] = req.remote_addr
    result['X-Remote-Host'],_,_ = socket.gethostbyaddr(req.remote_addr)
    result['X-Xhr'] = req.is_xhr

    return result


def detect_extension(req):
    best = req.accept_mimetypes.best_match(KNOWN_MIMES)

    if best == 'text/html' or best == 'application/xhtml+xml':
        return 'html'

    if best == 'application/xml':
        return 'xml'

    if best == 'application/json':
        return 'json'

    return "UNABLE TO DETECT EXTENSION"


@app.route('/', defaults={'extension': 'auto'})
@app.route('/default.<extension>')
def default(extension):
    if extension == 'auto':
        extension = detect_extension(request)

    if extension == 'html':
        resp = make_response(render_template('default.html', headers=getHeaders(request)))
        resp.mimetype = 'text/html'
        return resp

    if extension == 'xml':
        resp = make_response(render_template('default.xml', headers=getHeaders(request)))
        resp.mimetype = 'application/xml'
        return resp

    if extension == 'txt':
        resp = make_response(render_template('default.txt', headers=getHeaders(request)))
        resp.mimetype = 'text/plain'
        return resp

    if extension == 'json':
        return jsonify(getHeaders(request))

    return "UNKNOWN EXTENSION: " + extension

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/mu-f4cef731-9cad8885-3d770e39-b8663c18')
def blitzio():
    return "42"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.debug = bool(int(os.environ.get('DEBUG', 0)))
    app.run(host='0.0.0.0', port=port)
