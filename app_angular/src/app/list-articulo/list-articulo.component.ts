import { Component } from '@angular/core';
import { ArticulosService } from '../articulos.service';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-list-articulo',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './list-articulo.component.html',
  styleUrl: './list-articulo.component.sass'
})

export class ListArticuloComponent {
  constructor(public articuloservice: ArticulosService) {
  }
  
}
