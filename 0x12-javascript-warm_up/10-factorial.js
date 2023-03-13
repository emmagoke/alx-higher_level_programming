#!/usr/bin/node

const first = parseInt(process.argv[2]);

function factorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

if (Number.isNaN(first)) {
  console.log(1);
} else {
  console.log(factorial(first));
}
