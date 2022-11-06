import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoSearchComponent } from './co-search.component';

describe('CoSearchComponent', () => {
  let component: CoSearchComponent;
  let fixture: ComponentFixture<CoSearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CoSearchComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CoSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
