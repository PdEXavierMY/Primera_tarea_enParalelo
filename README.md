# Primera_tarea_enParalelo

En esta entrega aprendemos el valor de la programación concurrente. El código que se ha utilizado tiene una parte que se ejecuta en paralelo y otra que lo hace en secuencia. En este ejemplo concreto, podemos ver la gran diferencia que hay entre el tiempo que tarda el programa en ejecutarse de manera secuncial y el tiempo que tarda en ejecutarse de forma paralela.

El código provisto y analizado es el siguiente:

```python
def scrape(url): #definimos la funcion scrape
    print("starting", url) #imprimimos el mensaje "starting" junto con el valor de la variable url
    duration = round(random.random(),3) #generamos un numero aleatorio entre 0 y 1, con 3 decimales
    sleep(duration) #retrasamos la ejecucion del codigo durante el tiempo que dure el numero aleatorio generado, para una mejor visualizacion
    print("finished", url, "time taken:", duration, "seconds") #imprimimos el mensaje "finished" junto con el valor de la variable url, y el tiempo que ha tardado en ejecutarse
    return url, duration #devolvemos el valor de la variable url y el tiempo que ha tardado en ejecutarse


@mide_tiempo #decoramos la funcion scrape con la funcion mide_tiempo
def ejecutar_practica(): #definimos la funcion ejecutar_practica, que servira como lanzador del codigo
    urls = ["a.com", "b.com", "c.com", "d.com", "e.com"] #creamos una lista con 5 urls
    forma_de_ejecucion = solicitar_introducir_numero_extremo("¿Como desea ejecutar la practica? (1)Secuencialmente (2)Paralelamente", 1, 2) #pedimos al usuario que introduzca la opcion que desea ejecutar
    if forma_de_ejecucion == 1:
        output = []
        for url in urls: #recorremos la lista urls
            print(url)
            result = scrape(url)
            output.append(result) #añadimos el resultado de la ejecucion de la funcion scrape a la lista output
            #ejecutamos el codigo secuencialmente
    elif forma_de_ejecucion == 2:
        if __name__ != "__main__": #si el archivo se ejecuta directamente, se ejecutara la funcion ejecutar_practica
            pool = Pool(processes=4) #creamos un pool de procesos con 4 procesos
            data = pool.map(scrape, urls) #ejecutamos la funcion scrape en paralelo
            pool.close() #cerramos el pool de procesos
            print()
            for row in data:
                print(row)
            #ejecutamos el codigo en paralelo
            
```

Este script se basa en una función que controla la manera de ejecutar nuestro código prueba (secuencial o paralelo). Como se puede observar, la función ejecutora viene acompañada de una decoradora, que en este caso se encarga de medir el tiempo de ejecución para poder comparar que estilo de programación es más beneficioso para nuestro archivo python.

La función mide_tiempo desarrollada es la siguiente:

```python
def mide_tiempo(funcion): #definimos la funcion mide_tiempo, que servira para medir el tiempo de ejecucion de una funcion
    def wrapper(*args, **kwargs): #definimos la funcion wrapper, que servira como envoltorio de la funcion que queremos medir
        import time #importamos la libreria time para poder usar la funcion time.time()
        start = time.time() #guardamos el tiempo actual en la variable start
        result = funcion(*args, **kwargs) #ejecutamos la funcion que queremos medir
        end = time.time() #guardamos el tiempo actual en la variable end
        print("Tiempo de ejecucion:", end - start, "segundos") #imprimimos el tiempo que ha tardado en ejecutarse la funcion
        return result #devolvemos el resultado de la ejecucion de la funcion
    return wrapper #devolvemos la funcion wrapper
    
```

Con todas estas herramientas a nuestra disposición pasamos a analizar distintas muestras de salida por terminal de cada tipo de ejecución:

<h4>Ejecución secuencial</h4>

![C1](https://user-images.githubusercontent.com/91721699/220148299-df41e9de-26c0-410d-8b88-9310ee6f52af.png)

![C2](https://user-images.githubusercontent.com/91721699/220148314-358fd2d9-4478-47b4-ab39-9167e66a9edc.png)

![C3](https://user-images.githubusercontent.com/91721699/220148348-3420d6d3-b362-4f16-82f2-1bbf978dd8fe.png)

<h4>Ejecución paralela</h4>

![C4](https://user-images.githubusercontent.com/91721699/220148364-c8e83470-277c-44b7-ab9b-481b4d31975b.png)

![C5](https://user-images.githubusercontent.com/91721699/220148380-d6b853ef-8c3f-4172-9772-28e2691e4b76.png)

![C6](https://user-images.githubusercontent.com/91721699/220148397-655a14e5-bf15-40da-9127-f357886857b2.png)

Es bastante obvio simplemente fijándonos en las medias de cada tipo de programación, que el mejor método que podemos utilizar para poder optimizar al máximo nuestro tiempo y el del programa es la ejecución paralela.

<h5>Media de tiempo de ejecución en secuencia: 3.9538</h5>

<h5>Media de tiempo de ejecución en paralelo: 1.6177</h5>
