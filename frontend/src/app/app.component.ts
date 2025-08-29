import { Component, OnInit, OnDestroy } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { LoginComponent } from './components/login/login.component';
import { AuthService, User } from './services/auth.service';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'bus-reservation-frontend';
 
  isAuthenticated: boolean = false;
  currentUser: User | null = null;


  private authStatusSubscription: Subscription | undefined;
  private currentUserSubscription: Subscription | undefined;

  constructor(
    private authService: AuthService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.authStatusSubscription = this.authService.isAuthenticated$.subscribe(status => {
      this.isAuthenticated = status;
    });
    this.currentUserSubscription = this.authService.currentUser$.subscribe(user => {
      this.currentUser = user;
    });
  }

  ngOnDestroy(): void {
    this.authStatusSubscription?.unsubscribe();
    this.currentUserSubscription?.unsubscribe();
  }

  goHome(): void {
    this.router.navigate(['/home']);
  }

  openLogin(): void {
    this.router.navigate(['/login']);
  }

  logout(): void {
    this.authService.logout().subscribe({
      next: () => {
        this.router.navigate(['/login']);
      },
      error: (err) => {
        console.error('Logout failed:', err);
      }
    });
  }
}