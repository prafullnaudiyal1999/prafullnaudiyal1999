yaml = require('js-yaml');
fs = require('fs');

const inputfile = 'Learning.yaml';
const outputfile = 'output.json';

const json = yaml.load(fs.readFileSync(inputfile, 'utf8'));

fs.writeFileSync(outputfile, JSON.stringify(json, null, 2));