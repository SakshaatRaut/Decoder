from tkinter import *
import base64
from tkinter import messagebox


#screen is the instance here 
#Tk is the class
#our window is named "screen"
screen = Tk()
#SIZE
screen.geometry("680x600")
#TITLE
screen.title("ENCRYPTION AND DECRYPTION ")
#BACKGROUND COLOR
screen.configure(bg = "grey")


#DEFINING FUNCTION TO ENCRYPT AND SHOW THE GIVEN INPUT 

def encrypt():
    #SETTING VARIABLE 'PASSWORD' AS GLOBAL 
    global password
    #FETCH THE DATA FROM CODE AND THROW IT TO PASSWORD
    password = code.get()
        
    passkey = input_passkey.get() 


    if password == passkey and password != "" :
        #DIALOGUE BOX
        encryptscreen = Toplevel(screen)
        encryptscreen.title("ENCRYPTED DATA")
        encryptscreen.geometry("400x400")
        encryptscreen.configure(bg = "grey")
        


        #1.0 means from first word and 0 character index
        # END  is for , get data till the end . 

        # 4 MAIN LINES

        message = input_text1.get(1.0 , END)
        #ENCODING MESSAGE
        encodemessage = message.encode("ascii")
        base64bytes = base64.b64encode(encodemessage)
        encrypt = base64bytes.decode("ascii")


        Label(encryptscreen , text = "ENCRYPTED TEXT", font = ("Comic Sans MS", 15, "bold", "underline" ), bg = "grey").place(x = 25 , y = 25)
        input_text2 = Text(encryptscreen , font = "12" , bd = 4 , wrap = WORD)
        input_text2.place(x = 23 , y = 70 , width = 350 , height = 180)
        input_text2.insert(END , encrypt)

    else:
        messagebox.showerror("ERROR" , "ENTER THE KEY")



#DEFINING FUNCTION TO ENCRYPT AND SHOW THE GIVEN INPUT 

def decrypt():

    password1 = input_passkey.get()

    if password1 == password:

        decryptscreen = Toplevel(screen)
        decryptscreen.title("DECRYPTED DATA")
        decryptscreen.geometry("400x400")
        decryptscreen.configure(bg = "grey")

        #1.0 means from first word and 0 character index
        # END  is for , get data till the end . 

        # 4 MAIN LINES

        message = input_text1.get(1.0 , END)
        encodemessage = message.encode("ascii")
        base64bytes = base64.b64decode(encodemessage)
        encrypt = base64bytes.decode("ascii")


        Label(decryptscreen , text = "DECRYPTED TEXT", font = ("Comic Sans MS", 15, "bold", "underline" ), bg = "grey").place(x = 25 , y = 25)
        input_text2 = Text(decryptscreen , font = "12" , bd = 4 , wrap = WORD)
        input_text2.place(x = 23 , y = 70 , width = 350 , height = 180)
        input_text2.insert(END , encrypt)

    else:
        messagebox.showerror("ERROR" , "Wrong Key")



def reset():
    input_text1.delete(1.0 , END)
    code.set("")


#HEADING         #.place is used for adjusting the text.
Label(screen , text = "ENTER THE TEXT FOR ENCRYPTION AND DECRYPTION" , font = ("Comic Sans MS", 15, "bold", "underline"), bg = "grey").place(x=55 , y=50)


#INPUT TEXT WIDGET
Label(screen , text = "ENTER THE INPUT TEXT " , font = ("Comic Sans MS", 12, "bold"), bg = "grey").place(x=60 , y=110)
input_text1 = Text(screen, font = "12" , bd = 4)
input_text1.place(x = 60 , y = 143 , width = 560 , height = 80)


#TAKING A key AS INPUT 
Label(screen , text = "ENTER A KEY " ,  font = ("Comic Sans MS", 12, "bold"), bg = "grey").place(x=280 , y=250)

#ENTRY WIDGET
code = StringVar()     # Holds a string; the default value is an empty string ""
#TEXTVARIABLE is used to provide value through a variable
input_passkey = Entry(textvariable = code , bd = 4 ,  font =12 , show = "*" )  
input_passkey.place( x= 225 , y=290 ,height = 50)
#TEXT VARIABBLE IS USED SUCH THAT WE WILL GET TO KNOW THE INPUT GIVEN IN THE INPUT BOX.


#BUTTON FOR ENCRYPT
Button(screen , text = "ENCRYPT" , font = ("Comic Sans MS", 12, "bold"), bg='#1F5F57' , fg = "#0A2A26" , command = encrypt).place( x = 85 , y = 380 , width = 180 , height = 50)
#BUTTON FOR DECRYPT
Button(screen , text = "DECRYPT" , font = ("Comic Sans MS", 12, "bold"), bg='#1F5F57' , fg = "#0A2A26" , command = decrypt).place( x = 425 , y = 380 , width = 180 , height = 50)
#BUTTON FOR RESET
Button(screen , text = "RESET" , font = ("Comic Sans MS", 12, "bold"), bg='#1F5F57' , fg = "#0A2A26", command = reset).place( x = 215 , y = 480 , width = 250 , height=50)


mainloop()
