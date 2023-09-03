file = open('dieters.txt', 'r')
name = file.readline().strip("\n")
while name != '':
    w1 = int(file.readline())
    w2 = int(file.readline())
    w3 = w1-w2
    print(name+ " lost " + str(w3) + " pounds")
    name = file.readline().strip("\n")


