def sumofnumbers():
    age = input("Hi there! Please enter your age: ")
    
    age = int(age)
    total = 0
        
    for i in range(1, age + 1):
            total += i
            
    print(f"The sum of all numbers from 1 to {age} is: {total}")

sumofnumbers()