import { Routes } from '@angular/router';
import { AddFlatComponent } from './components/add-flat/add-flat.component';
import { ListFlatsComponent } from './components/list-flats/list-flats.component';

export const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'home' },
  { path: 'home', component: ListFlatsComponent },
  { path: 'add', component: AddFlatComponent },
  { path: 'list', component: ListFlatsComponent }
];
