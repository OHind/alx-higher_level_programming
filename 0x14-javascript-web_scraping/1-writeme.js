#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

fs.writeFile(args[1], args[2], 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
