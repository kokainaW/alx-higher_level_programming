#!/usr/bin/node
// imports an array
const originalList = require('./100-data').list;
console.log(originalList);
const mappedList = originalList.map (function (e, index) {
    return (e * index);
});
console.log(mappedList);
