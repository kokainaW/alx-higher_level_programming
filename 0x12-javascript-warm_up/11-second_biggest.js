#!/usr/bin/node
// Searches the 2nd biggest integer in the list

const args = process.argv;

if (isNaN(args[2])) {
  console.log('0');
} else if (args.length === 3) {
  console.log('0');
} else {
  let first = parseInt(args[2], 10);
  let second = parseInt(args[3], 10);
  for (let i = 2; i < args.length; i++) {
    if (parseInt(args[i], 10) > first) {
      second = first;
      first = parseInt(args[i], 10);
    }
    if (parseInt(args[i], 10) > second && parseInt(args[i], 10) < first) {
      second = parseInt(args[i], 10);
    }
  }
  console.log(second);
}
