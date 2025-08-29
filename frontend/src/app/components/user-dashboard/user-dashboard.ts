import { Component, OnInit } from '@angular/core';
import { BookingService } from '../../services/booking.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-user-dashboard',
  templateUrl: './user-dashboard.html',
  styleUrls: ['./user-dashboard.css']
})
export class UserDashboardComponent implements OnInit {
  userBookings: any[] = [];
  isLoading = true;

  constructor(private bookingService: BookingService, private snackBar: MatSnackBar) { }

  ngOnInit(): void {
    this.fetchUserBookings();
  }

  fetchUserBookings(): void {
    this.bookingService.getUserBookings().subscribe({
      next: (data) => {
        this.userBookings = data.bookings;
        this.isLoading = false;
      },
      error: (err) => {
        console.error('Error fetching user bookings:', err);
        this.snackBar.open('❌ Failed to load your bookings.', 'Close', { duration: 3000 });
        this.isLoading = false;
      }
    });
  }

  cancelBooking(bookingId: string): void {
    if (confirm('Are you sure you want to cancel this booking?')) {
      this.bookingService.cancelBooking(bookingId).subscribe({
        next: (res) => {
          this.snackBar.open('✅ Booking cancelled successfully.', 'Close', { duration: 3000 });
          this.fetchUserBookings(); 
        },
        error: (err) => {
          console.error('Error cancelling booking:', err);
          this.snackBar.open(`❌ Failed to cancel booking: ${err.error.message || ''}`, 'Close', { duration: 4000 });
        }
      });
    }
  }
}
