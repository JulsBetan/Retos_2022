# /*
#  * Reto #27
#  * VECTORES ORTOGONALES
#  * Fecha publicación enunciado: 07/07/22
#  * Fecha publicación resolución: 11/07/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea un programa que determine si dos vectores son ortogonales.
#  * - Los dos array deben tener la misma longitud.
#  * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
#  */

def punto(vec1, vec2):
    return (vec1[0]*vec2[0] + vec1[1]*vec2[1]) == 0
        
print ("Los vectores son", "ortogonales" if punto([1,-2],[2,1]) else "No ortogonales") 

print ("Los vectores son", "ortogonales" if punto([1,-3],[3,2]) else "No ortogonales") 