#README
Este código fue realizado en python 3.7 con su pip correspondiente. 
##Librerías Básicas
Las librerías usadas en este código fueron instaladas con pip
- networkx([referencia](https://networkx.github.io/documentation/stable/install.html)): 
~~~
pip install networkx
~~~
- matplotlib([referencia](https://matplotlib.org/users/installing.html)
~~~
python -m pip install -U matplotlib
~~~
##Uso del código
Las coordenadas pueden ser definidas en la lineas 194 y 195:
~~~
- Start: Sx, Sy = 12,7
- Goal: Gx, Gy = 15,15
~~~ 
El programa automaticamente correra ambos algoritmos y el resultado saldra en "Result.pdf" archivo al mismo nivel de donde se corrio.
- El **algoritmo A*** tendra un camino de color **verde**
- El **algoritmo Busqueda Ciega(por Profundidad)** tendra un camino de color **rojo**
***
![demostracion](https://github.com/TLJuan/CS_2020_1/blob/master/lab_busquedas/Demostration.png)