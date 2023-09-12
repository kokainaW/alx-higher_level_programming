#!/usr/bin/node
// imports an array and computes new array
const { list } = require('./100-data');

console.log(list);
console.log(list.map((element, idx) => element * idx));
