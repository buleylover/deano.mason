import time

print("welcome to clicker get the most point you can") 
print("hint try looking for secrets to increase you score")

def main():
    score = 0
    while True:
        print("Score: {}".format(score))
        print("1. Click")
        print("20. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            score += 1
        elif choice == "2":
            score += 10
            print("you found a gift + 10 point")
            
        elif choice == "3":
              score += 2
              print("double points") 

        elif choice == "9":
            score -= 200
            print("womp,womp") 

      
           
        
        elif choice == "20":
            
            print("thank for playing")
        
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
