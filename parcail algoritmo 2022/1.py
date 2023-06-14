def contar_palabra(palabra, vector):
    if not vector:  # Caso base: el vector está vacío
        return 0
    elif vector[0] == palabra:  # La primera palabra del vector coincide
        return 1 + contar_palabra(palabra, vector[1:])  # Llamada recursiva sin la primera palabra
    else:
        return contar_palabra(palabra, vector[1:])  # Llamada recursiva sin la primera palabra

# Ejemplo de uso
vector_palabras = ["armani", "aliendro", "aliendro", "beltran", "borja", "pirez"]
palabra_buscada = "pirez"
resultado = contar_palabra(palabra_buscada, vector_palabras)
print(f"La palabra '{palabra_buscada}' aparece {resultado} veces en el vector.")
