#comenzamos probando a ejecutar el primer ejemplo de codigo provisto
from multiprocessing import Pool
from time import sleep
import random

urls = ["a.com", "b.com", "c.com", "d.com"]
"""
import random
from time import sleep
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
#ahora ejecutaremos el codigo con la libreria multiprocessing, para probar la programacion paralela

def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

from multiprocessing import Pool

pool = Pool(processes=4)

data = pool.map(scrape, urls)

# scrape("a.com") # hecho por el proceso 1 
# scrape("b.com") # hecho por el proceso 2 
# scrape("c.com") # hecho por el proceso 3 
# scrape("d.com") # hecho por proceso 4

pool.close()
print()

for row in data:
    print(row)
"""
urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]


def scrape(url):
    print("starting", url)
    duration = round(random.random(),3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

urls = ["a.com", "b.com", "c.com", "d.com"]

if __name__ == "__main__":
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()    
    print()
    for row in data:
        print(row)"""