const { readFile, writeFile } = require('fs').promises;
const { json2csvAsync } = require('json-2-csv');
const path = require('path');
const fs = require('fs')

const currentDirectory = path.resolve();
const parentDirectory = path.join(currentDirectory, '..');
const fileDirectory = `${parentDirectory}/fileStorage`
const filePath = `${parentDirectory}/fileStorage/data.csv`


if(!fs.existsSync(fileDirectory)){
    fs.mkdirSync(fileDirectory);
    console.log("Directory Created Successfully!")
}

async function parseJSONFile (fileName) {
    try {
      const file = await readFile(fileName);
      return JSON.parse(file);
    } catch (err) {
      console.log(err);
      process.exit(1);
    }
  }
  
  async function writeCSV (fileName, data) {
    await writeFile(fileName, data, 'utf8');
  }

  const jsonData = {
    "ID": "123fafe",
    "Name": "Adss",
    "Age": 24,
    "Email": "nss@email.com",
    "Status": "M"
};
  
  (async () => {
    // const data = await parseJSONFile("data/data.json");
    const csv = await json2csvAsync(jsonData);
    await writeCSV(filePath, csv);
    console.log("CSV file created successfully!");
  })();