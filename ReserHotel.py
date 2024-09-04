reservas_hoteles = []


hotel1 = {
    "nombre": "La sucursal del Cielo",
    "ubicacion": "Cali",
    "disponibilidad": "si",
    "precio": 60,
}

cliente1 = {
    "nombre": "Juan Pérez",
    "direccion": "Calle  123",
    "email": "juan@gmail.com",
    "telefono": "1234567"
}

reservas_hoteles.append({"cliente": cliente1, "hotel": hotel1})
print(f"Reserva de hoteles para {cliente1['nombre']} a {hotel1['ubicacion']} realizada con éxito.")

if hotel1["disponibilidad"] > 0:
    reservas_hoteles.append({"cliente": cliente1, "hotel": hotel1})
    hotel1["disponibilidad"] -= 1
    print(f"Reserva de hotel para {cliente1['nombre']} en {hotel1['nombre']} realizada con éxito.")
else:
    print(f"No hay disponibilidad en el hotel {hotel1['nombre']}.")










