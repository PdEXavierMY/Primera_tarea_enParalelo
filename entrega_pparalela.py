import random #importamos la libreria random para generar numeros aleatorios
from multiprocessing import Pool #importamos la libreria multiprocessing para poder ejecutar procesos en paralelo
from time import sleep #importamos la libreria time para poder usar la funcion sleep(que restrasara la ejecucion del codigo)
from introducir import solicitar_introducir_numero_extremo #importamos la funcion solicitar_introducir_numero_extremo del modulo introducir, que nos permitira pedir al usuario que introduzca un numero entre dos valores

"""urls = ["a.com", "b.com", "c.com", "d.com"] #comenzamos probando a ejecutar el primer ejemplo de codigo provisto

def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

output = []
for url in urls:
    result = scrape(url)
    output.append(result)

#las ejecuciones de los procesos se realizan en orden, por lo que nunca comenzara el proceso 2 hasta que el proceso 1 no haya terminado
"""

"""urls = ["a.com", "b.com", "c.com", "d.com"] #ahora ejecutaremos el codigo con la libreria multiprocessing, para probar la programacion paralela"""

"""urls = ["a.com", "b.com", "c.com", "d.com", "e.com"] #probamos a ejecutar el codigo con 5 procesos

def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

from multiprocessing import Pool

if __name__ == "__main__":

    pool = Pool(processes=4)

    data = pool.map(scrape, urls)

    scrape("a.com") # hecho por el proceso 1 
    scrape("b.com") # hecho por el proceso 2 
    scrape("c.com") # hecho por el proceso 3 
    scrape("d.com") # hecho por proceso 4

    pool.close()
    print()

    for row in data:
        print(row)

#tras los arreglos correspondientes, el codigo funciona correctamente, y se puede observar que los procesos se ejecutan en paralelo, y no en orden

urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]
"""
"""#ahora probaremos a ejecutar el codigo final con 5 procesos

def scrape(url):
    print("starting", url)
    duration = round(random.random(),3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

#urls = ["a.com", "b.com", "c.com", "d.com"]
urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]

if __name__ == "__main__":
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()    
    print()
    for row in data:
        print(row)"""

def scrape(url): #definimos la funcion scrape
    print("starting", url) #imprimimos el mensaje "starting" junto con el valor de la variable url
    duration = round(random.random(),3) #generamos un numero aleatorio entre 0 y 1, con 3 decimales
    sleep(duration) #retrasamos la ejecucion del codigo durante el tiempo que dure el numero aleatorio generado, para una mejor visualizacion
    print("finished", url, "time taken:", duration, "seconds") #imprimimos el mensaje "finished" junto con el valor de la variable url, y el tiempo que ha tardado en ejecutarse
    return url, duration #devolvemos el valor de la variable url y el tiempo que ha tardado en ejecutarse

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