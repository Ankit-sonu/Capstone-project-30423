import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, of } from 'rxjs';
import { tap, catchError } from 'rxjs/operators';

export interface User {
  id: number;
  name: string;
  email: string;
  phone: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  message: string;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = '/api'; 
  private _isAuthenticated = new BehaviorSubject<boolean>(false);
  isAuthenticated$ = this._isAuthenticated.asObservable();

  private _currentUser = new BehaviorSubject<User | null>(null);
  currentUser$ = this._currentUser.asObservable();

  constructor(private http: HttpClient) {
    this.checkAuthenticationStatus();
  }

  private checkAuthenticationStatus(): void {
    this.http.get<any>(`${this.apiUrl}/auth/@me`, { withCredentials: true }).pipe(
      tap(response => {
        if (response.user) {
          this._isAuthenticated.next(true);
          this._currentUser.next(response.user);
        }
      }),
      catchError(() => {
        this._isAuthenticated.next(false);
        this._currentUser.next(null);
        return of(null);
      })
    ).subscribe();
  }

  login(credentials: LoginRequest): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.apiUrl}/auth/login`, credentials, { withCredentials: true })
      .pipe(
        tap(response => {
          this._isAuthenticated.next(true);
          this.checkAuthenticationStatus(); 
        })
      );
  }

  register(userData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/register`, userData, { withCredentials: true });
  }

  logout(): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/auth/logout`, {}, { withCredentials: true })
      .pipe(
        tap(() => {
          this._isAuthenticated.next(false);
          this._currentUser.next(null);
        })
      );
  }

  isLoggedIn(): boolean {
    let loggedInStatus = false;
    this.isAuthenticated$.subscribe(status => loggedInStatus = status).unsubscribe();
    return loggedInStatus;
  }
}