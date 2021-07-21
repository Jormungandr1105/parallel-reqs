const { readFile } = require("fs").promises;

async function read_from_file() {
	const file = await readFile('../../status/file.txt', 'utf8');
	console.log(file)
}

read_from_file()

console.log('do_this_asap')