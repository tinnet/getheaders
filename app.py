import os

from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template

app = Flask(__name__)

KNOWN_MIMES = ['text/html', 'application/xhtml+xml', 'application/json', 'application/xml']

@app.route('/')
def root():
    result = dict()
    for key, value in request.headers.iteritems():
        result[key] = value

    result['remote_addr'] = request.remote_addr
    result['xhr'] = request.is_xhr

    return find_best_response_type(request, result)

def find_best_response_type(req, headers):
    best = req.accept_mimetypes.best_match(KNOWN_MIMES)

    if best == 'text/html' or best == 'application/xhtml+xml':
        return render_template('default.html', headers=headers)
    
    if best == 'application/json':
        return jsonify(headers)
        
    if best == 'application/xml':
        return render_template('default.xml', headers=headers)
    return "UNKNOWN: " + best

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.debug = bool(int(os.environ.get('DEBUG', 0)))
    app.run(host='0.0.0.0', port=port)