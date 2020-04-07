####################
# Quiz biologiczny #
####################

from tkinter import *
import random

##################################
##################################
##################################

def lose():
    okno.after(500)
    tlo1 = Label(okno, image=przegrana)
    tlo1.place(x=0, y=0)
    button1=Button(okno, text="Wyjście", bg="red",padx=20, command=quit, cursor="pirate", fg="white")
    button1.config(font=("Arial", 10))
    button1.place(x=850, y=650)

    button5=Button(okno, text="Menu główne", bg="green", command=menu, fg="white")
    button5.config(font=("Arial", 10))
    button5.place(x=700, y=650)
    
    button5=Button(okno, text="Zagraj ponownie", bg="gold", command=start, fg="white")
    button5.config(font=("Arial", 10))
    button5.place(x=550, y=650)
    
def good11():
    okno.after(500)
    tlo1 = Label(okno, image=good1)
    tlo1.place(x=0, y=0)
    button1=Button(okno, text="Nastepne pytanie", bg="gold", cursor="heart",command=gra2)
    button1.config(font=("Arial", 15))
    button1.place(x=750, y= 550)

def good2():
    okno.after(500)
    tlo1 = Label(okno, image=good1)
    tlo1.place(x=0, y=0)
    button1=Button(okno, text="Nastepne pytanie", bg="gold", cursor="heart",command=gra3)
    button1.config(font=("Arial", 15))
    button1.place(x=750, y= 550)

def good3():
    okno.after(500)
    tlo1 = Label(okno, image=good1)
    tlo1.place(x=0, y=0)
    button1=Button(okno, text="Nastepne pytanie", bg="gold", cursor="heart",command=gra4)
    button1.config(font=("Arial", 15))
    button1.place(x=750, y= 550)

def good4():
    okno.after(500)
    tlo1 = Label(okno, image=good1)
    tlo1.place(x=0, y=0)
    button1=Button(okno, text="Nastepne pytanie", bg="gold", cursor="heart",command=gra5)
    button1.config(font=("Arial", 15))
    button1.place(x=750, y= 550)

def win():
    okno.after(1000)
    tlo1 = Label(okno, image=win1)
    tlo1.place(x=0, y=0)
    button1=Button(okno, text="Wyjście", bg="red",padx=20, command=quit, cursor="pirate", fg="white")
    button1.config(font=("Arial", 10))
    button1.place(x=850, y=650)

    button5=Button(okno, text="Menu główne", bg="green", command=menu, fg="white")
    button5.config(font=("Arial", 10))
    button5.place(x=700, y=650)
    
    button5=Button(okno, text="Zagraj ponownie", bg="gold", command=start, fg="white")
    button5.config(font=("Arial", 10))
    button5.place(x=550, y=650)


def tworcy():
    
    tlo1 = Label(okno, image=tworcytlo)
    tlo1.place(x=0, y=0)
    button1.place(x=0, y=800)
    button2.place(x=0, y=800)
    button3.place(x=0, y=800)
    button4.place(x=0, y=800)
    button5=Button(okno, text="Powrót", bg="red", command=menu, fg="white")
    button5.config(font=("Arial", 10))
    button5.place(x=1200, y=660)

def menu():
    tlo1 = Label(okno, image=menutlo)
    tlo1.place(x=0, y=0)
    button1=Button(okno, text="Start",command=start, bg="green", padx=120, pady=24, activebackground="dark green", bd=2,  cursor="heart", activeforeground="black", highlightcolor="light green")
    button1.config(font=("Arial", 30))
    button1.place(x=470, y=240)
    button2=Button(okno, text="Opcje", bg="cyan", padx=100, cursor="plus", command=opcje)
    button2.config(font=("Arial", 20))
    button2.place(x=500, y=400)
    button3=Button(okno, text="Twórcy", bg="purple", padx=92, command=tworcy, cursor="dotbox")
    button3.config(font=("Arial", 20))
    button3.place(x=499, y=475)
    button4=Button(okno, text="Wyjście", bg="red",padx=86, command=quit, cursor="pirate")
    button4.config(font=("Arial", 20))
    button4.place(x=499, y=550)

def start():
    tlo1 = Label(okno, image=dark)
    tlo1.place(x=0, y=0)
    button1=Button(okno, text="Zaczynamy!",bg="green", command=gra1)
    button1.config(font=("Arial", 20))
    button1.place(x=630, y=510)

#######################################################################################################################
def gra1():
        tlo1 = Label(okno, image=game)

        tlo1.place(x=0, y=0)
        pytanie1 = Label(okno, bg="green", bd=0, text=zadanie1)
        pytanie1.config(font=("Arial, 25"))
        pytanie1.place(x=100, y=100)
        
        button1=Button(okno,text="a) Fermentacja mlekowa",bg="purple",padx=10, pady=12, command=good11)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=72)

        button1=Button(okno,text="b) Fermentacja grzybowa",bg="blue",padx=5, pady=12, command=lose)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=214)

        button1=Button(okno,text="c) Fermentacja etanolowa",bg="orange",pady=12, command=lose)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=356)
        
        button1=Button(okno,text="d) Fermentacja masłowa",bg="light green",pady=14, padx=10, command=lose)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=500)

def gra2():
        tlo1 = Label(okno, image=game)
        tlo1.place(x=0, y=0)
        pytanie1 = Label(okno, bg="green", bd=0, text=zadanie2)
        pytanie1.config(font=("Arial, 25"))
        pytanie1.place(x=100, y=100)
        
        button1=Button(okno,text="a) Metan",bg="purple",padx=152, pady=12, command=lose, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=72)

        button1=Button(okno,text="b) Gaz ziemny",bg="blue",padx=102, pady=12, command=lose, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=214)

        button1=Button(okno,text="c) Biogaz",bg="orange", padx=146, pady=12, command=good2, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=356)
        
        button1=Button(okno,text="d) Ekogaz",bg="light green",pady=14, padx=140, justify=CENTER, command=lose)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=500)

def gra3():
        tlo1 = Label(okno, image=game)
        tlo1.place(x=0, y=0)
        pytanie1 = Label(okno, bg="green", bd=0, text=zadanie3)
        pytanie1.config(font=("Arial, 20"))
        pytanie1.place(x=90, y=100)
        
        button1=Button(okno,text="a) Destymutor",bg="purple",padx=108, pady=12, command=lose, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=72)

        button1=Button(okno,text="c) Gaz ziemny",bg="orange",padx=102, pady=12, command=lose, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=356)

        button1=Button(okno,text="b) Biogaz",bg="blue", padx=146, pady=12, command=good3, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=214)
        
        button1=Button(okno,text="d) Biofiltr",bg="light green",pady=14, padx=150, justify=CENTER, command=good3)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=500)

def gra4():
        tlo1 = Label(okno, image=game)
        tlo1.place(x=0, y=0)
        pytanie1 = Label(okno, bg="green", bd=0, text=zadanie4)
        pytanie1.config(font=("Arial, 20"))
        pytanie1.place(x=100, y=100)

        
        button1=Button(okno,text="a) Szczepionka",bg="purple",padx=94, pady=12, command=good4, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=72)

        button1=Button(okno,text="b) Antybiotyk",bg="blue",padx=116, pady=12, command=lose, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=214)

        button1=Button(okno,text="c) Antygen",bg="orange", padx=134, pady=12, command=lose, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=356)
        
        button1=Button(okno,text="d) Lek",bg="light green",pady=14, padx=172, justify=CENTER, command=lose)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=500)

def gra5():
        tlo1 = Label(okno, image=game)
        tlo1.place(x=0, y=0)
        pytanie1 = Label(okno, bg="green", bd=0, text=zadanie5)
        pytanie1.config(font=("Arial, 25"))
        pytanie1.place(x=100, y=100)
        
        button1=Button(okno,text="a) Biobiałka",bg="purple",padx=126, pady=12, command=lose, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=72)

        button1=Button(okno,text="b) Biofarmaceutyki",bg="blue",padx=66, pady=12, command=win, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=214)

        button1=Button(okno,text="c) Ekoantybiotyki",bg="orange", padx=80, pady=12, command=lose, justify=CENTER)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=356)
        
        button1=Button(okno,text="d) Białka mocy ",bg="light green",pady=14, padx=92, justify=CENTER, command=lose)
        button1.config(font=("Arial",30))
        button1.place(x=735, y=500)
#######################################################################################################################
    
def opcje():
        update = 500
        okno.after(update)
        tlo1 = Label(okno, image=opcje1)
        tlo1.place(x=0, y=0)
        button1=Button(okno, text="powrót", command=menu)
        button1.place(x=100, y=600)
        
        
#################
# Okno Startowe #
#################


okno=Tk()
okno.geometry("1280x720")
okno.title("Quiz")
okno.resizable(width=False, height=False)

win1 = PhotoImage(file="win.png")
good1 = PhotoImage(file="good.png")
przegrana = PhotoImage(file="lose.png")
opcje1 = PhotoImage(file="opcje.png")
dark = PhotoImage(file="dark.png")
game = PhotoImage(file="game.png")
tworcytlo = PhotoImage(file="tworcy.png")
menutlo = PhotoImage(file="menu.png")
tlo1 = Label(okno, image=menutlo)
tlo1.place(x=0, y=0)

button1=Button(okno, text="Start", command=start, bg="green", padx=120, pady=24, activebackground="dark green", bd=2,  cursor="heart", activeforeground="black", highlightcolor="light green")
button1.config(font=("Arial", 30))
button1.place(x=470, y=240)

button2=Button(okno, text="Opcje", bg="cyan", padx=100, cursor="plus", command=opcje)
button2.config(font=("Arial", 20))
button2.place(x=500, y=400)

button3=Button(okno, text="Twórcy", bg="purple", padx=92, command=tworcy, cursor="dotbox")
button3.config(font=("Arial", 20))
button3.place(x=499, y=475)

button4=Button(okno, text="Wyjście", bg="red",padx=86, command=quit, cursor="pirate")
button4.config(font=("Arial", 20))
button4.place(x=499, y=550)

zadanie1="Jak się nazywa fermentacja,\n dzięki której tworzymy ser?"
zadanie2="Jak jest nazwa gazu będącego, \n produktem fermentacji \n metanowej związków \n pochodzenia organicznego?"
zadanie3="Jak się nazywa rzecz, która służy do \n oczyszczania powietrza z toksycznych \n substancji? Składa się z warstwy materiału \n porowatego zasiedlonego przez \n mikroorganizmy."
zadanie4="Jak się nazywa preparat, który po \n wprowadzeniu do organizmu powoduje \n wytworzenieodpornośći skierowanej \n przeciwko danemu drobnoustrojowi?"
zadanie5="Jak brzmi nazwa białkowych \n substancji leczniczych?"

