#!/usr/bin/node

const list = require('./100-data').list;
/* This function imports an array and computes a
 * new array. The new array is equal to equal to the
 * value of the initial list, multipled by the index
 * in the list.
 */
/* const newarray = list.map((item, index) => {
  return item * index;
});
*/
console.log(list);
console.log(list.map((item, index) => item * index));
