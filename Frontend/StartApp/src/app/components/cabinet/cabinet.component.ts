import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cabinet',
  templateUrl: './cabinet.component.html',
  styleUrls: ['./cabinet.component.scss']
})
export class CabinetComponent implements OnInit {

  constructor() { }
  page: number = 1

  ngOnInit(): void {
    this.bindSidebar()
  }

  bindSidebar() {
    let items = document.getElementsByClassName("item")
    for (let i = 0; i < items.length; i++) {
      items[i].addEventListener("click", (event) => {
        let active = document.getElementsByClassName("bg-gray-700")
        if (active.length >= 1) {
          active[0].classList.toggle("bg-gray-700")
        }
        items[i].classList.toggle("bg-gray-700")
      })
    }
  }

}
