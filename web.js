var express = require('express');

var app = express.createServer(express.logger());

app.get('/', function(request, response) {
    var html = "";
    response.contentType('html');
    for (var header in request.headers) {
        response.write(header + ": " + request.headers[header]);
        response.write("<br/>");
    }
    response.end();
});

var port = process.env.PORT || 3000;
app.listen(port, function() {
    console.log('Listening on ' + port);
});
