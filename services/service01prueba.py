
from models import mascota

def getsaludos():
        return "Hoy es juernes"

def getMascota():
    dato = mascota.Mascota()
    dato.nombre = "Flounder"
    dato.raza   = "Pez"
    dato.edad   = 22
    return dato

def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Nala"
    dato.raza   = "Leona"
    dato.edad   = 18
    return dato

def getListaMascotas():
    listaMascotas = []
    listaMascotas.append(getMascota())
    listaMascotas.append(getMascota2())
    perro = mascota.Mascota()
    perro.nombre = "Schatzi"
    perro.raza   = "Rodweiller"
    perro.edad   = 5
    return listaMascotas

