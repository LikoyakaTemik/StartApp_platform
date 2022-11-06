import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders, HttpParams, HttpRequest, HttpResponse } from '@angular/common/http'
import { Observable, of, throwError } from 'rxjs';
import { catchError, last, map, retry, tap } from 'rxjs/operators';
import { ILogin } from '../models/login.model';
import { IErrors, ILoginResp, ILoginResponse, IRegister, IRegisterResponse } from '../models/register.model';
import { BACKEND_URL } from '../../environments/environment';
import { IUser } from '../models/users.model';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  is_authenticated = false
  errors: IErrors = {
    username: false,
    password: false,
    email: false
  }

  user: IUser | null = null

  constructor(private http: HttpClient) { }

  login(data: ILogin) {
    return this.http.post<ILoginResponse | ILoginResp>(BACKEND_URL + '/api/get2', data, {responseType: 'json', observe: 'body'}).pipe(
      catchError(this.errorHandler(data))
    )
  }

  setUser (user: IUser) {
    this.user = user
    localStorage.setItem('user', JSON.stringify(user))
  }

  getUser () {
    if (this.user == null) {
      let user = localStorage.getItem('user')
      if (user != null) {
        return JSON.parse(user)
      }
    }
    return this.user
  }

  register(data: IRegister) {
    return this.http.post<IRegisterResponse>(BACKEND_URL + '/api/get3', data, {responseType: 'json', observe: 'body'}).pipe(
      catchError(this.errorHandler(data))
    )
  }

  errorHandler(error: any) {
    return (error: HttpErrorResponse) => {
      if (error.error['username']) {
        this.errors.username = true
      }
      else {
        this.errors.username = false
      }
      if (error.error['password']) {
        this.errors.password = true
      }
      else {
        this.errors.password = false
      }
      if (error.error['email']) {
        this.errors.email = true
      }
      else {
        this.errors.email = false
      }
      const r = {errors: this.errors, resp: null, exception: error.status}
      return of(r)
    }
  }
}
