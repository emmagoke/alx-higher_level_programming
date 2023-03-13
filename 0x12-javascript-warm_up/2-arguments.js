#!/usr/bin/node
/*
const { argv } = require('node:process');

const inputarr = [];

for (let i = 2; i < argv.length; i++) {
  inputarr.push(argv[i]);
}
*/
const length = process.argv.length;

if (length < 3) {
  console.log('No argument');
} else if (length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
