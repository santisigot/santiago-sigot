class BitacoraNave:
    def __init__(self):
        self.pila = []

    def agregar_mision(self, planeta, capturado, recompensa):
        self.pila.append((planeta, capturado, recompensa))

    def mostrar_planetas_visitados(self):
        planetas_visitados = [mision[0] for mision in self.pila]
        return planetas_visitados

    def calcular_recaudacion_total(self):
        recaudacion_total = sum(mision[2] for mision in self.pila)
        return recaudacion_total

    def buscar_mision_han_solo(self):
        for i, mision in enumerate(self.pila):
            if mision[1] == "Han Solo":
                return i+1, mision[0]
        return None, None

# Crear una instancia de la bitácora
bitacora = BitacoraNave()

# Agregar misiones a la bitácora
bitacora.agregar_mision("bespin", "Jabba the Hutt", 1000)
bitacora.agregar_mision("endor", "Greedo", 800)
bitacora.agregar_mision("naboo", "Lando Calrissian", 8800)
bitacora.agregar_mision("endor", "Han Solo", 1700)

# Mostrar los planetas visitados en el orden de las misiones
planetas = bitacora.mostrar_planetas_visitados()
print("Planetas visitados:", planetas)

# Calcular la recaudación total
recaudacion_total = bitacora.calcular_recaudacion_total()
print("Recaudación total:", recaudacion_total)

# Buscar la misión en la que capturó a Han Solo
num_mision, planeta = bitacora.buscar_mision_han_solo()
if num_mision is not None:
    print("han solo fue caturado en la mision", num_mision, "en el planeta", planeta)
else:
    print("No se encontró información sobre la captura de Han Solo.")