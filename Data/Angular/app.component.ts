import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'mydemos';
  username = "admin"
  passwd = "admin"
  validUser  = false;
  txt =""
;
  validate(){
    if (this.username === "admin" && this.passwd === "admin"){
      this.validUser=true;
      console.log(this.username+" "+this.passwd)
    }
    else{
      this.validUser=false;
      console.log(this.username+" "+this.passwd)
    }
  }
}