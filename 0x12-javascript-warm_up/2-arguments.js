#!/usr/bin/node

// a script that prints boolean of each time the arguments found

if (process.argv.length < 3) {
	  console.log('No argument');
} else if (process.argv.length === 3) {
	  console.log('Argument found');
} else {
	  console.log('Arguments found');
}
