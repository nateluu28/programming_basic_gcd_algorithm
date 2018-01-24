#Nathan Luu
#Comp 157
#Programming Exercise 1-1

#Three algorithms
#Use array for the prime numbers
import time

#function for euclid's algorithm
def euclid(m, n):

    while n:
        r = m % n
        m = n
        n = r
    return m


#function for consecutive integer counting algorithm
def cic(m, n):

    t = min(m, n)

    while t:
        if (m % t) == 0:
            if (n % t) == 0:
                return t
        t -= 1

#function that takes prime factorization of any number and returns it into a list
def primeFact(f):
    factList =[]
    for i in primeList:
        while(f % i) == 0:
            factList.append(i)
            f /= i 
            if (f == 1):
                return factList

    return null    

#function for middle school procedure's algorithm
def msp(m, n):
    z = 1
    factList1 = primeFact(m)
    factList2 = primeFact(n)
    
    for i in range(len(factList1)):
        for j in range(len(factList2)):
            if(factList1[i] == factList2[j]):
                z *= factList1[i]
                factList1[i]= 1
                factList2[j]= 1

    return z


primeList = [2,3,5,7,11,13,17,19]

#recommended inputs to use: "60,24" for smaller data example|"1071,462" for bigger data example
m = int(input("type out m: "))
n = int(input("type out n: "))

#function call to print euclid algorithm time
print ("The GCD for Euclid's algorithm is"),
start1 = time.time()
print euclid(m, n)
end1 = time.time()
print ("The computing time of this algorithm is"), (end1 - start1), ("seconds.")

#function call to print cic algorithm time
print ("The GCD for Consecutive Integer Checking Algortihm is"),
start2 = time.time()
print cic(m, n)
end2 = time.time()
print ("The computing time of this algorithm is"), (end2 - start2), ("seconds.")

#function call to print msp algorithm time
print ("The GCD for Middle School Algortihm is"),
start3 = time.time()
print msp(m, n)
end3 = time.time()
print ("The computing time of this algorithm is"), (end3 - start3)

#references used: https://stackoverflow.com/questions/19290762/cant-modify-list-elements-in-a-loop-python



