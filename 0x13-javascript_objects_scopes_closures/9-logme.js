#!/usr/bin/node
// number of arguments already printed
let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
