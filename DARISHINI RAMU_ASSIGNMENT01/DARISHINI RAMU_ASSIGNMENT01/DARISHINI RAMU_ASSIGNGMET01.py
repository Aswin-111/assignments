import time

# Function to compute Mean and Standard Deviation
def calcMeanStdDev(a1,n):
    # a1 is the list
    # n is the length of a1
    # m is mean
    # s is std.dev.
    m = sum(a1)/n
    s1 = []

    for i in range (n):
        s = (a1[i] - m) ** 2
        s1.append(s)

    s2 = sum(s1)
    s3 = s2/ (n-1)
    s4 = s3 ** 0.5

    return str(format(m,".2f")) + "\t\t" + str(format(s4, ".2f"))

# Assigning variables
a = []
b = []
c= []

# Assigning new variables for Task #3 (a)
x = []
y = []
z = []

# Read the text file
with open("aldata.txt", "r") as input:
    for line in input:
        number_str = line.split()

        c1 = number_str[0]
        c2 = number_str[1]
        c3 = number_str[2]

        # Convert data to float numbers and store in a list
        n1 = [float(c1)]
        n2 = [float(c2)]
        n3 = [float(c3)]

        # Formatting the final output
        a.extend (n1)
        b.extend (n2)
        c.extend (n3)

        # Output Task #3 (a) 1
        x.extend (n1)
        y.extend(n2)
        z.extend(n3)

print("\nTask 1 and 2\n")
print("a is" + str (a))
print("b is" + str (b))
print("c is" + str (c))

print("\n\nTask 3\n")
print("\tMean\t\tStandard Deviation")
print("x\t" + calcMeanStdDev (x, len(x)))
print("y\t" + calcMeanStdDev (y, len(y)))
print("z\t" + calcMeanStdDev (z, len(z)))

time.sleep(5)

