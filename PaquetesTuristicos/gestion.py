#Creacion

paquetes_turisticos = []

paquete1 = {
    "destino": "Bogota",
    "duracion": 7,
    "precio": 150,
    "descripcion": "Tour por los mejores lugares de Bogota"
}

paquete2 = {
    "destino": "Cali",
    "duracion": 5,
    "precio": 120,
    "descripcion": "Tour por los mejores lugares de Cali"
}

paquete3 = {
    "destino": "Barranquilla",
    "duracion": 8,
    "precio": 180,
    "descripcion": "Tour por los mejores lugares de Barranquilla"
}

paquete4 = {
    "destino": "Quito",
    "duracion": 3,
    "precio": 150,
    "descripcion": "Tour por los mejores lugares de Quito"
}

paquetes_turisticos.append(paquete1)
paquetes_turisticos.append(paquete2)
paquetes_turisticos.append(paquete3)
paquetes_turisticos.append(paquete4)

print(f"Paquete turístico a {paquete1["destino"]} creado con éxito.")
print(f"Paquete turístico a {paquete2["destino"]} creado con éxito.")
print(f"Paquete turístico a {paquete3["destino"]} creado con éxito.")
print(f"Paquete turístico a {paquete4["destino"]} creado con éxito.")

#Busqueda
destino = "Bogota"
resultados = []

for paquete in paquetes_turisticos:
    if paquete["destino"] == destino:
        resultados.append(paquete)

if resultados:
    print(f"Se encontraron {len(resultados)} paquetes a {destino}:")
    for i in resultados:
        print(f"Destino: {i["destino"]}, Duración: {i["duracion"]} días, Precio: ${i["precio"]}")
else:
    print(f"No se encontraron paquetes a {destino}.")