numberList = []

def main():
    successCount = 0
    n = int(input())
    for i in range(n):
        if game():
            successCount += 1
    print(f"성공 확률: {successCount/n}")
    
    
#def game():
  
#def find_number():

#def setRandomNumber():


if __name__ == "__main__":
    main()
