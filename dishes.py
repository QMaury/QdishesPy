import random
import time

# dishList = ['inSink', 'outSink', 'inMach', 'outMach']

inSink = random.randint(0, 1)       # picks a random bool integer
inMach = random.randint(0, 1)
machClean = random.randint(0, 1)

print(int(inSink))          # displays the boolean values declared above. mostly just here for testing
print(int(inMach))
print(int(machClean))
print('\n')

while inSink == 0:         # if no dishes in sink, print good job
    print("The sink is empty.\nGood job.")
    quit()
while inSink == 1:         # if there are dishes in sink, finds out wether or not the machine is full or not 
    print("The sink needs to be emptied")
    if inMach == 0:
        print("The machine should be filled and turned on") #if there arent dishes in the sink 
        inMach = 1
        inSink = 0
    if inMach == 1:
        if machClean == 0:
            print("Turn on the machine")
            if inSink == 1:
                print("Wait for the machine to finish running")
                time.sleep(2)
                machClean = 1
                print("Empty the machine")
                inMach = 0
                time.sleep(1)
                if inMach == 0:
                    print("Load the machine")
                    inSink = 0
                    time.sleep(1)
        if machClean == 1:
            print("Empty the machine")
            time.sleep(1)
            inMach = 0 
            if inMach == 0:
                print("Load the machine")
                time.sleep(1)
                inMach = 1
                sinkEmpty = 0 
    if inSink == 0:
        print("The sink is empty.\nGood job.")
    quit()
