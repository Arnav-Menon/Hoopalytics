import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {CardComponent} from './card-component.component';
import {routing} from 'app/player-summary/player-summary.routing';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatCardModule} from '@angular/material/card';
import {FlexModule} from '@angular/flex-layout';
import {MatListModule} from '@angular/material/list';
import {MatRadioModule} from '@angular/material/radio';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatOptionModule} from '@angular/material/core';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {PlayersService} from 'app/_services/players.service';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
    declarations: [CardComponent],
    imports: [
      CommonModule,
      routing,
      MatToolbarModule,
      MatCardModule,
      FlexModule,
      MatListModule,
      MatRadioModule,
      MatIconModule,
      MatButtonModule,
      MatSelectModule,
      MatOptionModule,
      FormsModule,
      ReactiveFormsModule,
      BrowserAnimationsModule
    ],
    providers: [PlayersService],
    bootstrap: [CardComponent],
  })
  export class CardComponentModule { }