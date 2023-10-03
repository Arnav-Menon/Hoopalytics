import {ModuleWithProviders} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {CardComponent} from './card-component.component';


const routes: Routes = [
  { path: '', component: CardComponent, data: { title: 'Player Summary'} },
];

export const routing: ModuleWithProviders<RouterModule> = RouterModule.forChild(routes);