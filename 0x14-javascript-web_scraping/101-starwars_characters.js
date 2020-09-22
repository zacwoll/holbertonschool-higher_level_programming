#!/usr/bin/node
// print all characters of a Star Wars movie
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
let characters;
const dict = {};
request(url, function (error, response, body) {
  if (error) throw error;
  characters = JSON.parse(body).characters;
  for (const charUrl of characters) {
    request(charUrl, (error, response, body) =>
      !error && addData(charUrl, JSON.parse(body).name));
  }
});

function addData (charUrl, name) {
  dict[charUrl] = name;
  if (Object.entries(dict).length === characters.length) {
    for (const charUrl of characters) {
      console.log(dict[charUrl]);
    }
  }
}
