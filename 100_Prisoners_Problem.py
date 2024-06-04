numberList = []

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

def find_number():

def setRandomNumber(): 


if __name__ == "__main__":
    main()
