import os

from flask import Flask
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import request

app = Flask(__name__)

KNOWN_MIMES = ['text/html', 'application/xhtml+xml', 'application/json', 'application/xml']

def getHeaders(req):
    result = dict()
    for key, value in req.headers.iteritems():
        result[key] = value

    result['remote_addr'] = req.remote_addr
    result['xhr'] = req.is_xhr
    
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
@app.route('/extension.<extension>')
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

    if extension == 'json':
        return jsonify(getHeaders(request))

    return "UNKNOWN EXTENSION: " + extension

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.debug = bool(int(os.environ.get('DEBUG', 0)))
    app.run(host='0.0.0.0', port=port)