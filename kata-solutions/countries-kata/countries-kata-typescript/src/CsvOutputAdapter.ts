import { OutputPort } from "./Ports";

const fs = require('fs');

export class CsvOutputAdapter implements OutputPort {
    write(countrList: string[][]): void {
      let csvContent = "";

      countrList.forEach(function (rowArray) {
        let row = rowArray.join(",");
        csvContent += row + "\r\n";
      });

      fs.writeFileSync('countries.csv', csvContent, (error: any) => {
        if (error) throw error;
        console.log('countries.csv saved.');
      });
    }
  }
