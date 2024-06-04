import random

numberList = []

def main():
  
def game():
  
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

if __name__ == "__main__":
    main()
