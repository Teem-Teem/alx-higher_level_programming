#!/usr/bin/node

// a script that prints boolean of each time the arguments found

const argumentsPassed = process.argv.length;
console.log(argumentsPassed === 2 ? 'No argument' : argumentsPassed === 3 ? 'Argument found' : 'Arguments found');
