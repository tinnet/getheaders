import os

from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask import make_response

app = Flask(__name__)

KNOWN_MIMES = ['text/html', 'application/xhtml+xml', 'application/json', 'application/xml']

def getHeaders(req):
    result = dict()
    for key, value in req.headers.iteritems():
        result[key] = value

    result['remote_addr'] = req.remote_addr
    result['xhr'] = req.is_xhr
    
    return result

@app.route('/')
def root():
    return find_best_response_type(request, getHeaders(request))

@app.route('/default.<extension>')
def default(extension):
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

def find_best_response_type(req, headers):
    best = req.accept_mimetypes.best_match(KNOWN_MIMES)

    if best == 'text/html' or best == 'application/xhtml+xml':
        resp = make_response(render_template('default.html', headers=headers))
        resp.mimetype = best
        return resp

    if best == 'application/xml':
       resp = make_response(render_template('default.xml', headers=headers))
       resp.mimetype = best
       return resp

    if best == 'application/json':
        return jsonify(headers)

    return "UNKNOWN CONTENTTYPE: " + best

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.debug = bool(int(os.environ.get('DEBUG', 0)))
    app.run(host='0.0.0.0', port=port)