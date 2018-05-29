print('''Enter your new password:
Must contain:
1. At least eight characters long
2. Has lower case and upper case letters.
3. Has numbers and letters.
''')
end=0
while True:
    while True:
        count=0
        a=input('New Password:        ')
        for x in a:
            count+=1
        if count>=8:
            count1=0
            count2=0
            for x in a:
                if x.isupper()==True:
                    count1+=1
                else:
                    count2+=1
            if count1<1 and count2<2:
                count1=0
                count2=0
                for x in a:
                    if x.isdigit()==True:
                        count1+=1
                    else:
                        count2+=1
                if count1<1 and count2<2:
                    b=input("Enter the password again:")
                    if a==b:
                        break
                        end=1
                    else:
                        print("The passwords do not match")
                else:
                    print("The password has to have numbers and letters")
            else:
                print("The password has to contain at least one lower case letter and one upper case letter")
        else:
            print("The password does not have at least eight characters")
