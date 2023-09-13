#!/usr/bin/node
// searches the 2nd biggest integer in the list

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[1]);
}
