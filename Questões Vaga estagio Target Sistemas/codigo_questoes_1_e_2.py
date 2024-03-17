# questao 1

indice = 13
soma = 0
k = 0

while k < indice:
    k+=1
    soma +=k 

    print("K: ",k,"soma: ",soma)

print(soma)

# questao 2

def chkList(list):
     for number in list:
            if number == num:
                return True

def isInTheList(list):
    if chkList(list):
        print("Seu número está na sequência de Fibonacci !")
    else:
        print("seu número não está na sequência de Fibonacci.")

def FiboList():
    fibonacciList = [0,1,1]
    firstIndex = 1
    secondIndex = 2
    global num 
    num = int(input("Insira um número para verificar se esta na sequencia de fibonacci:\n"))
    while len(fibonacciList) < num:
        nextNumber = fibonacciList[firstIndex]+fibonacciList[secondIndex]
        fibonacciList.append(nextNumber)
        firstIndex +=1
        secondIndex +=1
    
    isInTheList(fibonacciList)
    
FiboList()