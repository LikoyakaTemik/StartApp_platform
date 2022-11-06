import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { IErrors, IErrorsLogin } from 'src/app/models/register.model';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup
  submit: boolean = false
  errors: IErrorsLogin = {
    username: false,
    password: false,
  }

  globalError = false
  
  constructor(private auth: AuthService, private router: Router) {}

  ngOnInit(): void {
    this.loginForm = new FormGroup({
      username: new FormControl("", [Validators.required]),
      password: new FormControl("", [Validators.required, Validators.minLength(8)]),
    })
  }

  on_submit() {
    this.submit = true
    if (this.loginForm.valid){
      this.auth.login({username: this.loginForm.controls['username'].value, password: this.loginForm.controls['password'].value})
      .subscribe({
        next: (result) => {
          if ('errors' in result) {
            if (result.errors != null) {
              console.log("ошибки")
              this.errors = result.errors
              if (result.exception != 400) {
                this.globalError = true
              } else {
                this.globalError = false
              }
            }
          } else {
            if ( result.user != undefined) {
              this.auth.setUser({'username': "joe"})
              this.router.navigate(['/home'])
            } else {
              this.globalError = true
            }
          }
        },
        error: error => this.globalError = true,
      })
    }
  }

}
