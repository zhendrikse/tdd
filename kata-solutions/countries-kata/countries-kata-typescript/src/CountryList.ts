'use strict';

import { InputPort, OutputPort } from "./Ports";
import { Country} from "./Country";
import { RestCountriesInputAdapter } from "./RestCountriesInputAdapter";
import { CsvOutputAdapter } from "./CsvOutputAdapter";

export class CountryList {
  private countryList: Country[];
  private outputPort: OutputPort;
  
   private constructor(inputPort: InputPort, outputPort: OutputPort) {
    this.countryList = inputPort.load_all();
    this.outputPort = outputPort;
  }

  static async create_instance(inputPort: InputPort, outputPort: OutputPort = new CsvOutputAdapter()): Promise<CountryList> {
     return new CountryList(inputPort, outputPort);
  }

  public compare(country1: Country, country2: Country): number {
    return country1.population - country2.population
  }

  public sorted_by_population(): Country[] {
    return this.countryList.sort(this.compare);
  }

  public sumOf(anArray: number[]): number {
    return anArray.reduce((total, item) => total + item, 0);
  }

  public average_population() {
    if (!this.countryList.length)
      return 0;

    var totalPopulation = this.sumOf(this.countryList.map(country => country.population));
    return totalPopulation / this.countryList.length;
  }

  public standard_deviation(): number {
    if (!this.countryList.length)
      return 0;

    var average = this.average_population();
    var diviationsList = this.countryList.map(country => (country.population - average) * (country.population - average));
    return Math.sqrt(this.sumOf(diviationsList) / this.countryList.length)
  }

  public standard_deviations_for(country: Country): number {
    var standardDeviations = Math.abs(this.average_population() - country.population) / this.standard_deviation();
    return Math.round((standardDeviations + Number.EPSILON) * 100) / 100
  }

  public as_nested_array(): string[][] {
    var sortedCountries = this.sorted_by_population();
    return sortedCountries.map(country => [country.name, country.capital, String(country.population), String(this.standard_deviations_for(country))]);
  }

  to_csv() {
    this.outputPort.write(this.as_nested_array());
  }
}


async function main() {
  let countryList = await CountryList.create_instance(await RestCountriesInputAdapter.instance());
  countryList.to_csv();
}

if (require.main === module) {
  main();
}