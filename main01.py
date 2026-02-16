from services import service01prueba

print("Soy un Main")
texto = service01prueba.getsaludos()
print(texto)

print("Soy una Mascota")
pez = service01prueba.getMascota()
print(f"Nombre: {pez.nombre}, Raza: {pez.raza}")

print("Soy una Mascota2")
leona = service01prueba.getMascota2()
print(f"Nombre: {leona.nombre}, Raza: {leona.raza}")

print("Hagamos una Lista de Mascotas")
milistademascotas = service01prueba.getListaMascotas()
for mascota in milistademascotas:
    print(milistademascotas.nombre)
    print(milistademascotas.raza)
    print(milistademascotas.edad)