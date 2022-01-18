# -*- coding: utf-8 -*-
"""
*** Simple PDF Viewer inside the current Folder ***

The current GUI program permits to list all pdf files inside the current folder
where the exe file is placed, and visualize them.

Created on Mon Jan 10 2022

@author: Marco Martino Rosso
"""
# import modules
import tkinter as tk
import tkPDFViewer as pdf 
from os import path
from glob import glob
import sys
import os
from PIL import ImageTk, Image

# set global variable v2
global v2,zoomDPI,zoomDPIdefault
v2 = None
zoomDPI,zoomDPIdefault=72,72

def list_file_ext_current_folder(dr, ext, ig_case=False):
    if ig_case: # case sensitive
        ext =  "".join(["[{}]".format(ch + ch.swapcase()) for ch in ext])
    return glob(path.join(dr, "*." + ext))

def on_select(evt):
    try:
        global v2,value
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        # print('You selected item %d: "%s"' % (index, value))
        if v2: # if old instance exists, destroy it first
            v2.destroy()
        # creating object of ShowPdf from tkPDFViewer. 
        v1 = pdf.ShowPdf() 
        # clear the image list # this corrects the bug inside tkPDFViewer module
        v1.img_object_li.clear()
        # Adding pdf location and width and height. 
        v2=v1.pdf_view(frame2,pdf_location = f"{value}",zoomDPI=zoomDPIdefault)
        # Placing Pdf inside gui
        v2.pack()
    except:
        pass

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# tkinter root widnow
window = tk.Tk() 
window.geometry('800x600')
window.minsize(800, 600)
window.title('Simple PDF Viewer inside the current Folder')
window.wm_iconbitmap(resource_path('logo.ico'))

root=tk.PanedWindow(window, orient="horizontal")
# root.configure(background="white")
# root.pack_propagate(0)

# tkinter frame for listbox
frame1=tk.Frame(root,width=100)
root.add(frame1)
# tkinter frame for pdf viewer
frame2=tk.Frame(root)
root.add(frame2)

root.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
# tkinter frame for utility buttons
frame3=tk.Frame(frame2)

# frame1.pack(side="left",fill="both",expand=True)
# frame2.pack(side="right",fill="both",expand=True)
frame3.pack(side="bottom",fill="both",expand=True)

# get list of pdf files inside the current folder
paths=list_file_ext_current_folder(".","pdf",True)

# vertical scrollbar
yscrollbar = tk.Scrollbar(frame1)
yscrollbar.pack(side = tk.RIGHT, fill = tk.Y)

# generate listbox
lb = tk.Listbox(frame1, selectmode = "SINGLE", name='lb', yscrollcommand = yscrollbar.set)

lb.pack(padx = 10, pady = 10, expand = tk.YES, fill = "both")

if paths: # if paths list is not empty
    for each_item in range(len(paths)):
    	lb.insert(tk.END, paths[each_item])
    	lb.itemconfig(each_item)
    lb.bind('<<ListboxSelect>>', on_select)
    lb.select_set(0) # This only sets focus on the first item.
    lb.event_generate("<<ListboxSelect>>") # This creates the even clicked
else:
    lb.insert(tk.END, "No PDF are present in this forlder!")

# Attach listbox to vertical scrollbar
yscrollbar.config(command = lb.yview)

# %% Utility Buttons inside frame3: zoom buttons
def zoomIn():
    try:
        global zoomDPI,v2,value
        zoomDPI=int(zoomDPI*1.5)
       # messagebox.showinfo( "Hello Python", "Hello World")
        if v2: # if old instance exists, destroy it first
            v2.destroy()
        # creating object of ShowPdf from tkPDFViewer. 
        v1 = pdf.ShowPdf() 
        # clear the image list # this corrects the bug inside tkPDFViewer module
        v1.img_object_li.clear()
        # Adding pdf location and width and height. 
        v2=v1.pdf_view(frame2,pdf_location = f"{value}", zoomDPI=zoomDPI)
        # Placing Pdf inside gui
        v2.pack()
    except:
        pass
    
def zoomOut():
    try:
        global zoomDPI,v2,value
        zoomDPI=int(zoomDPI*0.5)
       # messagebox.showinfo( "Hello Python", "Hello World")
        if v2: # if old instance exists, destroy it first
            v2.destroy()
        # creating object of ShowPdf from tkPDFViewer. 
        v1 = pdf.ShowPdf() 
        # clear the image list # this corrects the bug inside tkPDFViewer module
        v1.img_object_li.clear()
        # Adding pdf location and width and height. 
        v2=v1.pdf_view(frame2,pdf_location = f"{value}", zoomDPI=zoomDPI)
        # Placing Pdf inside gui
        v2.pack()
    except:
        pass

def zoomRestore():
    try:
        global zoomDPI,zoomDPIdefault,v2,value
        zoomDPI=zoomDPIdefault
       # messagebox.showinfo( "Hello Python", "Hello World")
        if v2: # if old instance exists, destroy it first
            v2.destroy()
        # creating object of ShowPdf from tkPDFViewer. 
        v1 = pdf.ShowPdf() 
        # clear the image list # this corrects the bug inside tkPDFViewer module
        v1.img_object_li.clear()
        # Adding pdf location and width and height. 
        v2=v1.pdf_view(frame2,pdf_location = f"{value}", zoomDPI=zoomDPI)
        # Placing Pdf inside gui
        v2.pack()
    except:
        pass

# Load button images
BzoomINimg = Image.open(resource_path("Inbtn.png"))
BzoomINimg = BzoomINimg.resize((40, 40), Image.ANTIALIAS) #(height, width)
BzoomINimg = ImageTk.PhotoImage(BzoomINimg) # convert to PhotoImage

BzoomRestoreimg = Image.open(resource_path("Restorebtn.png"))
BzoomRestoreimg = BzoomRestoreimg.resize((35, 40), Image.ANTIALIAS) #(height, width)
BzoomRestoreimg = ImageTk.PhotoImage(BzoomRestoreimg) # convert to PhotoImage

BzoomOUTimg = Image.open(resource_path("Outbtn.png"))
BzoomOUTimg = BzoomOUTimg.resize((40, 40), Image.ANTIALIAS) #(height, width)
BzoomOUTimg = ImageTk.PhotoImage(BzoomOUTimg) # convert to PhotoImage

# Buttons
BzoomIN = tk.Button(frame3, text ="+", command = zoomIn, image=BzoomINimg)
BzoomRestore = tk.Button(frame3, text ="z", command = zoomRestore, image=BzoomRestoreimg)
BzoomOUT = tk.Button(frame3, text ="-", command = zoomOut, image=BzoomOUTimg)

# pack buttons
BzoomIN.pack(side='left', anchor='e', expand=True)
BzoomRestore.pack(side='left',ipadx=5)
BzoomOUT.pack(side='right', anchor='w', expand=True)

# %% mainloop

window.mainloop()