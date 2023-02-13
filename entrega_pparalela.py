#comenzamos probando a ejecutar el primer ejemplo de codigo provisto

urls = ["a.com", "b.com", "c.com", "d.com"]

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

#from multiprocessing import Pool

# pool = Pool(processes=4)

# data = pool.map(scrape, urls)

# scrape ("a.com") # hecho por el proceso 1 
# scrape ("b.com") # hecho por el proceso 2 
# scrape ("c.com") # hecho por el proceso 3 
# scrape ("d.com") # hecho por proceso 4

# pool.close()
# print()
# for row in data:
#     print(row)

# urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]

# from multiprocessing import Pool
# from time import sleep
# import random
# def scrape(url):
#     print("starting", url)
#     duration = round(random.random(),3)
#     sleep(duration)
#     print("finished", url, "time taken:", duration, "seconds")
#     return url, duration
# urls = ["a.com", "b.com", "c.com", "d.com"]
# if __name__ == "__main__":
#     pool = Pool(processes=4)
#     data = pool.map(scrape, urls)
#     pool.close()    
#     print()
#     for row in data:
#         print(row)