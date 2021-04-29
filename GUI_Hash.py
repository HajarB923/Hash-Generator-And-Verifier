from tkinter import *
from tkinter import scrolledtext 
import hashlib
#
#
############################        Functions        ############################
'''                              HASH GENERATOR                               '''
#
#Copy the text from hash 
def copy_text():
    global generated_hash
    root.clipboard_clear()
    generated_hash=hashOutput1.get('1.0', 'end-1c')
    root.clipboard_append(generated_hash)
    
#Generate the hash code and insert it into hash 
def generate():
    messageToHash=entryMsg1.get('1.0', 'end-1c').encode('utf-8')
    if hash_gen_choice.get()=='Choose' :
        errorMsg1= Label(myCanvas,text="Please choose a hash function ->",bg="white",fg='red')
        errorMsg1.config(font=("Calibri",8,'bold'))
        errorMsg1.place(relx =0.51, rely=0.29, anchor='center')
    elif hash_gen_choice.get()=='SHA-1' :
        #a label to hide the error message
        nothing1=Label(myCanvas,text="Please choose a hash function ->",bg="white",fg='white')
        nothing1.config(font=("Calibri",8,'bold'))
        nothing1.place(relx =0.51, rely=0.29, anchor='center')
        hash_object=hashlib.sha1(messageToHash)
    elif hash_gen_choice.get() =='MD5':
        #a label to hide the error message
        nothing1=Label(myCanvas,text="Please choose a hash function ->",bg="white",fg='white')
        nothing1.config(font=("Calibri",8,'bold'))
        nothing1.place(relx =0.51, rely=0.29, anchor='center')
        hash_object=hashlib.md5(messageToHash)
    pbHash=hash_object.hexdigest()
    hashOutput1.delete('1.0',END)
    hashOutput1.config(state=NORMAL)
    hashOutput1.insert(INSERT, pbHash)
#
'''                              HASH VERIFIER                               '''
#
def generate_msgToVerif():
    messageToHash=entryMsg2.get('1.0', 'end-1c').encode('utf-8')
    if hash_verif_choice.get()=='Choose' :
        errorMsg2= Label(myCanvas,text="Please choose a hash function ->",bg="white",fg='red')
        errorMsg2.config(font=("Calibri",8,'bold'))
        errorMsg2.place(relx =0.531, rely=0.738, anchor='center')
    elif hash_verif_choice.get()=='SHA-1' :
        #a label to hide the error message
        nothing2=Label(myCanvas,text="Please choose a hash function ->",bg="white",fg='white')
        nothing2.config(font=("Calibri",8,'bold'))
        nothing2.place(relx =0.531, rely=0.738, anchor='center')
        hash_object=hashlib.sha1(messageToHash)
    elif hash_verif_choice.get() =='MD5':
        #a label to hide the error message
        nothing2=Label(myCanvas,text="Please choose a hash function ->",bg="white",fg='white')
        nothing2.config(font=("Calibri",8,'bold'))
        nothing2.place(relx =0.531, rely=0.738, anchor='center')
        hash_object=hashlib.md5(messageToHash)
    pbHash=hash_object.hexdigest()
    hashOutput2.delete('1.0',END)
    if Checksum_input.get('1.0', 'end-1c')=='':
        #a label to hide the result message
        nothing4=Label(myCanvas,text= "The messages are identitical :)", bg="white", fg='white')
        nothing4.config(font=("Calibri",14))
        nothing4.place(relx =0.5, rely=0.92, anchor='center')
        errorMsg3= Label(myCanvas,text="Please add a checksum",bg="white",fg='red')
        errorMsg3.config(font=("Calibri",8,'bold'))
        errorMsg3.place(relx =0.71, rely=0.905, anchor='center')
    else :
        #a label to hide the error message
        nothing3= Label(myCanvas,text="Please add a checksum",bg="white",fg='white')
        nothing3.config(font=("Calibri",8,'bold'))
        nothing3.place(relx =0.71, rely=0.905, anchor='center')
        hashOutput2.config(state=NORMAL)
        hashOutput2.insert(INSERT, pbHash)
        if hashOutput2.get('1.0', 'end-1c')==Checksum_input.get('1.0', 'end-1c'):
            verif_result=Label(myCanvas,text= "The messages are identitical :)", bg="white")
            verif_result.config(font=("Calibri",14))
            verif_result.place(relx =0.5, rely=0.92, anchor='center')
        else : 
            verif_result=Label(myCanvas,text= "The messages are different :(", bg="white")
            verif_result.config(font=("Calibri",14))
            verif_result.place(relx =0.5, rely=0.92, anchor='center')

def verify ():
    generate_msgToVerif()
#
#
#
############################        Prepare the environment        ############################
#
root= Tk(className=' Hash Generator & Verifier ')
root.resizable(False,False)
root.geometry("700x700") 
root.iconphoto(False,PhotoImage(file='hachIcon.png'))
#
#Create the canvas
#
myCanvas=Canvas(root,width=700,height=700,background='white') 
myCanvas.grid(row=0,column=0)
myCanvas.create_line(1.5,0,1.5,700,fill='cadet blue') #left border
myCanvas.create_line(698.5,0,698.5,700,fill='cadet blue') #right border
#
'''''''''''''''''''''''''''          HASH GENERATOR          '''''''''''''''''''''''''''
#
# Label : HASH GENERATOR
#
label1= Label(myCanvas,text="HASH GENERATOR",bg="white")
label1.config(font=("Calibri",18,'bold'))
label1.place(relx =0.5, rely=0.05, anchor='center')
#
# Message :
#
msg1=Label(myCanvas,text= "Message :", bg="white")
msg1.config(font=("Calibri",14))
msg1.place(relx =0.15, rely=0.1, anchor='ne')
#
# input [Message]
#
entryMsg1=scrolledtext.ScrolledText(myCanvas, height=5, width=70, bg='snow', bd=1)
entryMsg1.place(relx =0.5, rely=0.2, anchor='center')
#
# Hash :
#
hashLabel=Label(myCanvas,text= "Hash :", bg="white")
hashLabel.config(font=("Calibri",14))
hashLabel.place(relx =0.11, rely=0.3, anchor='ne')
#
# Hash output 
#
hashOutput1=scrolledtext.ScrolledText(myCanvas, height=0.5, width=70, bg='snow', bd=1)
hashOutput1.config(state=DISABLED)
hashOutput1.place(relx =0.5, rely=0.38, anchor='center')
#
# Dropdown menu to choose a hash function
#
hash_gen_choice=StringVar(root)
choices={'SHA-1','MD5'}
hash_gen_choice.set('Choose')
menu=OptionMenu(myCanvas,hash_gen_choice,*choices)
menu.config(font=("Calibri",10),padx=10,pady=7,width=6, borderwidth=1)
menu.place(relx =0.695, rely=0.288, anchor='center')
#
# Generate button
#
generate = Button(myCanvas,text="Generate", font=("Calibri",10),padx=21,pady=5, command=generate) 
generate.config(borderwidth=1)
generate.place(relx =0.84, rely=0.288, anchor='center')
#
# Copy Button
#
copy = Button(myCanvas,text="Copy", font=("Calibri",8),padx=0,pady=0, command=copy_text) 
copy.config(borderwidth=1, width=5)
copy.place(relx =0.115, rely=0.436, anchor='center')
#
### Separator ###
#
myCanvas.create_line(0,330,700,330,fill='cadet blue') 
#
'''''''''''''''''''''''''''          HASH VERIFIER          '''''''''''''''''''''''''''
#
# Label : HASH VERIFIER
#
Label2= Label(myCanvas,text="HASH VERIFIER",bg="white")
Label2.config(font=("Calibri",18,'bold'))
Label2.place(relx =0.5, rely=0.5, anchor='center')
#
# Message to verify :
#
msg2=Label(myCanvas,text= "Message to verify :", bg="white")
msg2.config(font=("Calibri",14))
msg2.place(relx =0.246, rely=0.55, anchor='ne')
#
# input [Message to verify]
#
entryMsg2=scrolledtext.ScrolledText(myCanvas, height=5, width=70, bg='snow', bd=1)
entryMsg2.place(relx =0.5, rely=0.65, anchor='center')
#
# Hash (*) :
#
hashLabel2=Label(myCanvas,text= "Hash (*):", bg="white")
hashLabel2.config(font=("Calibri",14))
hashLabel2.place(relx =0.14, rely=0.778, anchor='ne')
#
# Hash (*) output 
#
hashOutput2=scrolledtext.ScrolledText(myCanvas, height=2, width=32, bg='snow', bd=1)
hashOutput2.place(relx =0.28, rely=0.855, anchor='center')
#
# Checksum :
#
Checksum_label=Label(myCanvas,text= "Checksum :", bg="white")
Checksum_label.config(font=("Calibri",14))
Checksum_label.place(relx =0.62, rely=0.778, anchor='ne')
#
# input [Checksum]
#
Checksum_input=scrolledtext.ScrolledText(myCanvas, height=2, width=32, bg='snow', bd=1)
Checksum_input.place(relx =0.716, rely=0.855, anchor='center')
#
# Dropdown menu to choose a hash function
#
hash_verif_choice=StringVar(root)
choices={'SHA-1','MD5'} # !!!!!
hash_verif_choice.set('Choose')
menu2=OptionMenu(myCanvas,hash_verif_choice,*choices)
menu2.config(font=("Calibri",10),padx=10,pady=7,width=6, borderwidth=1)
menu2.place(relx =0.718, rely=0.737, anchor='center')
#
# Verify button
#
verify = Button(myCanvas,text="Verify", font=("Calibri",10),padx=21,pady=5, command=verify) 
verify.config(borderwidth=1)
verify.place(relx =0.85, rely=0.737, anchor='center')
#
'''''''''''''''''''''''''''          THE END          '''''''''''''''''''''''''''
#
# Exit button
ExitButton = Button(myCanvas,text="Exit", font=("Calibri",10),padx=21,pady=5, command=root.destroy) 
ExitButton.config(borderwidth=1)
ExitButton.place(relx =0.91, rely=0.95, anchor='center')
#
#
root.mainloop()