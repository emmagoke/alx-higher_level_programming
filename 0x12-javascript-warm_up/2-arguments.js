#!/usr/bin/node

const {argv} = require('node:process');

const inputarr = [];

for (let i = 2; i < argv.length; i++)
{
	inputarr.push(argv[i]);
}

if (inputarr.length == 0)
{
	console.log("No argument");
}
else if (inputarr.length == 1)
{
	console.log("Argument found")
}
else
{
	console.log("Arguments found");
}
