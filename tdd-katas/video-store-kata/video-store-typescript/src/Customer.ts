export enum MovieType {
  REGULAR = "Regular movie",
  NEW_RELEASE = "New release movie",
  CHILDRENS = "Childrens movie",
}

export class Movie {
  constructor(
    public readonly title: string,
    public readonly movieType: MovieType
  ) {}
}

export class Rental {
  constructor(public readonly movie: Movie, public readonly days: number) {}
}

export class Customer {
  constructor(private name: string, private rentals: Rental[] = []) {}

  public addRental(rental: Rental): void {
    this.rentals.push(rental);
  }

  public statement(): string {
    let totalAmount = 0;
    let frequentRenterPoints = 0;
    let result = `Rental Record for ${this.name}\n`;

    for (let rental of this.rentals) {
      let thisAmount = 0;

      // determine amount for each movie
      switch (rental.movie.movieType) {
        case MovieType.REGULAR:
          thisAmount = 2;
          if (rental.days > 2) {
            thisAmount += (rental.days - 2) * 1.5;
          }
          break;
        case MovieType.NEW_RELEASE:
          thisAmount = rental.days * 3;
          break;
        case MovieType.CHILDRENS:
          thisAmount = 1.5;
          if (rental.days > 3) {
            thisAmount += (rental.days - 3) * 1.5;
          }
          break;
      }

      //add frequent renter points
      frequentRenterPoints++;
      // add bonus for a two day new release rental
      if (rental.movie.movieType === MovieType.NEW_RELEASE && rental.days > 2)
        frequentRenterPoints++;

      //print figures for this rental
      result += `\t${rental.movie.title}\t${thisAmount}\n`;
      totalAmount += thisAmount;
    }
    // add footer lines
    result += `Amount owed is ${totalAmount}\n`;
    result += `You earned ${frequentRenterPoints} frequent renter points\n`;

    return result;
  }
}
