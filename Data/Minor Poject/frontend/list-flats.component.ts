import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { Flat } from '../add-flat/add-flat.component';

@Component({
  selector: 'app-list-flats',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './list-flats.component.html',
  styleUrls: ['./list-flats.component.css']
})
export class ListFlatsComponent implements OnInit {
  flats: Flat[] = [];

  constructor(private router: Router) {}

  ngOnInit(): void {
    this.flats = JSON.parse(localStorage.getItem('flats') || '[]');
  }

  deleteFlat(index: number) {
    this.flats.splice(index, 1);
    localStorage.setItem('flats', JSON.stringify(this.flats));
  }
}
