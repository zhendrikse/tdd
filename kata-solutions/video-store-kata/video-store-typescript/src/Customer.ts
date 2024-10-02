export class Movie {
  constructor(public readonly title: string) {}

  public getAmount(rentalDays: number): number {
    return rentalDays * 3;
  }

  public getFrequentRenterPoints(rentalDays: number): number {
    return 1;
  }
}

export class Rental {
  constructor(public readonly movie: Movie, public readonly days: number) {}

  public getAmount(): number {
    return this.movie.getAmount(this.days);
  }

  public getFrequentRenterPoints(): number {
    return this.movie.getFrequentRenterPoints(this.days)
  }
}

export class RegularMovie extends Movie {
  public getAmount(rentalDays: number): number {
    return (rentalDays > 2) ? 2 + (rentalDays - 2) * 1.5 : 2;
  }
}

export class NewRelease extends Movie {
  public getFrequentRenterPoints(rentalDays: number): number {
    return (rentalDays > 2) ? 2 : 1;
  }
}

export class Childrens extends Movie {
  public getAmount(rentalDays: number): number {
    return (rentalDays > 3) ? 1.5 + (rentalDays - 3) * 1.5 : 1.5;
  }
}

export class Statement {
  constructor(private name: String, private rentals: Rental[] = []) {}

  private getTotalFrequentRenterPoints(): number {
    return this.rentals
      .map(rental => rental.getFrequentRenterPoints())
      .reduce((acc, x) => acc + x, 0);;
  }

  private getTotalAmount(): number {
    return this.rentals
      .map(rental => rental.getAmount())
      .reduce((acc, x) => acc + x, 0);;
  }

  public asString(): string {
    let result = `Rental Record for ${this.name}\n`;

    for (let rental of this.rentals) {
      result += `\t${rental.movie.title}\t${rental.getAmount()}\n`;
    }

    result += `Amount owed is ${this.getTotalAmount()}\n`;
    result += `You earned ${this.getTotalFrequentRenterPoints()} frequent renter points\n`;

    return result;
  }
}

export class Customer {
  constructor(private name: string, private rentals: Rental[] = []) {}

  public addRental(rental: Rental): void {
    this.rentals.push(rental);
  }

  public statement(): string {
    let statement = new Statement(this.name, this.rentals);

    return statement.asString();
  }
}
