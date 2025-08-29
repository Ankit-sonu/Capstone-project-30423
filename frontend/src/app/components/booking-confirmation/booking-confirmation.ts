import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BookingService } from '../../services/booking.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-booking-confirmation',
  templateUrl: './booking-confirmation.html',
  styleUrls: ['./booking-confirmation.css']
})
export class BookingConfirmationComponent implements OnInit {
  bookingDetails: any;
  isLoading = true;
  bookingId: string | null = null;

  constructor(
    private route: ActivatedRoute,
    private bookingService: BookingService,
    private snackBar: MatSnackBar
  ) { }

  ngOnInit(): void {
    this.bookingId = this.route.snapshot.paramMap.get('id');
    if (this.bookingId) {
      this.fetchBookingDetails(this.bookingId);
    } else {
      this.snackBar.open('❌ Booking ID not found!', 'Close', { duration: 3000 });
      this.isLoading = false;
    }
  }

  fetchBookingDetails(bookingId: string): void {
    this.bookingService.getBookingDetails(bookingId).subscribe({
      next: (data) => {
        this.bookingDetails = data;
        this.isLoading = false;
      },
      error: (err) => {
        console.error('Error fetching booking details:', err);
        this.snackBar.open('❌ Failed to load booking details.', 'Close', { duration: 3000 });
        this.isLoading = false;
      }
    });
  }
}
