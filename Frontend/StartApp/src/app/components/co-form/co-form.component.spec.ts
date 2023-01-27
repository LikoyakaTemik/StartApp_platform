import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoFormComponent } from './co-form.component';

describe('CoFormComponent', () => {
  let component: CoFormComponent;
  let fixture: ComponentFixture<CoFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CoFormComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CoFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
