nombre = raw_input ("Nombre: ")
apellido = raw_input ("Apellido: ")
direccion = raw_input ("Direccion: ")
telefono_uno = raw_input ("Escribe tu numero telefonico: ")
telefono_dos = raw_input ("Escribe otro numero telefononico: ")
telefonos = int(telefono_uno) + int(telefono_dos)
duplicar = telefonos + telefonos

formulario = nombre + "/" + apellido + "/"+ direccion + "/" + str(telefonos) + "/" + str(duplicar)
print formulario
