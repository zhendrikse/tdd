
'use strict';

export class Player {
  private name: string;
  private purse: number;
  private rank: number;
  private inPenaltyBox: boolean;

  constructor(name: string) {
    this.name = name;
    this.purse = 0;
    this.rank = 0;
    this.inPenaltyBox = false;
  }
  
  public play(roll: number, questions: Questions) {
    this.makeMove(roll);
    this.askQuestion(questions);
  }

  public addCoin() {
    this.purse += 1
    console.log(this.name + " now has " + this.purse + " Gold Coins.");
  }

  public hasWon(): boolean {
    return this.purse == 6
  }

  private makeMove(amount: number) {
    this.rank += amount
    if (this.rank > 11)
        this.rank -= 12
    console.log(this.name + "'s new location is " + this.rank);
    console.log("The category is " + this.currentCategory());
  }

  public currentCategory(): string {
    const rank_category_map = ["Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports"]
    if (this.rank <= 10)
      return rank_category_map[this.rank]
    else
      return "Rock"
  }

  public goToInPenaltyBox() {
    this.inPenaltyBox = true;
  }

  public isInPenaltyBox(): boolean {
    return this.inPenaltyBox;
  }

  private askQuestion(questions: Questions) {
    if (this.currentCategory() == 'Pop')
      console.log(questions.getPopQuestion());
    if (this.currentCategory() == 'Science')
      console.log(questions.getScienceQuestion());
    if (this.currentCategory() == 'Sports')
      console.log(questions.getSportsQuestion());
    if (this.currentCategory() == 'Rock')
      console.log(questions.getRockQuestion());
  }

  public toString(): string {
    return this.name;
  }
}

export class Questions {
  private popQuestions = new Array<string>();
  private scienceQuestions = new Array<string>();
  private sportsQuestions = new Array<string>();
  private rockQuestions = new Array<string>();

  public constructor() {
    for (var i = 0; i < 50; i++) {
      this.popQuestions.push("Pop Question " + i);
      this.scienceQuestions.push("Science Question " + i);
      this.sportsQuestions.push("Sports Question " + i);
      this.rockQuestions.push("Rock Question " + i);
    }
  }

  public getPopQuestion(): string {
    return this.popQuestions.shift()!;
  }

  public getRockQuestion(): string {
    return this.rockQuestions.shift()!;
  }

  public getScienceQuestion(): string {
    return this.scienceQuestions.shift()!;
  }

  public getSportsQuestion(): string {
    return this.sportsQuestions.shift()!;
  }
}

class Players {
  private players = new Array<Player>();

  private current = 0;

  public constructor(player1: Player, player2: Player, players: Player[] = []) {
    this.add(player1);
    this.add(player2);
    players.forEach(player => this.add(player));
  }

  public nextPlayersTurn() {
    this.current += 1;
    if (this.current == this.players.length)
      this.current = 0;
  }

  private add(player: Player) {
    this.players.push(player);
    console.log(player.toString() + " was added");
    console.log("They are player number " + this.players.length);
  };

  public currentPlayer(): Player {
    return this.players[this.current];
  }
}

export class Game {
  private players: Players;
  private questions = new Questions();
  private isGettingOutOfPenaltyBox = false;

  public constructor(player1: Player, player2: Player, players: Player[] = []) {
    this.players = new Players(player1, player2, players);
  }

  private tryToGetOutOfPenaltyBox(roll: number) {
    if (roll % 2 == 0) {
      console.log(this.players.currentPlayer() + " is not getting out of the penalty box");
      this.isGettingOutOfPenaltyBox = false;
      return;
    } 

    this.isGettingOutOfPenaltyBox = true;
    console.log(this.players.currentPlayer() + " is getting out of the penalty box");
  }

  public roll(roll: number) {
    console.log(this.players.currentPlayer() + " is the current player");
    console.log("They have rolled a " + roll);

    if (this.players.currentPlayer().isInPenaltyBox()) 
      this.tryToGetOutOfPenaltyBox(roll);
    else 
      this.players.currentPlayer().play(roll, this.questions);
  }


  private correctAnswerForPlayerInPenaltyBox(): boolean {
    var winner = true;

    if (this.isGettingOutOfPenaltyBox) {
      console.log('Answer was correct!!!!');
      this.players.currentPlayer().addCoin();
      winner = !this.players.currentPlayer().hasWon();
    }

    this.players.nextPlayersTurn();
    return winner;
  }

  private correctAnswerForPlayer(): boolean {
    console.log("Answer was correct!!!!");
    this.players.currentPlayer().addCoin();
    var winner = !this.players.currentPlayer().hasWon();
    this.players.nextPlayersTurn();
    return winner;
  }

  public wasCorrectlyAnswered(): boolean {
    if (this.players.currentPlayer().isInPenaltyBox()) 
      return this.correctAnswerForPlayerInPenaltyBox();

    return this.correctAnswerForPlayer();
  }

  public wrongAnswer(): boolean {
    console.log('Question was incorrectly answered');
    console.log(this.players.currentPlayer() + " was sent to the penalty box");
    this.players.currentPlayer().goToInPenaltyBox()
    this.players.nextPlayersTurn();
    return true;
  };
};

