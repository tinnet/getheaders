# WHAT

Small app to return http request headers in format determined by Accept: header

# WHY

* because i am sick of googling for an website to show me my ip/user-agent ;)

* because the world needs a service that has a plain text response that we can grep/awk/sed in bash scripts

# HOW
## GET XML (via content type)

    curl -H Accept:application/xml http://localhost:5000
    <headers>
        <Accept>application/xml</Accept>
        <Content-Length></Content-Length>
        <Content-Type></Content-Type>
        <Host>localhost:5000</Host>
        <remote_addr>127.0.0.1</remote_addr>
        <User-Agent>curl/7.21.4 (universal-apple-darwin11.0) libcurl/7.21.4 OpenSSL/0.9.8r zlib/1.2.5</User-Agent>
        <xhr>False</xhr>
    </headers>

## GET XML (via file extension)
    curl http://localhost:5000/default.xml

## GET JSON (via content type)

    curl -H Accept:application/json http://localhost:5000
    {
      "xhr": false, 
      "Content-Length": "", 
      "remote_addr": "127.0.0.1", 
      "Content-Type": "", 
      "Host": "localhost:5000", 
      "Accept": "application/json", 
      "User-Agent": "curl/7.21.4 (universal-apple-darwin11.0) libcurl/7.21.4 OpenSSL/0.9.8r zlib/1.2.5"
    }

## GET JSON (via file extension)
    curl http://localhost:5000/default.json

## GET PLAINTEXT (via content type)

    curl -H Accept:text/plain http://localhost:5000
    xhr: false
    Content-Length:
    remote_addr: 127.0.0.1
    Content-Type:
    Host: localhost:5000
    Accept: application/json
    User-Agent: curl/7.21.4 (universal-apple-darwin11.0) libcurl/7.21.4 OpenSSL/0.9.8r zlib/1.2.5

## GET PLAINTEXT (via file extension)
    curl http://localhost:5000/default.txt

# TODO

* add some nonstandard magic headers like:
	* ~~remote_addr (make sure heroku does not mess with remote it via x-forward)~~
	* geolocation?
	* ~~reverse hostname?~~

* ~~filter heroku headers (secret?!)~~

* improve html view

  * add banner (money!)

  * add style

* ~~add json view~~

* ~~add txt view~~

* ~~add xml view~~
