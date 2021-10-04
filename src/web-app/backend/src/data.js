var fs = require('fs');


function readData(atime, Data, callback) {
	
	const file = "../../../status/file.json"

	fs.stat(file, (err, stats) => {
		if (err) {
			console.error(err);
			return;
		}
		if (stats.mtimeMs > atime) {
			fs.readFile(file, function(err, data) {
				Data = JSON.parse(data);
				console.log("New Data Accessed");
				callback(null, Data, Date.now());
			});
		} else {
			console.log("Old Data Accessed");
			callback(null, Data, atime);
		}
	});
	
}

module.exports = {readData}
