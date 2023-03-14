#!/usr/bin/node
let array = [];
const length = process.argv.length;

function sort (array) {
  let temp;
  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (array[i] > array[j]) {
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }
  return array;
}

if (length < 3) {
  console.log(0);
} else if (length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < length; i++) {
    array.push(parseInt(process.argv[i]));
  }
  array = sort(array);
  console.log(array[length - 4]);
}
/* second largest element =
 * length - 2 (process stuff) - 1 (zero index) - 1
 */
