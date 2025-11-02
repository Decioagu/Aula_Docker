from time import sleep
# the program will print hello world
#  every 1 second foever
x=0
while True:
    x=+1 + x
    print("Ola, Mundo")
    sleep(1)
    if x == 3:
        break  
print("Fim")