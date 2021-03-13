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
  
trashSize = Label(frame, text =osCore.folderSize(), fg ="red") 
trashSize.pack( side = LEFT) 
  
b2_button = Button(frame, text ="Geeks2", fg ="brown") 
b2_button.pack( side = LEFT ) 
  
b3_button = Button(frame, text ="Geeks3", fg ="blue") 
b3_button.pack( side = LEFT ) 
  
b4_button = Button(bottomframe, text ="Geeks4", fg ="green") 
b4_button.pack( side = BOTTOM) 
  
b5_button = Button(bottomframe, text ="Geeks5", fg ="green") 
b5_button.pack( side = BOTTOM) 
  
b6_button = Button(bottomframe, text ="Geeks6", fg ="green") 
b6_button.pack( side = BOTTOM) 

window.title('Plasma Pro')
window.geometry("450x300") 
window.mainloop()
