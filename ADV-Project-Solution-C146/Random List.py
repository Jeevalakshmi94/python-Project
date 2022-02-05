# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 15:23:56 2021

@author: jivas
"""

from tkinter import *
import random

root=Tk()

root.title("Random LIst")
root.geometry("400x400")

randomlist=Label(root)
randomlistSorted=Label(root)

def randomList():

   rand = random.sample(range(10,100),10)
   randomlist["text"]= "Random list -" +str(rand)
   rand.sort()
   randomlistSorted["text"]= "Sorted List -" +str(rand)
  


btn = Button(root,text="Generate random number" , command= randomList)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

randomlist.place(relx=0.5,rely=0.4,anchor=CENTER)

randomlistSorted.place(relx=0.5,rely=0.5,anchor=CENTER)






root.mainloop();
