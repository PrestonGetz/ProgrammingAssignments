error=False
at_true=False
email=input(str("What is the e-mail you want to test?")).lower
for x in email:
    if x=='@':
        at_true=True
if at_true==False:
    error=True
    print("Error: no @ symbol")
split=email.split('@')
if split[1]!="gmail.com":
    error=True
    print("Error: does not have gmail.com at the end")
if error==False:
    print("E-mail is valid")
