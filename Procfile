web: newrelic-admin run-program gunicorn -b 0.0.0.0:$PORT -w 3 -k gevent_wsgi app:app
local: python app.py -b 0.0.0.0:$PORT
