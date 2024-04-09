import { Routes } from '@angular/router';
import { FormularioComponent } from './formulario/formulario.component';
import { ListadoApiComponent } from './listado-api/listado-api.component';
import { AddArticuloComponent } from './add-articulo/add-articulo.component';
import { ListadoComponent } from './listado/listado.component';

export const routes: Routes = [

    { path:'formulario',component:FormularioComponent},
    { path: 'listadoapi',component:ListadoApiComponent},
    { path: 'adicionar',component:AddArticuloComponent},
    { path:'registro',component:ListadoComponent},

];
