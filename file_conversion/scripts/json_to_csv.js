const fs = require("fs");
const createCsvWriter = require("csv-writer").createObjectCsvWriter;

// Read the JSON file
fs.readFile("data.json", "utf8", (err, data) => {
  if (err) throw err;

  // Parse the JSON data into a JavaScript object
  const jsonData = JSON.parse(data);

  // Define the headers for the CSV file
  const csvWriter = createCsvWriter({
    path: "data.csv",
    header: [
      { id: "id", title: "ID" },
      { id: "name", title: "Name" },
      { id: "age", title: "Age" },
      { id: "email", title: "Email" },
    ],
  });

  // Write the data to the CSV file
  csvWriter.writeRecords(jsonData).then(() => {
    console.log("CSV file created successfully!");
  });
});
