from tkinter import *
import tkinter as tk
import library.core as osCore
window = tk.Tk() 



osN = Label(window, text ='OS : '+osCore.osName(), font = "50")  
osN.pack() 
  
frame = Frame(window) 
frame.pack() 
  
bottomframe = Frame(window) 
bottomframe.pack( side = BOTTOM )

trashSizee=" Trash : "+osCore.trashSize()+" "
  
trashSize = Label(frame, text =trashSizee, fg ="#444444", font = "50") 
trashSize.pack( side = LEFT,padx=10) 
  
b2_button = Button(frame, text ="Clear Trash", fg ="#444444",command =osCore.clearTrash()) 
b2_button.pack( side = LEFT ) 
  
b3_button = Button(frame, text ="Geeks3", fg ="blue") 
b3_button.pack( side = LEFT ) 
  
b4_button = Button(bottomframe, text ="Geeks4", fg ="green") 
b4_button.pack( side = BOTTOM) 
  
b5_button = Button(bottomframe, text ="Geeks5", fg ="green") 
b5_button.pack( side = BOTTOM) 
  
b6_button = Button(bottomframe, text ="Geeks6", fg ="green") 
b6_button.pack( side = BOTTOM) 

window.title('Python Gui')
window.geometry("400x300") 
window.mainloop()
