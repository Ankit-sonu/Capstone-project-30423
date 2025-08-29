import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { AuthService } from '../../services/auth.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  loginForm: FormGroup;
  registerForm: FormGroup;
  isLoginMode = true;
  isLoading = false;
  selectedIndex = 0;
  currentRoute: string = '';

  constructor(
    private fb: FormBuilder,
    private snackBar: MatSnackBar,
    private authService: AuthService,
    private router: Router,
    private route: ActivatedRoute
  ) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });

    this.registerForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(2)]],
      email: ['', [Validators.required, Validators.email]],
      phone: ['', [Validators.pattern('^[0-9]{10}$')]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['', [Validators.required]]
    }, { validators: this.passwordMismatchValidator });
  }

  ngOnInit(): void {
    this.route.url.subscribe(url => {
      this.currentRoute = url[0]?.path;
      if (this.currentRoute === 'signup') {
        this.isLoginMode = false;
        this.selectedIndex = 1;
      } else {
        this.isLoginMode = true;
        this.selectedIndex = 0;
      }
    });
  }

  passwordMismatchValidator(form: FormGroup) {
    return form.get('password')?.value === form.get('confirmPassword')?.value
      ? null : { 'mismatch': true };
  }

  onLogin() {
    if (this.loginForm.valid) {
      this.isLoading = true;
      const { email, password } = this.loginForm.value;

      let loginObservable: Observable<any>;

      loginObservable = this.authService.login({ email, password });

      loginObservable.subscribe({
        next: (res: any) => {
          this.isLoading = false;
          this.snackBar.open('✅ Login successful!', 'Close', { duration: 3000 });
          this.authService.currentUser$.subscribe(user => {
            if (user) {
              this.router.navigate(['/user/dashboard']);
            } else {
              this.snackBar.open('❌ Login successful, but user data not found.', 'Close', { duration: 4000 });
            }
          }).unsubscribe(); 
        },
        error: (err) => {
          this.isLoading = false;
          this.snackBar.open(`❌ Invalid credentials! ${err.error.message || ''}`, 'Close', { duration: 4000 });
        }
      });
    }
  }

  onRegister() {
    if (this.registerForm.valid) {
      const { name, email, phone, password } = this.registerForm.value;
      this.isLoading = true;
      this.authService.register({ name, email, phone, password }).subscribe({
        next: (res: any) => {
          this.isLoading = false;
          this.snackBar.open('✅ Registration successful! Please login.', 'Close', { duration: 3000 });
          this.isLoginMode = true;
          this.selectedIndex = 0;
          this.router.navigate(['/login']);
        },
        error: (err) => {
          this.isLoading = false;
          this.snackBar.open(`❌ Registration failed! ${err.error.message || ''}`, 'Close', { duration: 4000 });
        }
      });
    }
  }

  toggleMode() {
    this.isLoginMode = !this.isLoginMode;
    this.selectedIndex = this.isLoginMode ? 0 : 1;
    this.router.navigateByUrl(this.isLoginMode ? '/login' : '/signup');
  }

  onTabChange(index: number) {
    this.selectedIndex = index;
    this.isLoginMode = index === 0;
    this.router.navigateByUrl(this.isLoginMode ? '/login' : '/signup');
  }
}
