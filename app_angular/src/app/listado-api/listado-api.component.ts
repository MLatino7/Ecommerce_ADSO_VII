import { Component } from '@angular/core';
import { ApirestService } from '../servicios/apirest/apirest.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';



@Component({
  selector: 'app-listado-api',
  standalone: true,
  imports: [ CommonModule, FormsModule],
  templateUrl: './listado-api.component.html',
  // styleUrl: './listado-api.component.scss'
})
export class ListadoApiComponent {
  productos: any[] = []; // Inicializa como arreglo vacío

  constructor(public apirestservice: ApirestService) { }

  ngOnInit(): void {
    // this.obtenerEmpleados();
    this.obtenerProductos();

  }
 
  
  obtenerProductos() {
    this.apirestservice.getProductos().subscribe((responseP: any) => {
      console.log(responseP); // Esto te mostrará la estructura exacta de la respuesta
  
      if (responseP.message === "Success") {
        this.productos = responseP.productos; // Asigna el arreglo de productos a 'productos'
      } else {
        console.error("Error en la respuesta de la API:", responseP.message);
      }
    }, error => {
      console.error("Error al obtener productos:", error);
    });
  }
}