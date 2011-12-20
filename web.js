var express = require('express');

var app = express.createServer(express.logger());

var HEADER_BLACKLIST = ['x-heroku-dynos-in-use'] 

app.get('/', function(request, response) {
    response.contentType('html');
    response.write("<html><head><title></title></head><body>");
    for (var header in request.headers) {
        if (header in HEADER_BLACKLIST) { continue; }
        response.write(header + ": " + request.headers[header]);
        response.write("<br/>");
    }
    response.write("</body></html>");
    response.end();
});

var port = process.env.PORT || 3000;
app.listen(port, function() {
    console.log('Listening on ' + port);
});
