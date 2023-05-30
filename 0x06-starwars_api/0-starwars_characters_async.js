#!/usr/bin/node

const request = require('request');
const argv = process.argv;

const api = 'https://swapi-api.alx-tools.com/api/films/';

async request.get(`${api}${argv[2]}`, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (const character of characters) {
      await request.get(character, function(error, response, body) {
        if (!error) {
	  console.log(JSON.parse(body).name);
	}
      });
    }
  }
});

/*
function printCharName (characters, index) {
  request.get(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharName(characters, index + 1);
      }
    } else {
      console.log(error);
    }
  });
}
*/
