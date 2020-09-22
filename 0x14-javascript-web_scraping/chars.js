#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches
// given integer
const request = require('request');
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).characters);
});
