# questao 2

def FiboList():
    global numByUser    
    numByUser = int(input("Insira um número para verificar se esta na sequencia de fibonacci:\n"))
    isInTheList(buildList(numByUser))

def buildList(numByUser):
    fibonacciList = [0,1,1]
    firstIndex = 1
    secondIndex = 2
    while len(fibonacciList) < numByUser:
        nextNumber = fibonacciList[firstIndex]+fibonacciList[secondIndex]
        fibonacciList.append(nextNumber)
        firstIndex +=1
        secondIndex +=1
    return fibonacciList

def chkList(list):
     for number in list:
        if number == numByUser:
            return True
        else:
            return False
            
def isInTheList(list):
    if chkList(list):
        print("Seu número está na sequência de Fibonacci !")
    else:
        print("seu número não está na sequência de Fibonacci.")

FiboList() 