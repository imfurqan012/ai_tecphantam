Education=int(input("Enter Your Education: "))
Age=int(input("Enter Your Age: "))
Height=float(input("Enter Your Height: "))


#if(Education>=14 and Age>=18 and Heights>=5)
   # print("Eligible")
#else:
   # print("Not Eligible") 


if((Education>=16 and Age>=18 )or(Education>=16 and Height>=5)or(Age>=18 and Height>=5)):
    print("You are Eligible")
else:
    print("You are not Eligible")
    


       

