import { Component,EventEmitter,Input, Output } from '@angular/core';
import { Product } from './Product';

@Component({
  selector: 'app-productlist',
  templateUrl: './productlist.component.html',
  styleUrls: ['./productlist.component.css']
})
export class ProductlistComponent {

  @Input()
  products : Product[]= []

  @Output()
  productSelected = new EventEmitter<Product>();

  select(p:Product){
    this.productSelected.emit(p);
  }

}

