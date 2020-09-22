#!/usr/bin/node
// Writes a string to a file
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err, data) => {
  if (err) {
    return console.log(err);
  }
});
