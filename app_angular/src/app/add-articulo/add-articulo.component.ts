import { Component } from '@angular/core';
import { ApirestService } from '../servicios/apirest/apirest.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-add-articulo',
  standalone: true,
  imports: [FormsModule,CommonModule],
  templateUrl: './add-articulo.component.html',
  styleUrl: './add-articulo.component.sass'
})
export class AddArticuloComponent {
  estudios: any[] = []; // Inicializa como arreglo vacío
  productos: any[] = []; // Inicializa como arreglo vacío
  empleados: any[] = []; // Inicializa como arreglo vacío
  nuevoProducto: any = {}; // Nuevo objeto para almacenar los datos del formulario
  constructor(public apirestservice: ApirestService) { }

  
 

  articulo:string='';
  

  crearProducto() {
    console.log(this.nuevoProducto);
    this.apirestservice.crearProducto(this.nuevoProducto).subscribe((response: any) => {
      
      if (response.message === "Producto creado con éxito") {
        alert("Producto creado exitosamente");
        // this.obtenerProductos(); // Actualiza la lista de productos después de la inserción
        this.nuevoProducto = {}; // Limpia los datos del formulario después de la inserción
        
      } else {
        console.error("Error en la respuesta de la API:", response.message);
      }
    }, error => {
      console.error("Error al crear producto:", error);
      // Imprimir el objeto error completo para obtener más detalles
      console.error(error);
    });
  }

  
  
}
