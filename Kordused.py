########################################################################## <<<<<<< 1 >>>>>>>
#def sk(n):
#    for _ in range(n):
#        print("   -----", end=" ")
#    print()  
#    for _ in range(n):
#        print("  |  O  |", end=" ")
#    print()  
#    for _ in range(n):
#        print("  !  -  !", end=" ")
#    print()  

#n = int(input("vvedite chislo (ot 1 do 9): "))

#if 1 <= n <= 9:
#    sk(n)
#    print("Molodec!!!")
#else:
#    print("Please!!! vvedite chislo 1 do 9!!!")

############################################################################ <<<<<< 2 >>>>>>

#a = int(input("vedite stepen: "))
#n = int(input("vedite chislo: "))
#resultat = 1
#net = 1
#while resultat <= n**3:
#    print(f"{a}^{net} = {resultat}")
#    net += 1
#    resultat = a ** net
#print("Kruto!!!")

############################################################################ <<<<<< 3 >>>>>>>

#import random
#student = random.randint(1, 20)
#ocenki = [random.randint(1, 5)]
#a = 0
#b = ocenki
#for ocenki in student:
#    a += ocenki
#    if b == 0:
#        print("netu ocenki")
#else:
#    sred = a / b
#print(f"srednaja ocenka: {sred}")

########################################################################### <<<<<< 4 >>>>>>>

#podarok = 1
#vozrast = 1

#while podarok <=100:
#    vozrast += 1
#    podarok += vozrast

#print(f"prevysit 100 dolarov na {vozrast}!")

############################################################################ <<<<< 5 >>>>>>>

a = 1
b = 1
n = input("nomer: ")
n = int(n)
i = 0
while i < n - 2:
    sum = a + b
    a = b
    b = sum
    i = i + 1
print(f"element:",b)


#a, b = 0, 1
#print(a, b, end=" ")
#while b < 21: 
#    a, b = b, a + b
#    print(b, end=" ")
#print("ponjat i prostit...")














