import numpy as np

start = input("start from : ")
end = input("end with : ")
number = int(np.random.randint(int(start), int(end)+1))

g = int(input("Input your guess here : "))

while g != number:
    if g > number:
        print("The number is smaller")
        g = int(input("Give another guess : "))
    else:
        print("The number is bigger")
        g = int(input("Give another guess : "))

print("HOOORAY! That's correct!")
