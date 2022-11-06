import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CoNavbarComponent } from './components/co-navbar/co-navbar.component';
import { HomeComponent } from './components/home/home.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CoSearchComponent } from './components/co-search/co-search.component';
import { CoCardComponent } from './components/co-card/co-card.component';
import { LoginComponent } from './components/login/login.component';
import { RegistrationComponent } from './components/registration/registration.component';
import { HttpClientModule } from '@angular/common/http';
import { AuthService } from './services/auth.service';
import { CabinetComponent } from './components/cabinet/cabinet.component';
import { CoFormComponent } from './components/co-form/co-form.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatFormFieldModule } from '@angular/material/form-field';
import { CoDateComponent } from './co-date/co-date.component';
import { MatInputModule } from '@angular/material/input';
import { MatNativeDateModule } from '@angular/material/core'
import { MatAutocompleteModule } from '@angular/material/autocomplete'
import { MatRadioModule } from '@angular/material/radio';
import { CoProfileComponent } from './components/co-profile/co-profile.component'

@NgModule({
  declarations: [
    AppComponent,
    CoNavbarComponent,
    CoSearchComponent,
    HomeComponent,
    CoCardComponent,
    LoginComponent,
    RegistrationComponent,
    CabinetComponent,
    CoFormComponent,
    CoDateComponent,
    CoProfileComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatInputModule,
    MatFormFieldModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatAutocompleteModule,
    MatRadioModule
  ],
  providers: [AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
