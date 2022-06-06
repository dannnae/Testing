usuarios = []
validacion_rut = True
validacion_correo = True
validacion_edad = True
validacion_genero = True
validacion_tipo = True
continuar = True
opcion = 0

while continuar:
    print(' 1. Registrar cliente \n 2. Suscripcion \n 3. Consultar base de datos \n 4. Salir')
    try:
        opcion = int(input('Ingrese una de las opciones anteriores: '))
    except ValueError:
        print('Ingresaste una letra!, intentelo nuevamente')
    if opcion == 1:
        datos_usuario = []
        while validacion_rut:
            rut = int(input('Ingrese su rut: '))
            if rut > 4000000 and rut < 99999999:
                datos_usuario.append(rut)
                validacion_rut = False
            else:
                print('rut no valido')

        nombre = str(input('Ingrese su nombre: '))
        direccion = str(input('Ingres su direccion: '))
        comuna = str(input('Ingrese su comuna: '))
        datos_usuario.append(nombre)
        datos_usuario.append(direccion)
        datos_usuario.append(comuna)

        while validacion_correo:
            correo = str(input('Ingrese su correo: '))
            if '@' in correo:
                index = correo.find('@')
                if index != 0 and index != len(correo) - 1:
                    datos_usuario.append(correo)
                    validacion_correo = False
                else:
                    print('Correo no valido')
                    
            else:
                print('Correo no valido')

        while validacion_edad: 
            edad = int(input('Ingrese su edad: '))
            if edad > 0 and edad < 111:
                datos_usuario.append(edad)
                validacion_edad = False
            else:
                print('Edad no valida')

        while validacion_genero: 
            genero = str(input('Ingrese su genero femenino o masculino (F/M): '))
            if genero == 'F':
                datos_usuario.append('Femenino')
                validacion_genero = False
            elif genero == 'M':
                datos_usuario.append('Masculino')
                validacion_genero = False
            else:
                print('No valido')
            
        celular = int(input('Ingrese su celular: '))
        datos_usuario.append(celular)

        while validacion_tipo: 
            tipo = str(input('Ingrese el tipo de suscripcion (PREMIUM / GOLD / SILVER)): '))
            if tipo == 'PREMIUM' or tipo == 'GOLD' or tipo == 'SILVER':
                datos_usuario.append(tipo)
                validacion_tipo = False
            else:
                print('Suscripcion no valida')

        usuarios.append(datos_usuario)
   
    #SUSCRIPCION
    elif opcion == 2:
        rut = int(input('Ingrese su rut: '))
        usuario_registrado = False
        for usuario in usuarios:
            if rut in usuario:
                usuario_registrado = True
                fecha = input('Ingrese la fecha: ')
                usuario.append(fecha)

        if not usuario_registrado:
            print('Usted no está registrado')
            

    elif opcion == 3:
        rut = int(input('Ingrese su rut: '))
        usuario_registrado = False
        for usuario in usuarios:
            if rut in usuario:
                print(usuario)
                usuario_registrado = True

        if not usuario_registrado:
            print('Usted no está registrado')

    elif opcion == 4:
        print('Gracias por suscribirse a la App de Juan Maestro')
        continuar = False


