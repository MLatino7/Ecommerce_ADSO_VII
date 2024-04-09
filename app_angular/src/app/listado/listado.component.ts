import { Component } from '@angular/core';
import { ApirestService } from '../servicios/apirest/apirest.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-listado',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './listado.component.html',
  styleUrl: './listado.component.sass'
})
export class ListadoComponent {
  estudios: any[] = []; // Inicializa como arreglo vacío
  productos: any[] = []; // Inicializa como arreglo vacío
  empleados: any[] = []; // Inicializa como arreglo vacío
  nuevoProducto: any = {}; // Nuevo objeto para almacenar los datos del formulario

  constructor(public apirestservice: ApirestService) { }
  
  ngOnInit(): void {
    // this.obtenerEmpleados();
    this.obtenerProductos();

  }
 
  // obtenerEmpleados() {
  //   this.apirestservice.getUsuarios().subscribe((response: any) => {
  //     console.log(response); // Esto te mostrará la estructura exacta de la respuesta
  //     if (response.message === "Success") {
  //       this.empleados = response.empleados; // Asigna el arreglo de empleados a 'estudios'
  //     } else {
  //       console.error("Error en la respuesta de la API:", response.message);
  //     }
  //   }, error => {
  //     console.error("Error al obtener empleados:", error);
  //   });
  // }

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


  
crearProducto() {
  console.log(this.nuevoProducto);
  this.apirestservice.crearProducto(this.nuevoProducto).subscribe((response: any) => {
    
    if (response.message === "Producto creado con éxito") {
      alert("Producto creado exitosamente");
      this.obtenerProductos(); // Actualiza la lista de productos después de la inserción
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

  delete_estudio(id:any)
  {
    this.apirestservice.deleteEstudios(id).subscribe(
    result => {
    alert("Borrado Exitoso");
    // this.obtenerEmpleados();
    }
    );
    // this.obtenerEmpleados();
  }




}
