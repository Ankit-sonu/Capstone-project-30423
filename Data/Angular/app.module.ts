import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { ToggleButtonComponent } from './toggle-button/toggle-button.component';
import { ProductlistComponent } from './productlist/productlist.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ParentComponent } from './parent/parent.component';
import { ChildComponent } from './child/child.component';

@NgModule({
  declarations: [
    AppComponent,
    ToggleButtonComponent,
    ProductlistComponent,
    DashboardComponent,
    ParentComponent,
    ChildComponent
  ],
  imports: [
    BrowserModule,
    FormsModule

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }