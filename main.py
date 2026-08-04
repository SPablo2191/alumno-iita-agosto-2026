alumnos = {
    "43168585" : {
        "nombre" : "pablo",
        "apellido": "sandoval",
        "notas" : [1,2,3]
    },
        "23168585" : {
        "nombre" : "Nicolas",
        "apellido": "Martinelli",
        "notas" : [10,9,10]
    }
}

nombre = input("ingrese nombre: ")
apellido = input("ingrese apellido: ")
dni = input("ingrese dni: ")
nro_notas = int(input("ingrese cuantas notas a cargar: "))
notas = []
for i in range(nro_notas):
    notas.append(int(input("ingrese nota obtenida: ")))

nuevo_alumno = {"nombre": nombre, "apellido" : apellido, "notas": notas }


alumnos[dni] = nuevo_alumno

print(alumnos)

