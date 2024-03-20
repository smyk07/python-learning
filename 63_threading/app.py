# a thread is a flow of execution of the program, like seperate order of instructions
# can run turn-by-turn in concurrency not parallel, because the GIL (global interpreter lock) allows only one thread to hold control of the python interpreter at a time. 

# CPU BOUND PROGRAM = program / task that spends most of its time waiting for internal events (CPU Intensive)
#                     use multi-processing 

# IO BOUND PROGRAM = program / task which spends most of its time waiting for external events (user input, web scraping)
#                    use multi-threading 

import threading 
import time 

print()

def eat_breakfast(): # IO BOUND TASK 
    time.sleep(3) 
    print("Breakfast eaten")

def drink_coffee(): # IO BOUND TASK
    time.sleep(4)
    print("Coffee Drank")

def study(): # IO BOUND TASK
    time.sleep(6) 
    print("Studying finished")

# creting new threads to run functions parallelly
x = threading.Thread(target=eat_breakfast, args=())
y = threading.Thread(target=drink_coffee, args=())
z = threading.Thread(target=study, args=()) 

# starting the threads
x.start()
y.start()
z.start()

# threads joined and syncronised
x.join() 
y.join()
z.join()

# running functions sequentially on the main thread
# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count()) # prints the number of threads running - one thread known as main thread
print(threading.enumerate()) # prints list of all threads running
print(time.perf_counter()) # time taken by main thread to comlete task

print() 