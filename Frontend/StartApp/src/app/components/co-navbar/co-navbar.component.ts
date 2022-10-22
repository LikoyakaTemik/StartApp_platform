import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-co-navbar',
  templateUrl: './co-navbar.component.html',
  styleUrls: ['./co-navbar.component.scss']
})
export class CoNavbarComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    let rotated: boolean = false

    function toggleMenu(event: any) {
      if (event.target != null){
        if (!rotated){
          event.target.style.transform = "rotate(90deg)"
          rotated = true
        }
        else {
          event.target.style.transform = "rotate(0deg)"
          rotated = false
        }
      }
      let element = document.getElementById("responsive-menu")
      if (element != null) {
        element.classList.toggle('visible')
      }
    }

    let menuButton = document.getElementById("menu-btn")
    if (menuButton != null) {
      menuButton.addEventListener("click", toggleMenu)
    }
  }

}
