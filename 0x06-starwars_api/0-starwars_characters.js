#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, async (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }
  for (const characterId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(characterId, (error, response, body) => {
        if (error) {
          reject(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
