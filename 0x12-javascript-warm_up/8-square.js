#!/usr/bin/node
let out = '';
const size = process.argv[2];

if (size) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      out += 'X';
    }
    if (i !== size - 1) {
      out += '\n';
    }
  }
} else {
  out += 'Missing size';
}
console.log(out);
