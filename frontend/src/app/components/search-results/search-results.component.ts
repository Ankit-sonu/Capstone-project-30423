import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BusService } from '../../services/bus.service';
import { BookingService } from '../../services/booking.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-search-results',
  templateUrl: './search-results.component.html',
  styleUrls: ['./search-results.component.scss']
})
export class SearchResultsComponent implements OnInit {
  buses: any[] = [];
  searchParams: any = {};
  isLoading = true;
  isBooking = false;

  private mapBusIdForRoute(uiBusId: number, origin: string, destination: string): number {
    const o = (origin || '').toLowerCase();
    const d = (destination || '').toLowerCase();
 
    if (o === 'delhi' && d === 'manali') {
      return uiBusId === 2 ? 2 : 1;
    }
    if (o === 'mumbai' && d === 'pune') {
      return uiBusId === 3 || uiBusId === 4 ? uiBusId : 3;
    }
    if (o === 'bangalore' && d === 'chennai') {
      return 9; 
    }
    if (o === 'delhi' && d === 'jaipur') {
      return 11; 
    }
    if (o === 'kolkata' && d === 'darjeeling') {
      return 13;
    }
 
    return 1;
  }

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private busService: BusService,
    private bookingService: BookingService,
    private snackBar: MatSnackBar
  ) {}

  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      this.searchParams = params;
      this.searchBuses();
    });
  }

  searchBuses() {
    this.isLoading = true;

    setTimeout(() => {
      this.buses = [
        {
          id: 1,
          operator: 'Himachal Tourism',
          type: 'Volvo AC Sleeper',
          departure: '20:00',
          arrival: '08:00+1',
          price: 1200,
          duration: '12h 0m',
          available: 12,
          total: 40,
          amenities: ['AC', 'WiFi', 'Charging', 'Blanket', 'Entertainment'],
          rating: 4.5,
          image: 'https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=200&h=120&fit=crop'
        },
        {
          id: 2,
          operator: 'RedBus Travels',
          type: 'Semi-Sleeper AC',
          departure: '21:30',
          arrival: '10:00+1',
          price: 900,
          duration: '12h 30m',
          available: 8,
          total: 35,
          amenities: ['AC', 'Charging', 'Water'],
          rating: 4.2,
          image: 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=200&h=120&fit=crop'
        },
        {
          id: 3,
          operator: 'Mountain Express',
          type: 'Deluxe AC',
          departure: '19:00',
          arrival: '07:30+1',
          price: 1100,
          duration: '12h 30m',
          available: 15,
          total: 42,
          amenities: ['AC', 'WiFi', 'Snacks', 'Blanket'],
          rating: 4.3,
          image: 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=200&h=120&fit=crop'
        }
      ];
      this.isLoading = false;
    }, 1500);
  }

  bookBus(bus: any) {
    if (this.isBooking) { return; }
    this.isBooking = true;
    const seats = ['A1']; 
    const resolvedBusId = this.mapBusIdForRoute(bus.id, this.searchParams.origin, this.searchParams.destination);
    if (!resolvedBusId || (this.searchParams.origin?.toLowerCase() === this.searchParams.destination?.toLowerCase())) {
      this.snackBar.open('🚫 This route is not available for booking in the demo.', 'Close', { duration: 3000 });
      this.isBooking = false;
      return;
    }
    const payload = {
      bus_id: resolvedBusId,
      origin: this.searchParams.origin,
      destination: this.searchParams.destination,
      travel_date: this.searchParams.date,
      seat_numbers: seats,
      total_amount: bus.price * seats.length
    };
    this.bookingService.createBooking(payload).subscribe({
      next: (res) => {
        this.snackBar.open('✅ Booking created!', 'Close', { duration: 2500 });
        this.isBooking = false;
        this.router.navigate(['/user/dashboard']);
      },
      error: (err) => {
        console.error('Booking failed', err);
        this.snackBar.open('❌ Booking failed', 'Close', { duration: 3000 });
        this.isBooking = false;
      }
    });
  }

  goBack() {
    this.router.navigate(['/home']);
  }
}