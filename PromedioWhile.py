def calcularpromediodeedad():
    cantidad_salones = int(input("Digite la cantidad de salones: "))
    
    suma_edades = 0
    total_alumnos = 0
    
    i = 1
    
    while i <= cantidad_salones:
        cantidad_alumnos = int(input(f"Digite la cantidad de alumnos del salón {i}: "))
        
        j = 1
        
        while j <= cantidad_alumnos:
            edad = float(input("Digite la edad del alumno: "))
            
            suma_edades = suma_edades + edad
            total_alumnos = total_alumnos + 1
            
            j = j + 1
        
        i = i + 1
    
    promedioedad = suma_edades / total_alumnos
    
    print(f"El promedio de edades es: {promedioedad}")

calcularpromediodeedad()