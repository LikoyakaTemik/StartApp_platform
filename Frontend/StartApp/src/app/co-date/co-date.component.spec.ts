import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoDateComponent } from './co-date.component';

describe('CoDateComponent', () => {
  let component: CoDateComponent;
  let fixture: ComponentFixture<CoDateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CoDateComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CoDateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
