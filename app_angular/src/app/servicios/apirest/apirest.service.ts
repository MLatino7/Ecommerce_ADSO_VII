import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

  @Injectable({
  providedIn: 'root'
  })
  export class ApirestService {
    constructor(private http: HttpClient) { }

    // getUsuarios() {
    //   return this.http.get('http://127.0.0.1:8000/api/empleados/');
    // }

     
    getProductos() {
      return this.http.get('http://127.0.0.1:8000/api/productos/');
    }

    crearProducto(nuevoProducto: any) {
      return this.http.post('http://127.0.0.1:8000/api/productos/', nuevoProducto);
    }
    
    deleteEstudios(id:any) {
       return this.http.delete('http://localhost:8000/api_drf/v1/estudios/'+id+"/");
    }
  }
