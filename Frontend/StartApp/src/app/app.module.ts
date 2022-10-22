import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CoNavbarComponent } from './components/co-navbar/co-navbar.component';
import { CoHomeComponent } from './components/co-home/co-home.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CoSearchComponent } from './components/co-search/co-search.component';
import { CoCardComponent } from './components/co-card/co-card.component';

@NgModule({
  declarations: [
    AppComponent,
    CoNavbarComponent,
    CoHomeComponent,
    CoSearchComponent,
    CoCardComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
