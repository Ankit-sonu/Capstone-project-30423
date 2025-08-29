import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.css']
})
export class ChildComponent {
  product = {
    id: '',
    name: '',
    price: 0
  };

  @Output() productAdded = new EventEmitter<any>();

  submitProduct() {
    this.productAdded.emit({ ...this.product });
    this.product = { id: '', name: '', price: 0 }; // Reset form
  }

}s