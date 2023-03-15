#!/usr/bin/node
let args = 0;

/* This function prints the number of arguments
 * already printed and the new argument value.
 */
exports.logMe = function (item) {
  console.log(`${args}: ${item}`);
  args += 1;
};
