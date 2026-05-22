def calcularpromediodeedad():
        cantidad_salones =int(input("Digite la cantidad de salones: "))
        suma_edades=0
        for i in range(1,cantidad_salones+1):
            cantidad_alumnos=int(input(f"Digite la cantidad de alumnos del salon {i}: "))
            for j in range(1,cantidad_alumnos+1):
                edad= float(input("digite la edad del alumno"))
                suma_edades=suma_edades+edad

        promedioedad=suma_edades/cantidad_alumnos
        print(f"El promedio de edades es: {promedioedad}")
        
calcularpromediodeedad()