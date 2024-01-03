#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], (error, response) => {
  if (error) {
    console.error(error);
    return;
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
