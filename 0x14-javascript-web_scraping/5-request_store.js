#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fileToStore = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileToStore, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
