import { Component, Input, OnInit } from '@angular/core';
import { IUser } from 'src/app/models/users.model';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-co-navbar',
  templateUrl: './co-navbar.component.html',
  styleUrls: ['./co-navbar.component.scss']
})
export class CoNavbarComponent implements OnInit {

  constructor(private auth: AuthService) { }

  @Input() user: IUser | null = null

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

    function toggleDropdown(event: any) {
      let dropdown = document.getElementById("dd-account")
      if (dropdown != null) {
        dropdown.classList.toggle("visible")
      }
    }

    let menuButton = document.getElementById("menu-btn")
    if (menuButton != null) {
      menuButton.addEventListener("click", toggleMenu)
    }
    let accountButton = document.getElementById("btn-account")
    if (accountButton != null) {
      accountButton.addEventListener("click", toggleDropdown)
    }
  }

  logout() {
    this.auth.logout()
    this.user = null
  }

}
