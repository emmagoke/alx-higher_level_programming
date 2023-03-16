#!/usr/bin/node

/* This function converts a number from base 10
 * to another base passed as argument
 */
exports.converter = function (base) {
  return function (number) {
    return parseInt(number, 10).toString(base);
  };
};
