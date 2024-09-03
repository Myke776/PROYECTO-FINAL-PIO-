#Resevadelvuelo
class ReservaVuelo:
    def __init__(self, id_reserva, nombre_pasajero, origen, destino, fecha_vuelo):
        self.id_reserva = id_reserva
        self.nombre_pasajero = nombre_pasajero
        self.origen = origen
        self.destino = destino
        self.fecha_vuelo = fecha_vuelo

class AgenciaViajes:
    nombre_pasajero=input("Ingrese su nombre de usuario: ")
    origen= input("Ciudad de origen: ")
    destino= input("Ciudad de destino: ")
    fecha_vuelo= input("Fecha de vuelo:DD/MM/AA ")
    siguiente_id= fecha_vuelo 
#No he logrado hacer que pase de aqui si alguno me puede ayudar lo agradezco 


    def crear_reserva(self, nombre_pasajero, origen, destino, fecha_vuelo):
        reserva = ReservaVuelo(self.siguiente_id, nombre_pasajero, origen, destino, fecha_vuelo)
        self.siguiente_id += 1
        print(f"Reserva creada exitosamente. ID de la reserva: {reserva.id_reserva}")

def listar_reservas(self):
        if not self.reservas:
            print("No hay reservas disponibles.")
        else:
            for reserva in self.reservas:
                print(f"ID: {reserva.id_reserva}, Pasajero: {reserva.nombre_pasajero}, Origen: {reserva.origen}, Destino: {reserva.destino}, Fecha: {reserva.fecha_vuelo}")

def cancelar_reserva(self, id_reserva):
        for reserva in self.reservas:
            if reserva.id_reserva == id_reserva:
                self.reservas.remove(reserva)
                print(f"Reserva con ID {id_reserva} cancelada exitosamente.")
                return
        print(f"No se encontró una reserva con ID {id_reserva}.")


