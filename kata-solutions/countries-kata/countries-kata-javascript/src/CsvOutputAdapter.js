const fs = require('fs');

class CsvOutputAdapter {
    write(countrList) {
      let csvContent = "";
  
      countrList.forEach(function (rowArray) {
        let row = rowArray.join(",");
        csvContent += row + "\r\n";
      });
  
      fs.writeFileSync('countries.csv', csvContent, (err) => {
        if (err) throw err;
        console.log('countries.csv saved.');
      });
    }
  }

module.exports = {
    CsvOutputAdapter: CsvOutputAdapter
}