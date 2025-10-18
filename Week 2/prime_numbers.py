def is_prime(num):
    count = 0
    if num > 1:
        for i in range(1,num):
            if num % i == 0:
                count += 1
        
        if count <2:
            print("True")
        else:
            print("False")  
                
                
is_prime(73)