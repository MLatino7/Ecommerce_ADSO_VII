import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ArticulosService {

  
  articulos:string[]=["a","b"];
  
  add(articulo:string)
  {
    this.articulos.push(articulo);
  }

 
    
}
