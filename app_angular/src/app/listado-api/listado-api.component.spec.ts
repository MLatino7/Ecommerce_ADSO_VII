import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListadoApiComponent } from './listado-api.component';

describe('ListadoApiComponent', () => {
  let component: ListadoApiComponent;
  let fixture: ComponentFixture<ListadoApiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListadoApiComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ListadoApiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
