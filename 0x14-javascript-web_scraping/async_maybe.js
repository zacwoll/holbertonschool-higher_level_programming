#!/usr/bin/node
// print all characters of a Star Wars movie
const request = require('request');
const filmsURL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

function getCharName (url) {
  return new Promise((resolve, reject) => {
	request(url, (error, response, body) => {
  	if (error) {
    	reject(error);
  	}
  	resolve(JSON.parse(body).name);
	});
  });
}

async function charsInFilm (urlList) {
  try {
	let name;
	for (const url of urlList) {
  	name = await getCharName(url);
  	console.log(name);
	}
  } catch (error) {
	console.error(error);
  }
}

request(filmsURL, function (error, response, body) {
  if (error) {
	console.error(error);
  }
  const urlList = JSON.parse(body).characters;
  charsInFilm(urlList);
});
