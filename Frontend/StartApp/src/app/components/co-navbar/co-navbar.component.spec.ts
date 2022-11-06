import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoNavbarComponent } from './co-navbar.component';

describe('CoNavbaComponent', () => {
  let component: CoNavbarComponent;
  let fixture: ComponentFixture<CoNavbarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CoNavbarComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CoNavbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
