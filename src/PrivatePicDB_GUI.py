'''
Created on 2020-01-14:
GUI for the project PrivatePictureDatabase (working title) based on tkinter.

Idea of the GUI:
Frontend for database-queries, including preselected lists of e.g. name-entries in the database, available years of the pictures, availables sceneries 
Preview of the images found in the database.
The logic layer shall include face-recognition and scenery recognition: training the models will be done in a popup window (name-selection, new name entries 
and similar for sceneries).

@author: ho-stil
'''

import tkinter as tk
from tkinter.constants import NW, W, LEFT, END
from tkinter import messagebox as msgbox
import sqlite3

class App():
    def __init__(self, master, titleApp='Window', iconApp=''):
        '''
        Define the window-layout:
        - Generate main window first (including menu-bar, Imageviewer-widget and search-fields a.s.o)
        - Load picture-database on startup - included in ini and menu for change of database
        '''
        master.title(titleApp)
        master.iconbitmap(iconApp)
        menubar = tk.Menu(master)
        master.config(menu=menubar)
        self.master=master
        # Menu entries
        #
        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label="")
        fileMenu.add_command(label="Quit", command=self.quitApp)
        menubar.add_cascade(label="Datei", menu=fileMenu)
        settingsMenu = tk.Menu(menubar)
        settingsMenu.add_command(label="Ablageorte für Bilder")
        settingsMenu.add_command(label="Datenbank")
        settingsMenu.add_command(label="Gesichtserkennung")
        menubar.add_cascade(label="Einstellungen", menu=settingsMenu)
    def quitApp(self):
        if msgbox.askyesno('Quit?', 'Do you want to close the program?'):
            self.master.quit()
    #def loadPicDB(self):
    #    
    def ShowPic(self, pathPic):
        '''
        Method for the main window: load the main picture and show it in the Imageviewer
        '''
        
if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(640, 480)#("720x480+300+300")
    app = App(root, titleApp="Your private picture database")
    root.mainloop()
