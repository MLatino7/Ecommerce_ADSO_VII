import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListArticuloComponent } from './list-articulo.component';

describe('ListArticuloComponent', () => {
  let component: ListArticuloComponent;
  let fixture: ComponentFixture<ListArticuloComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListArticuloComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ListArticuloComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
