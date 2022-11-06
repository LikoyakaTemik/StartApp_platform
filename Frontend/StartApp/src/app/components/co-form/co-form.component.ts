import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, AbstractControl, Validators } from '@angular/forms';


const date = new Date()
const right_expirated = date.toISOString().split("T")[0]
date.setFullYear(date.getFullYear() - 18)
const right = date.toISOString().split("T")[0]
date.setFullYear(date.getFullYear() - 82)
const left = date.toISOString().split("T")[0]

@Component({
  selector: 'app-co-form',
  templateUrl: './co-form.component.html',
  styleUrls: ['./co-form.component.scss']
})
export class CoFormComponent implements OnInit {
  ankete!: FormGroup
  submit: boolean = false

  constructor() { }

  ngOnInit(): void {
    this.ankete = new FormGroup({
      name: new FormControl(null, [Validators.required]),
      surname: new FormControl(null, [Validators.required]),
      patronymic: new FormControl(null, [Validators.required]),
      date_borned: new FormControl(new Date(), [this.date_borned_validator, Validators.required]),
      country: new FormControl(null, [Validators.required]),
      city: new FormControl(null, [Validators.required]),
      citizenship: new FormControl(null, [Validators.required]),
      male: new FormControl("0", [Validators.required]),
      university: new FormControl(null, [Validators.required]),
      speciality: new FormControl(null, [Validators.required]),
      date_expirated: new FormControl(new Date(), [this.date_expirated_validator, Validators.required]),
      email: new FormControl(null, [Validators.email, Validators.required]),
      employment: new FormControl("0", [Validators.required]),
      achievements: new FormControl(null, [Validators.required]),
      work_experience: new FormControl(0, [Validators.required, Validators.min(0), Validators.max(60)]),
      skills: new FormControl(null, [Validators.required]),
      is_have_team: new FormControl("0", [Validators.required]),
      role: new FormControl(null, [Validators.required]),
      inn: new FormControl(null, [Validators.required]),
      phone: new FormControl(null, [Validators.required, this.phone_validator])
    })

    console.log(right, left)
    document.getElementById('date_borned')?.setAttribute('max', right)
    document.getElementById('date_borned')?.setAttribute('min', left)
    document.getElementById('date_expirated')?.setAttribute('max', right_expirated)
    document.getElementById('date_expirated')?.setAttribute('min', left)
  }

  date_borned_validator(form: AbstractControl){
    const value = form.value
    const date_parsed = Date.parse(value)
    const date_max = Date.parse(right)
    const date_min = Date.parse(left)
    if (date_parsed > date_max) {
      return {'message': 'Недопустимое значение'}
    } else
    if (date_parsed < date_min) {
      return {'message': 'Недопустимое значение'}
    }
    return null
  }

  date_expirated_validator(form: AbstractControl){
    const value = form.value
    const date_parsed = Date.parse(value)
    const date_max = Date.parse(right_expirated)
    const date_min = Date.parse(left)
    if (date_parsed > date_max) {
      return {'message': 'Недопустимое значение'}
    } else
    if (date_parsed < date_min) {
      return {'message': 'Недопустимое значение'}
    }
    return null
  }
  
  phone_validator(form: AbstractControl){
    const value = form.value
    if (value?.match("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$") >= 1 && value.length == 10) {
      return null
    } else {
      return {'phone': "Неверный формат телефона"}
    }
  }

  on_submit() {
    this.submit = true
    console.log(this.ankete)
  }

}
