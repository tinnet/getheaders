WHAT
====
Small app to return http request headers in format determined by Accept: header

WHY
===
* ~~to try out node.js and heroku~~
	* python and heroku it is (nodejs in branch) ;P

* because i am sick of googling for an website to show me my ip/user-agent ;)

* because the world needs a service that has a plain text response that we can grep/awk/sed in bash scripts

TODO
====
* add some nonstandard magic headers like:
	* remote_addr (make sure heroku does not mess with remote it via x-forward)
	* geolocation
	* reverse hostname

* filter heroku headers (secret?!)

* improve html view

  * add banner (money!)

  * add style

* add json view

* add txt view

* add xml view
