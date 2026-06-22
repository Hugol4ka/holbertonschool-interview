#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';

request(url, function (error, response, body) {
  if (!error) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    function fetchCharacter (index) {
      if (index >= characters.length) return;

      request(characters[index], function (charError, charResponse, charBody) {
        if (!charError) {
          const charData = JSON.parse(charBody);
          console.log(charData.name);

          fetchCharacter(index + 1);
        }
      });
    }
    fetchCharacter(0);
  }
});
