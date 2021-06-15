#JosephusProblem
#6/15/2021

def joseph(n):
    if (n & (n-1) == 0) and n != 0:
        return 0
    i = 1
    while i < n:
        i *= 2
    i = int(i/2)
    l = n - i
    return (2 * l) + 1
   
print("Survivor is: " + str(joseph(int(input("Group size: "))))) 


