import { Country} from "./Country";
import { InputPort } from "./Ports";

const REST_ENDPOINT = 'https://restcountries.com/v3.1/all?fields=name,capital,population,cioc,region';

export class RestCountriesInputAdapter implements InputPort {
   private constructor(private countries: Country[]) {}

  public load_all(): Country[] {
    return this.countries; 
  }

  static async instance(): Promise<RestCountriesInputAdapter> {
    let response = await fetch(REST_ENDPOINT, {
      method: 'GET'
    });
    let jsonResponse = await response.json();
    //let restCountries = JSON.parse(JSON.stringify(responseAsJson));
  
    return new RestCountriesInputAdapter(jsonResponse.map((country: any) => new Country(country.name.common, country.capital[0], country.population)));
  }
}
