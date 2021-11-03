import numpy as np
import itertools
c = True
while c:
    dim = input("Enter size of matrix: ")
    while True:
        if dim.isdigit() == False:
            dim = input("You entered wrong number\n try again: ")
        elif type(dim) == float:
            dim = input("Size can't be float number\n try again:: ")
        else:
            break
    def random_matrix(dim):
        """
        The function generates dim x dim array of integers
        between 0 and 10.
        """
        matrix = np.random.randint(10, size = (dim, dim))
        return matrix
    m = random_matrix(int(dim))
    print("Matrix:\n ", m)
    def per(m):
        """
        The function create all possible permission
        """
        n = ""
        for i in range(len(m)):
            n += str(i+1)
        t = list(itertools.permutations(n, len(n)))
        return t
        
        
    def mark(t):
        """
        The function create list of sum all permutations with righ index + or -.
        """
        final_list = []
        for e in t:
            v = 0
            index = 1
            for i in range(len(e)):
                for s in range(i):
                    if e[s] > e[i]:
                        v += 1
            for i in range(len(e)):
                index = index * int(m[i][int(e[i])-1])
            if v % 2 == 0 or v == 0:
                final_list.append(index)
            else:
                final_list.append((-1)*(index))
        return final_list
    def sum(l):
        count = 0
        for i in range(len(l)):
            count += l[i]
        return count
    print("Determinant=",sum(mark(per(m))))
    print()
    print("np.linalg.det()=",round(np.linalg.det(m)))
    prog = input("Do you want to restart program?\n Please enter y - Yes, n - No: ")
    if prog == "y":
        c = True
    elif prog == "n":
        print("Program stoped")
        c = False
    else :
        print("you entered wrong index! Programm will restart")
        c = True
            
