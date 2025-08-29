import { Injectable } from '@angular/core';

export interface Flat {
  type: string;
  price: number;
  location: string;
}

@Injectable({
  providedIn: 'root'
})
export class FlatService {
  private flats: Flat[] = [];

  getFlats(): Flat[] {
    return this.flats;
  }

  addFlat(flat: Flat): void {
    this.flats.push(flat);
  }

  deleteFlat(index: number): void {
    this.flats.splice(index, 1);
  }
}
