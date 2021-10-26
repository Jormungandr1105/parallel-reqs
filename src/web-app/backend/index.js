var Data = require('./src/data.js');
const express = require('express'); //Line 1
const app = express(); //Line 2

var atime = 0;
var aData;

app.listen(5000, () => console.log(`Listening on port 5000`));


app.use(function(req, res, next) {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

app.get("/data", function(req, res) {
	Data.readData(atime, aData, function(err, data, new_atime, updated) {
		res.send(data);
		atime = new_atime;
		if (updated == true) {aData = data;}
	});
});
