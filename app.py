import os

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    result = dict()
    for key, value in request.headers.iteritems():
        result[key] = value

    result['remote_addr'] = request.remote_addr
    result['xhr'] = request.is_xhr

    return render_template('default.html', headers=result)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)