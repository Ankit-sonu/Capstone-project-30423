import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { SearchResultsComponent } from './components/search-results/search-results.component';
import { BookingConfirmationComponent } from './components/booking-confirmation/booking-confirmation';
import { UserDashboardComponent } from './components/user-dashboard/user-dashboard'; 
import { AuthGuard } from './services/auth.guard'; 

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: LoginComponent }, 
  { path: 'search-results', component: SearchResultsComponent },
  { path: 'bus/book/:id', component: BookingConfirmationComponent, canActivate: [AuthGuard] }, 
  { path: 'user/dashboard', component: UserDashboardComponent, canActivate: [AuthGuard] }, 
  { path: '**', redirectTo: '/home' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
    scrollPositionRestoration: 'top'
  })],
  exports: [RouterModule]
})
export class AppRoutingModule { }