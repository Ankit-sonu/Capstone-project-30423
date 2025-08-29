import { Component, Input } from '@angular/core';
import { Product } from '../productlist/Product';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {

  products : Product[] = [
    {id:1,name:"Keyboard", price:799},
    {id:2,name:"Guitair", price:599},
    {id:3,name:"Violin", price:1299},
    {id:4,name:"Drums", price:699},
    {id:5,name:"Flute", price:299}
  ]

additem(selectProduct:Product){
  this.products.push(selectProduct);
}
  
}