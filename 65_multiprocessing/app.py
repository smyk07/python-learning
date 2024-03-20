# multiprocessing => act of running tasks in parallel on different cpu cores, different from multi-threading which runs one thread at a time
#                    multiproocessing => better for CPU bound tasks, heavy cpu usage
#                    multithreading => better for io bound tasks, waiting around

from multiprocessing import Process, cpu_count
import time 

def counter(num): 
    count = 0
    while count < num: 
        count += 1

def main(): 
    
    # print(cpu_count())
    
    a = Process(target=counter, args=(100000000000/4,))
    b = Process(target=counter, args=(100000000000/4,))
    # c = Process(target=counter, args=(100000000000/4,))
    # d = Process(target=counter, args=(100000000000/4,))
    
    a.start() 
    b.start()
    # c.start()
    # d.start()
    
    a.join() 
    b.join()
    # c.join()
    # d.join()
    
    print("Finished in: ", time.perf_counter(), " seconds.")
 
if __name__ == "__main__": 
    main()