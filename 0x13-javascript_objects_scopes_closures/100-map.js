#!/usr/bin/node

const list = require('./100-main').list;
/* This function imports an array and computes a
 * new array. The new array is equal to equal to the
 * value of the initial list, multipled by the index
 * in the list.
 */

console.log(list);
console.log(list.map((item, index) => item * index));
