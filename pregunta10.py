def convertir_fecha(input_fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    partes = input_fecha.split("/")

 
    if len(partes) == 3:
        mes, dia, anio = partes
    else:
       
        for i, nombre_mes in enumerate(meses, start=1):
            input_fecha = input_fecha.replace(nombre_mes, str(i))
        mes, dia, anio = input_fecha.split()

    
    fecha_formateada = f"{anio.zfill(4)}-{mes.zfill(2)}-{dia.zfill(2)}"
    return fecha_formateada


entrada_usuario = input("Ingresa una fecha (mes-día-año o Mes día, año): ")


resultado = convertir_fecha(entrada_usuario)
print("Resultado:", resultado)