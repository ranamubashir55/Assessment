import { Component } from '@angular/core';
import { NgForm, ReactiveFormsModule, FormsModule } from '@angular/forms';
import { ActionsService } from './service/actions.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Assignment';
  statsData = [];
  constructor(private _actionService: ActionsService) { }


  getStats(ipForm: NgForm) {
    // USING SERVICE TO GET DATA FROM SERVER

    this._actionService.stats(ipForm.value)
    .subscribe( data => { 
      let max = 0;
      let  index = 0;
      data.forEach((data,i) => {
        data.class = "";
        if (parseInt(data.use) > max) {
          max = parseInt(data.use);
          index = i;
        }
      });
      data[index].class = "red";

       console.log(data)
       this.statsData = data;
    },error => {
       // console.log('Error', error);
      }
    );
  }


  addVm(ip:string, username:string, password:string){
    console.log(ip)
  }
}
