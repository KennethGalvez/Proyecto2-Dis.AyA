# Proyecto2-Dis.AyA

# Programacion Dinamica
El algoritmo de programacion dinamica utiliza una matriz dp para almacenar los resultados de los subproblemas. 
Primero, se llena la matriz dp calculando las longitudes de las subsecuencias comunes más largas entre todas las combinaciones posibles de prefijos de secuencia1 y secuencia2.
Luego, se reconstruye la subsecuencia común más larga obteniendo los elementos correspondientes a partir de la matriz dp.
La complejidad de este algoritmo es O(m x n), donde m y n son las longitudes de las secuencias respectivas.

# Enfoque Greedy
El algoritmo de enfoque greedy consiste en iterar sobre los elementos de secuencia1 y agregar aquellos elementos que también están presentes en secuencia2 a la subsecuencia común más larga LCS.
La complejidad de este algoritmo es O(m x n), donde m y n son las longitudes de las secuencias respectivas, ya que es necesario verificar si cada elemento de secuencia1 está presente en secuencia2.


