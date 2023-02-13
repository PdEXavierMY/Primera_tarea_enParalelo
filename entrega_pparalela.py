import random #importamos la libreria random para generar numeros aleatorios
from multiprocessing import Pool #importamos la libreria multiprocessing para poder ejecutar procesos en paralelo
from time import sleep #importamos la libreria time para poder usar la funcion sleep(que restrasara la ejecucion del codigo)

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

def scrape(url):
    print("starting", url)
    duration = round(random.random(),3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

def ejecutar_practica():
    forma_de_ejecucion = input("¿Como desea ejecutar la practica? (1)Secuencialmente (2)Paralelamente: ")
    if forma_de_ejecucion == "1":
        urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]
        output = []
        for url in urls:
            result = scrape(url)
            output.append(result)
    elif forma_de_ejecucion == "2":
        urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]
        if __name__ == "__main__":
            pool = Pool(processes=4)
            data = pool.map(scrape, urls)
            pool.close()    
            print()
            for row in data:
                print(row)
    else:
        print("Opcion no valida")
        ejecutar_practica()