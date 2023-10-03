import {
    ChangeDetectorRef,
    Component,
    Input,
    OnInit,
    ViewEncapsulation
} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {untilDestroyed, UntilDestroy} from '@ngneat/until-destroy';
import {PlayersService} from '../_services/players.service';
import { trigger, style, animate, transition } from '@angular/animations';

@UntilDestroy()
@Component({
  selector: 'card-component',
  templateUrl: './card-component.component.html',
  styleUrls: ['./card-component.component.scss'],
  animations: [
    trigger(
      'inOutAnimation', 
      [
        transition(
          ':enter', 
          [
          style({ height: 20, opacity: 0 }),
          animate('1s ease-out', 
            style({ height: '*', opacity: 1 }))
          ]
        ),
        transition(
          ':leave', 
          [
          style({ height: '*', opacity: 1 }),
          animate('1s ease-in', 
            style({ height: 20, opacity: 0 }))
          ]
        )
      ]
    )
  ],
  encapsulation: ViewEncapsulation.None,
})
export class CardComponent implements OnInit {

    @Input()
    playerID: number;
    
    name: string;
    games: any;

    avgMinutes: number;
    avgPoints: number;
    avgFG: number;
    avgRebounds: number;
    avgAssits: number;

    numGames: number;

    displayTotalStatsDiv: boolean = false;

    totalStats: {
        "minutes": any,
        "points": any,
        "assists": any,
        "offensiveRebounds": any,
        "defensiveRebounds": any,
        "steals": any,
        "blocks": any,
        "turnovers": any,
        "defensiveFouls": any,
        "offensiveFouls": any,
        "freeThrowsMade": any,
        "freeThrowsAttempted": any,
        "twoPointersMade": any,
        "twoPointersAttempted": any,
        "threePointersMade": any,
        "threePointersAttempted": any
      };

    constructor(
        protected activatedRoute: ActivatedRoute,
        protected cdr: ChangeDetectorRef,
        protected playersService: PlayersService,
    ) {
    
    }

    ngOnInit(): void {
        this.fetchApiResponse(this.playerID);
    }

    displayName(id): void {
        this.displayTotalStatsDiv = !this.displayTotalStatsDiv;
    }

    fetchApiResponse(id): void {
        this.playersService.getPlayerSummary(this.playerID).pipe(untilDestroyed(this)).subscribe(data => {
            this.name = data.apiResponse.name;
            this.games = data.apiResponse.games;

            this.numGames = this.games.length;
      
            this.sumTotalStats();
          });
    }

    getTotal = (field: string) => {
        const gamesArray = Object.values(this.games);
    
        let total = 0;
    
        for (const game of gamesArray) {
          const value = game[field];
          total += value;
        }
    
        return total;
    };

    round = (value: number): number => {
        return Math.round(10 * value) / 10;
    };
    
    fgRound = (value: number): number => {
        return Math.round(1000 * value) / 1000;
    };

    sumTotalStats() {
        this.totalStats = {
            "minutes": this.getTotal("minutes"),
            "points": this.getTotal("points"),
            "assists": this.getTotal("assists"),
            "offensiveRebounds": this.getTotal("offensiveRebounds"),
            "defensiveRebounds": this.getTotal("defensiveRebounds"),
            "steals": this.getTotal("steals"),
            "blocks": this.getTotal("blocks"),
            "turnovers": this.getTotal("turnovers"),
            "defensiveFouls": this.getTotal("defensiveFouls"),
            "offensiveFouls": this.getTotal("offensiveFouls"),
            "freeThrowsMade": this.getTotal("freeThrowsMade"),
            "freeThrowsAttempted": this.getTotal("freeThrowsAttempted"),
            "twoPointersMade": this.getTotal("twoPointersMade"),
            "twoPointersAttempted": this.getTotal("twoPointersAttempted"),
            "threePointersMade": this.getTotal("threePointersMade"),
            "threePointersAttempted": this.getTotal("threePointersAttempted")
        };

        this.avgMinutes = this.round(this.totalStats.minutes / this.numGames);
        this.avgPoints = this.round(this.totalStats.points / this.numGames);
        this.avgFG = parseFloat((this.fgRound((this.totalStats.twoPointersMade + this.totalStats.threePointersMade) / (this.totalStats.twoPointersAttempted + this.totalStats.threePointersAttempted)) * 10 * 10).toFixed(2));
        this.avgAssits = this.round(this.totalStats.assists / this.numGames);
        this.avgRebounds = this.round((this.totalStats.offensiveRebounds + this.totalStats.defensiveRebounds) / this.numGames);
      
    }
}