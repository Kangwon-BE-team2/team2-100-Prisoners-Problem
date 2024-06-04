import random

numberList = []

def setRandomNumber():
    for i in range(1, 101):
        numberList.append(i)
    random.shuffle(numberList)

def main():
    n = int(input())
    for i in range(n):
        game()
    
def game():
    setRandomNumber()
    for prisoner in range(100):
        if not find_number(prisoner):
            return False
    return True
  
def find_number(answer):
    result  = False # False mean prisoner is not able to find his number
    findList = range(100)
    findList.shuffle()
    findList = findList[:50]
    for i in findList:
        if answer == numberList[i]:
            result = True # True mean prisoner is able to find his number
            break
    return result

def find_number():

def setRandomNumber(): 

if __name__ == "__main__":
    main()
