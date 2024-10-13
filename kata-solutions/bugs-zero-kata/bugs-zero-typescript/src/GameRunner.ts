'use strict';

import { Game, Player } from "./Game"
import seedrandom from "seedrandom";

export class GameRunner {
    private notAWinner: boolean;
    private randomNumberGenerator = seedrandom('1234');

    public constructor() {
        this.notAWinner = false;
    }

    public doRoll(): number {
        return Math.floor(this.randomNumberGenerator() * 6) + 1;
    }

    public playGame(rand: number) {
        var game = new Game(new Player('Chet'), new Player('Pat'), [new Player('Sue')]);

        while (true) {
            game.roll(rand);

            if (Math.floor(this.randomNumberGenerator() * 10) == 7)
                this.notAWinner = game.wrongAnswer();
            else
                this.notAWinner = game.wasCorrectlyAnswered();

            if (!this.notAWinner)
                break;
        }
    }
}
