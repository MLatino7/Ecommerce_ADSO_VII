import { Component } from '@angular/core';
import { FormularioComponent } from './formulario/formulario.component';
import { AddArticuloComponent } from './add-articulo/add-articulo.component';
import { ListArticuloComponent } from './list-articulo/list-articulo.component';
import { ListadoComponent } from './listado/listado.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterOutlet } from '@angular/router';
import { ListadoApiComponent } from './listado-api/listado-api.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ListadoComponent,HttpClientModule,FormularioComponent,RouterOutlet,ListArticuloComponent,AddArticuloComponent,FormsModule,ListadoApiComponent ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.sass'
})
export class AppComponent {
  title = 'app_angular';
}
