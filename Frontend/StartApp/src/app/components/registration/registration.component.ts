import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { catchError } from 'rxjs';
import { IRegister, IRegisterResponse, IErrors } from 'src/app/models/register.model';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss']
})
export class RegistrationComponent implements OnInit {
  registerForm!: FormGroup
  loginForm!: FormGroup
  submit: boolean = false
  errors: IErrors = {
    username: false,
    password: false,
    email: false
  }

  globalError = false

  constructor(private auth: AuthService, private router: Router) {}

  ngOnInit(): void {
    this.registerForm = new FormGroup({
      email: new FormControl("pavlovks2004@yandex.ru", [Validators.required, Validators.email, Validators.minLength(1)]),
      username: new FormControl("wqeqwe", [Validators.required, Validators.minLength(4)]),
      password: new FormControl("qweqweqwe123", [Validators.required, Validators.minLength(8)]),
      password2: new FormControl("qweqweqwe123", [Validators.required, Validators.minLength(8)])
    }, [passwordValidator])
  }
  
  on_submit() {
    this.submit = true
    if (this.registerForm.valid){
      this.auth.register({username: this.registerForm.controls['username'].value, password: this.registerForm.controls['password'].value, email: this.registerForm.controls['email'].value})
      .subscribe({
        next: (result) => {
          console.log(result)
          if (result.errors != null) {
            this.errors = result.errors
            if (result.exception != 400) {
              this.globalError = true
            } else {
              this.globalError = false
            }
          } else {
            this.auth.setUser(result)
            this.router.navigate(['/home'])
          }
        },
        error: error => this.globalError = true,
      })
    }
  }
}

function passwordValidator(form: AbstractControl){
  if (form.value.password == form.value.password2 && (form.value.password != "")) {
    return null
  }
  return { message: 'Пароли должны совпадать'}
}