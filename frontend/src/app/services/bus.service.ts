import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';

export interface Bus {
  id: number;
  operator: string;
  type: string;
  departure: string;
  arrival: string;
  price: number;
  available: number;
  total_seats: number;
  amenities: string[];
  rating: number;
}

export interface SearchParams {
  origin: string;
  destination: string;
  date: string;
}

@Injectable({
  providedIn: 'root'
})
export class BusService {
  private apiUrl = 'http://localhost:5000/api';

  constructor(private http: HttpClient) {}

  searchBuses(params: SearchParams): Observable<{buses: Bus[]}> {
    const queryParams = `origin=${params.origin}&destination=${params.destination}&date=${params.date}`;
    return this.http.get<{buses: Bus[]}>(`${this.apiUrl}/buses/search?${queryParams}`);
  }

  getCities(): Observable<{cities: string[]}> {
    const cities = [
      'Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 
      'Hyderabad', 'Pune', 'Jaipur', 'Ahmedabad', 'Kochi',
      'Manali', 'Goa', 'Rishikesh', 'Haridwar', 'Shimla',
      'Darjeeling', 'Ooty', 'Mysore', 'Udaipur', 'Jodhpur'
    ];
    return of({cities});
  }

  getBusById(id: number): Observable<Bus> {
    return this.http.get<Bus>(`${this.apiUrl}/buses/${id}`);
  }

  bookBus(bookingData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/bookings`, bookingData);
  }
}