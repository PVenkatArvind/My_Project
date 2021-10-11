def gen_pass():
    import random

    upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"         # declaring all the characters we might use in a password
    lower_case= upper_case.lower()
    digits ="0123456789"
    symbols = "(){}[],;:-_/\\@#$%^&*!+?"

    upper,lower,numbers,syms= True,True,True,True    #6 # allowing the use of the above strings to create a password

    final_pass =""                                  #creating an empty string 

    if upper:                                       #this means , if we chose uppercase letters ,we are going to add it to the final string .
        final_pass+= upper_case
    if lower:
        final_pass+= lower_case
    if numbers:
        final_pass+= digits
    if syms:
        final_pass+= symbols

    length = 9            #length of each password 
    amount = 5            #number of passwords we want to generate
    for x in range(amount):
        password="".join(random.sample(final_pass,length))
        Output.insert(END,(password),END," (Password strength is strong)\n ",END)
    Output.insert(END,"You may choose any one of the five passwords given above")
    
def examin_strength():
    
    import re
    
    password=inputtxt.get('1.0',END)
    
    password_strength={'has_upper':False,'has_lower':False,'has_num':False}
    password_score={0:'invalid',1:'weak',2:'medium',3:'strong'}
    
    if len(password)<9:
        Output2.insert(END,"Invalid password(insufficient characters).\n",END)
    else:    
        
        if re.search(r'[A-Z]',password):
            password_strength['has_upper']=True

        if re.search(r'[a-z]',password):
            password_strength['has_lower']=True

        if re.search(r'[0-9]',password):
            password_strength['has_num']=True
    
    score=len([b for b in password_strength.values()if b])
    Output2.insert(END,"Password strength is ",END,password_score[score],END)

    if score>1 :
        Output2.insert(END," \n Valid password. ",END)
    else:
        Output2.insert(END,"\n Password must contain atleast 9 characters.\n",END,
                       " Password must contain atleast one uppercase letter.\n",END,
                       " Password must contain atleast one lowercase letter.\n" ,END,
                       "Password must contain atleast one digit.\n",END)




import tkinter as tk
from tkinter import *

root = tk.Tk() 
root.title('Password generator and Strength analyser')

Display=Button(root,height=2,width=25,text="Generate password",command=lambda:gen_pass())   #GUI for password generator
Output=Text(root,height=7,width=150,bg="misty rose")

Lab=tk.Label(root,text="Enter your password:")
Lab.place(relx=0.0,rely=3.0,anchor='nw')

inputtxt=Text(root,height=2,width=25,bg='DarkSeaGreen1')                                    #GUI for password strength analyser.
Display1=Button(root,height=2,width=20,text='Enter',command=lambda:examin_strength())
Output2=Text(root,height=10,width=150,bg='DarkSeaGreen3')

Display.pack()
Output.pack()
Lab.pack()
inputtxt.pack()
Display1.pack()
Output2.pack()

root.mainloop()


