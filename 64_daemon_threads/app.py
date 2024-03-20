# daemon thread - a thread that runs in the background, not important for program, and the program will not wait for the daemon threads to complete before exiting
#                 non-daemon threads cannot be normally killed, and stay alive until the porgram is complete 
#                 ex. background tasks, garbage collection, waiting for input, long running processes, etc. 

import threading 
import time 

def timer(): 
    print()
    print()
    count = 0
    while True: 
        time.sleep(1)
        count += 1 
        print("Logged in for: " + str(count) + " seconds")

# non-daemon thread
# x = threading.Thread(target=timer) 
# x.start()

# daemon thread
x = threading.Thread(target=timer, daemon=True) 
# x.setDaemon(True) # alternative to set daemon thread 
x.start()

answer = input("Do you wish to exit?")