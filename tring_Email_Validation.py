email = input("Enter your email : ")

# minimum lenght of gmail address must be 6

k,j,d = 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."): #XOR operator will be true if only anyone of them is true.
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="." or i=="_" or i=="@":
                        continue
                    else:   #For any other special characters.
                        d=1

                if k==1 or j==1 or d==1:
                    print("Error5 : Wrong Email Address.")
                else:
                    print("Valid Email Address.")
            else:
                print("Error4 : Wrong Email Address.")
        else:
            print("Error3 : Wrong Email Address.")
    else:
        print("Error2 : Wrong Email Address.")
else:
    print("Error1 : Wrong Email Address.")
