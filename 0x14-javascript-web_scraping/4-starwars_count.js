#!/usr/bin/node
// Prints the number of movies where the character 'Wedge Antilles' is present
const request = require('request');
const wedge = '18';
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  let count = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.includes(wedge)) {
        count++;
      }
    }
  }
  console.log(count);
});
