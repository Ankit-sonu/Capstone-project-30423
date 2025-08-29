import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class BookingService {
  private apiUrl = '/api'; 

  constructor(private http: HttpClient, private authService: AuthService) { }

  

  createBooking(bookingData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/bookings`, bookingData, { withCredentials: true });
  }

  getBookingDetails(bookingId: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/bookings/${bookingId}`, { withCredentials: true });
  }

  getUserBookings(): Observable<any> {
    return this.http.get(`${this.apiUrl}/bookings/user`, { withCredentials: true });
  }

  

  cancelBooking(bookingId: string): Observable<any> {
    return this.http.put(`${this.apiUrl}/bookings/${bookingId}/cancel`, {}, { withCredentials: true });
  }
}
