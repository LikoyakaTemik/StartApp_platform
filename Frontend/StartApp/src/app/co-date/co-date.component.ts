import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

const today = new Date();
const month = today.getMonth();
const year = today.getFullYear();

@Component({
  selector: 'app-co-date',
  templateUrl: './co-date.component.html',
  styleUrls: ['./co-date.component.scss']
})
export class CoDateComponent implements OnInit {

  date!: FormControl

  constructor() { }

  ngOnInit(): void {
    this.date = new FormControl()
  }

  setDate(event: any) {
    console.log(event.value, typeof event)
  }

}
