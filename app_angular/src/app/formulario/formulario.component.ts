import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router'; // Importa RouterModule

@Component({
  selector: 'app-formulario',
  standalone: true, // Esta es la única instancia necesaria de la propiedad standalone
  imports: [CommonModule, FormsModule,RouterModule],
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.sass']
})
export class FormularioComponent {
  nombre: string = '';
  apellido: string = '';
  registrado: boolean = false;
  mensaje: string = 'Usuario registrado exitosamente';

  registrar_usuario() {
    this.registrado = true;
    // Aquí puedes agregar lógica adicional para el registro del usuario, como llamadas a servicios.
  }
}