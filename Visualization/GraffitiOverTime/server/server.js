/**
 * @author dhanannjay.deo
 */
 
// Module dependencies.
var express = require('express');

var app = express();

// Configuration
app.configure( function() {
});

// Routes
app.get('/', function(req, res) {
    res.send('Hello World');
});

app.use(express.static(__dirname + '/static'));
app.use(express.static(__dirname + '/data'));

app.listen(80);