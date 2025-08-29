import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { BusService } from '../../services/bus.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  searchForm: FormGroup;
  cities: string[] = [];
  isLoading = false;

  popularRoutes = [
    { 
      origin: 'Delhi', 
      destination: 'Manali', 
      price: '₹900-1200',
      duration: '12-14 hours',
      image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=250&fit=crop',
      description: 'Experience the breathtaking beauty of Himachal Pradesh',
      icon: '🏔️'
    },
    { 
      origin: 'Mumbai', 
      destination: 'Pune', 
      price: '₹400-600',
      duration: '3-4 hours',
      image: 'https://images.unsplash.com/photo-1567157577867-05ccb1388e66?w=400&h=250&fit=crop',
      description: 'Quick journey to Maharashtra cultural capital',
      icon: '🌊'
    },
    { 
      origin: 'Bangalore', 
      destination: 'Chennai', 
      price: '₹600-900',
      duration: '6-7 hours',
      image: 'https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=400&h=250&fit=crop',
      description: 'Connect the IT hubs of South India',
      icon: '🏛️'
    },
    { 
      origin: 'Delhi', 
      destination: 'Jaipur', 
      price: '₹500-800',
      duration: '5-6 hours',
      image: 'https://images.unsplash.com/photo-1599661046289-e31897846e41?w=400&h=250&fit=crop',
      description: 'Discover the Pink City of Rajasthan',
      icon: '🕌'
    },
    { 
      origin: 'Kolkata', 
      destination: 'Darjeeling', 
      price: '₹900-1300',
      duration: '10-12 hours',
      image: 'https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=400&h=250&fit=crop',
      description: 'Journey to the Queen of Hills',
      icon: '⛰️'
    },
    { 
      origin: 'Goa', 
      destination: 'Mumbai', 
      price: '₹700-1000',
      duration: '8-10 hours',
      image: 'https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=400&h=250&fit=crop',
      description: 'From beaches to commercial capital',
      icon: '🏖️'
    }
  ];

  features = [
    {
      icon: 'verified',
      title: 'Verified Operators',
      description: 'All bus operators are verified and trusted'
    },
    {
      icon: 'schedule',
      title: 'Real-time Tracking',
      description: 'Track your bus in real-time'
    },
    {
      icon: 'payment',
      title: 'Secure Payments',
      description: 'Multiple payment options with security'
    },
    {
      icon: 'support_agent',
      title: '24/7 Support',
      description: 'Round the clock customer support'
    }
  ];

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private snackBar: MatSnackBar,
    private busService: BusService
  ) {
    this.searchForm = this.fb.group({
      origin: ['', Validators.required],
      destination: ['', Validators.required],
      date: ['', Validators.required]
    });
  }

  ngOnInit() {
    this.loadCities();
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    this.searchForm.patchValue({ date: tomorrow });
  }

  loadCities() {
    this.cities = [
      'Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 
      'Hyderabad', 'Pune', 'Jaipur', 'Ahmedabad', 'Kochi',
      'Manali', 'Goa', 'Rishikesh', 'Haridwar', 'Shimla',
      'Darjeeling', 'Ooty', 'Mysore', 'Udaipur', 'Jodhpur'
    ];
  }

  onSearch() {
    if (this.searchForm.valid) {
      const formValue = this.searchForm.value;

      if (formValue.origin === formValue.destination) {
        this.snackBar.open('🚫 Origin and destination cannot be same!', 'Close', { duration: 3000 });
        return;
      }

      const searchParams = {
        origin: formValue.origin,
        destination: formValue.destination,
        date: this.formatDate(formValue.date)
      };

      this.isLoading = true;

      setTimeout(() => {
        this.isLoading = false;
        this.snackBar.open('🎉 Found buses for your journey!', 'Close', { duration: 3000 });
        this.router.navigate(['/search-results'], { queryParams: searchParams });
      }, 2000);
    } else {
      this.snackBar.open('📝 Please fill all fields!', 'Close', { duration: 3000 });
    }
  }

  onPopularRouteClick(route: any) {
    this.searchForm.patchValue({
      origin: route.origin,
      destination: route.destination
    });

    document.querySelector('.search-form-container')?.scrollIntoView({ behavior: 'smooth' });
    this.snackBar.open(`🚌 Route selected: ${route.origin} → ${route.destination}`, 'Close', { duration: 2000 });
  }

  swapCities() {
    const origin = this.searchForm.get('origin')?.value;
    const destination = this.searchForm.get('destination')?.value;

    this.searchForm.patchValue({
      origin: destination,
      destination: origin
    });

    this.snackBar.open('🔄 Cities swapped!', 'Close', { duration: 2000 });
  }

  private formatDate(date: Date): string {
    return date.toISOString().split('T')[0];
  }
}