import { HttpErrorResponse } from "@angular/common/http"
import { IUser } from "./users.model"

export interface IRegister {
    email: string
    username: string
    password: string
}

export interface IRegisterResp {
    success: boolean
}

export interface ILoginResp {
    user: IUser
    token: string
}
  
export interface IErrors {
    username: boolean,
    password: boolean,
    email: boolean
}

export interface IErrorsLogin {
    username: boolean,
    password: boolean,
}

export interface IRegisterResponse {
    errors: IErrors | null
    resp: IRegisterResp | null
    exception: HttpErrorResponse
}

export interface ILoginResponse {
    errors: IErrors | null
    resp: ILoginResp | null
    exception: number | null
}