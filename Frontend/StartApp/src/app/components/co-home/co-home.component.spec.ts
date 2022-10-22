import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoHomeComponent } from './co-home.component';

describe('CoHomeComponent', () => {
  let component: CoHomeComponent;
  let fixture: ComponentFixture<CoHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CoHomeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CoHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
