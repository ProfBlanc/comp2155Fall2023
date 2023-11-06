

def countdown(name, number):
    print("Starting countdown named", name)
    for n in range(number, 0, -1):
        print(f"{name}-{n}")
    print("Ending countdown named", name)

countdown("first", 10)
countdown("second", 10)

import threading
print("*" * 20)

t1 = threading.Thread(target=countdown,
                      args=("first", 10))
t2 = threading.Thread(target=countdown,
                      args=("second", 10))

t1.start()


t2.start()

print("I'm going to get a cup of coffee")

t1.join()  # wait for thread to finish
print("Thank you for your services, T1")
