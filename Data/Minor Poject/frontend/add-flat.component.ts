import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

export interface Flat {
  type: string;
  price: number;
  location: string;
  image: string;
}

@Component({
  selector: 'app-add-flat',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './add-flat.component.html',
  styleUrls: ['./add-flat.component.css']
})
export class AddFlatComponent {
  flat: Flat = { type: '', price: 0, location: '', image: '' };

  constructor(private router: Router) {}

  private getRandomImage(type: string): string {
    const images: { [key: string]: string[] } = {
      "1BHK": [
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800",
        "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=800",
        "https://images.unsplash.com/photo-1599423300746-b62533397364?w=800"
      ],
      "2BHK": [
        "https://images.unsplash.com/photo-1600585154154-0c14f0c1f3c2?w=800",
        "https://images.unsplash.com/photo-1560448075-bb8c1a3c4ef4?w=800",
        "https://images.unsplash.com/photo-1600047509807-7e7f8a90be4b?w=800"
      ],
      "3BHK": [
        "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800",
        "https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=800",
        "https://images.unsplash.com/photo-1600585154208-466b4cbb154d?w=800"
      ]
    };

    const imgs = images[type] || images["1BHK"];
    return imgs[Math.floor(Math.random() * imgs.length)];
  }

  onSubmit() {
    const savedFlats = JSON.parse(localStorage.getItem('flats') || '[]');
    this.flat.image = this.getRandomImage(this.flat.type);
    savedFlats.push(this.flat);
    localStorage.setItem('flats', JSON.stringify(savedFlats));
    this.router.navigate(['/list']);
  }
}
