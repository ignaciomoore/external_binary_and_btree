Hay tres archivos que se forman parte de la tarea, estos 
son BinaryTree2.py, el cual contiene todo lo necesario para
hacer busquedas binarias, BTree.py contiene todo para poder 
crear B-Trees y buscar numeros en B-Trees, por ultimo 
helper.py hace todo lo necesario para probar y analisar el
rendimiento de los algoritmos.

Si uno corre helper.py va a retornar graficos con resultados 
a partir de archivos y numeros aleatorios que crea el 
programa, si quiere probar cada algoritnmo manualmente estan 
las funcion busquedaBinaria(num, fileName, blockSize) de 
BinaryTree2.py que retorna si es que el valor num se 
encuentra en el archivo fileName bucando un blocque de tamaño 
blockSize.

En BTree.py se encuntra la estructura BTree(order), que 
representa un B-Tree de orden igual order en memoria 
interna, esta estructura tiene la funcion insert(payload), 
que inserta el valor payload en el arbol B-Tree. Para pasar 
el arbol a memoria externa esta la funcion write(filename), 
que escribe el arbol en el archivo filename, asi ahora uno 
puede hacer busquedas en el archivo con 
searchBTree(num, fileName), el cual no esta en la estructura
de datos, uno solo escribe el num a buscar dentro del arbol
filename escrito en memoria externa. 