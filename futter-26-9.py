from tkintertable import TableCanvas, TableModel
import glob
from tkinter import *
import numpy as np
import urllib.request 
import mechanicalsoup
from autocomplete import AutocompleteEntry
import csv
import numpy as np
import datetime
import os
import shutil
from  selenium import webdriver
import time
import pandas as pd
import re
import substring
import sys
import functools
from memory import reduce_mem_usage
from tkinter import messagebox
from sys import exit
from fpdf import FPDF
from datetime import date
import getpass
#import Mineral 

date=datetime.datetime.now()

# Ereignisbehandlung
def buttonaktualisieren():
    global status
    status ='aktualisieren'
    Tk.destroy(tkFenster)
    return 

def buttonneu():
    global status
    status ="neu"
    Tk.destroy(tkFenster)
    return 

def ButtonName():
    global NameRation
    NameRation=EingabeRation.get()
    Tk.destroy(tkFenster)

def matches(fieldValue, acListEntry):
    pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
    return re.search(pattern, acListEntry)

def buttonauswählen():
    global Betrieb,Betrieb1,Betrieb2
    Betrieb=EingabeBetrieb.get()
    Betrieb1=EingabeBetrieb1.get()
    Betrieb2=EingabeBetrieb2.get()
    Tk.destroy(tkFenster)
    return Betrieb 

def buttonabbrechen():
    Tk.destroy(tkFenster)
    global status
    status='beenden'
    quit()
    return status1 

def buttonVerarbeitenClick():
    global nameAusgewaehlt
    listeAusgewaehlt = listboxNamen.curselection()
    itemAusgewaehlt = listeAusgewaehlt[0]
    nameAusgewaehlt = listboxNamen.get(itemAusgewaehlt) 
    Tk.destroy(tkFenster)
    return nameAusgewaehlt  

def Buttonauswahlanalysen():
    global status1
    status1 ='fertig'
    Tk.destroy(tkFenster)
    return 

def Buttonauswahlmineral():
    global status1
    status1 ='fertig'
    root.destroy()
    return 

def Buttonauswahlfeucht():
    global status1
    status1 ='fertig'
    root.destroy()
    return 

def Buttonauswahltrocken():
    global status1
    status1 ='fertig'
    root.destroy()
    return 

def buttonKosten():
    number_rows=rationfenster.shape
    
    global Kosten, TS
    Kosten= [0] * number_rows[0]
    TS= [0] * number_rows[0]
    for x in range(number_rows[0]):
        Kosten[x] = entryKosten[x].get()
        TS[x] = entryTS[x].get()
        Kosten[x]=Kosten[x].replace(',','.')
        TS[x]=TS[x].replace(',','.')
        if Kosten[x]=='':
            Kosten[x]=0
        if TS[x]=='':
            TS[x]=rationfenster.iloc[x,4]
        try:
            Kosten[x]=float(Kosten[x])
        except ValueError: 
            messagebox.showerror("Error","Eingegebene Kosten können nicht verarbeitet werden")
            return
        try:
            TS[x]=float(TS[x])
        except ValueError: 
            messagebox.showerror("Error","Ein eingegebener TS-Gehalt kann nicht verarbeitet werden")
            return
    Tk.destroy(tkFenster)
    return

          

pd.read_csv = functools.partial(pd.read_csv, low_memory=False)    

# öffnen Startbildschirm
tkFenster = Tk()
tkFenster.title('Fütterungsprogramm')
tkFenster.geometry('600x450')    

os.chdir('/home/thomas/.config/spyder-py3/Projekt1/')
img = PhotoImage(file="agroprax.png")
canvas = Canvas(master=tkFenster, width=600, height=360)
canvas.pack()

canvas.create_image(12, 60, image=img, anchor='nw')
header = Label(master=tkFenster, text='Herzlich Willkommen beim Fütterungsprogramm der ', fg='black', bg='white', font='Arial 14 bold')
header.place(x=12, y=5, width=575, height=60)
header = Label(master=tkFenster, text='Soll eine neue Ration geschaffen\n oder eine alte aktualisiert werden?', fg='black', bg='white', font='Arial 14 bold')
header.place(x=12, y=360, width=575, height=60)

# Button
buttonneu = Button(master=tkFenster, text='neu', bg='#FFCFC9', font='Arial 12 bold', command=buttonneu)
buttonneu.place(x=5, y=420, width=100, height=30)
buttonaktualisieren = Button(master=tkFenster, text='aktualisieren', bg='#D5E88F',font='Arial 12 bold', command=buttonaktualisieren)
buttonaktualisieren.place(x=440, y=420, width=150, height=30)

tkFenster.mainloop()


if status == "neu":
    #Auswahl Query
    list_of_files = glob.glob('/home/thomas/.config/spyder-py3/Projekt1/queries/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    if  latest_file.endswith('.csv'):
        os.rename(latest_file, '/home/thomas/.config/spyder-py3/Projekt1/queries/latest_query.csv')
    else: 
        messagebox.showerror("Error","Keine aktuelle .csv Query-Datei im Ordner queries in vorhanden")
  
    os.chdir('/home/thomas/.config/spyder-py3/Projekt1/queries/')
    filename='latest_query.csv'
    Analysen = pd.read_csv(filename,encoding='latin-1')
    
    list1 = Analysen['Sampled For'].astype(str)
    autocompleteList=list(set(list1))
    
    
    
tkFenster = Tk()
tkFenster.title('Benenne die neue Ration')
tkFenster.geometry('450x160')

NameRation=Label(master=tkFenster, text= "Wie soll die neue Ration genannt werden?", font='Arial 12 bold')
NameRation.place(x=30, y=20)
EingabeRation = Entry(master=tkFenster, bg='white', width=56, x=10)
EingabeRation.place(x=30, y=50)
ButtonName=Button(master=tkFenster, text='ok',bg='#D5E88F',font='Arial 12 bold', command=ButtonName)
ButtonName.place(x=300, y=80, width=100, height=30)
ButtonAbbruch=Button(master=tkFenster, text='abbrechen',font='Arial 12 bold',bg='#FFCFC9', command=buttonabbrechen)
ButtonAbbruch.place(x=50, y=80, width=100, height=30)

tkFenster.mainloop()

emptyDataFrame = pd.DataFrame(columns=['Maske','Kosten ( € /dt )', 'kg Frischmasse', '% der Ration TS','Kationen','Anionen','Rohprotein','Grundfutter NDF','Reihenfolge', 'untere Lademenge', 'normale Lademenge', 'obere Lademenge'])        

if status=='beenden':
    exit()

#status='neu'
if status =='neu':
    tkFenster = Tk()
    tkFenster.title('Auswahl des Betriebes')
    tkFenster.geometry('520x250')
    
    Labelueberschrift=Label(master=tkFenster, text= "Die Analysen welcher Betriebe soll genutzt werden?", font='Arial 12 bold')
    Labelueberschrift.place(x=10, y=20)
    EingabeBetrieb = AutocompleteEntry(autocompleteList, tkFenster, listboxLength=12, width=70, x=10,  matchesFunction=matches)
    EingabeBetrieb.place(x=10, y=50)
    EingabeBetrieb1 = AutocompleteEntry(autocompleteList, tkFenster, listboxLength=12, width=70, x=10,  matchesFunction=matches)
    EingabeBetrieb1.place(x=10, y=90)
    EingabeBetrieb2 = AutocompleteEntry(autocompleteList, tkFenster, listboxLength=12, width=70, x=10,  matchesFunction=matches)
    EingabeBetrieb2.place(x=10, y=130)
     
    ButtonAuswahl=Button(master=tkFenster, text='auswählen',bg='#D5E88F',font='Arial 12 bold', command=buttonauswählen)
    ButtonAuswahl.place(x=400, y=150, width=100, height=30)
    ButtonAbbruch=Button(master=tkFenster, text='abbrechen',bg='#FFCFC9',font='Arial 12 bold', command=buttonabbrechen)
    ButtonAbbruch.place(x=10, y=150, width=100, height=30)
    
    tkFenster.mainloop()
    
    
    AnalysenBetrieb=Analysen.head(0)
    i=0
    for x in range(list1.size):
        if Betrieb==Analysen.iloc[x]['Sampled For']:
            AnalysenBetrieb=AnalysenBetrieb.append(Analysen.iloc[x])
        if Betrieb1==Analysen.iloc[x]['Sampled For']:
            AnalysenBetrieb=AnalysenBetrieb.append(Analysen.iloc[x])
        if Betrieb2==Analysen.iloc[x]['Sampled For']:
            AnalysenBetrieb=AnalysenBetrieb.append(Analysen.iloc[x])
            
        #Kennung	Komponente Bezeichnung	Kosten     	kg Frichmasse	 % der Ration in TS	TS in% 	MJ NEL	NDF	G NDF	ADF	Lignin	NSC	Stärke	Zucker	Roh- protein	lösl. Protein	Asche	Ca	P	Mg	K	Na	S	Kationen	Anionen
    AnalysenRation=pd.concat([emptyDataFrame['Maske'],AnalysenBetrieb["Sampled For"], AnalysenBetrieb["Product Type"],AnalysenBetrieb["Description 1"], AnalysenBetrieb["Date Processed"], emptyDataFrame['Kosten ( € /dt )'],
                             AnalysenBetrieb["Dry Matter"],AnalysenBetrieb["NEL OARDC"]/100*2.2/0.236, AnalysenBetrieb["aNDFom"],emptyDataFrame["Grundfutter NDF"], AnalysenBetrieb["uNDFom30"],AnalysenBetrieb["uNDFom120"],AnalysenBetrieb["uNDFom240"],AnalysenBetrieb["NFC"],
                             AnalysenBetrieb["Starch"],AnalysenBetrieb["IVSD7-o"],AnalysenBetrieb['Adjusted CP'], AnalysenBetrieb["Soluble Protein"],AnalysenBetrieb["Ammonia CP%DM"], AnalysenBetrieb["Ash"],AnalysenBetrieb["Ca"],AnalysenBetrieb["P"],
                             AnalysenBetrieb["Mg"],AnalysenBetrieb["Na"],AnalysenBetrieb["K"],AnalysenBetrieb["S"]], axis=1, ignore_index=False)

    AnalysenRation["Grundfutter NDF"]=AnalysenRation["aNDFom"]
    AnalysenRation, NAlist = reduce_mem_usage(AnalysenRation)
    AnalysenBetriebFenster=pd.concat([AnalysenBetrieb["Field Name"], AnalysenBetrieb["Date Processed"],AnalysenBetrieb["Sampled For"], AnalysenBetrieb["Product Type"],AnalysenBetrieb["Description 1"]], axis=1, ignore_index=False)
    number_rows=AnalysenBetriebFenster.shape
    for r in range(number_rows[0]):
        if AnalysenBetriebFenster.iloc[r,3]=='1':
            AnalysenBetriebFenster.iloc[r,3]='Heu'
        if AnalysenBetriebFenster.iloc[r,3]=='1A':
            AnalysenBetriebFenster.iloc[r,3]='Leguminosen Heu'
        if AnalysenBetriebFenster.iloc[r,3]=='1B':
            AnalysenBetriebFenster.iloc[r,3]='Grassheu'
        if AnalysenBetriebFenster.iloc[r,3]=='1C':
            AnalysenBetriebFenster.iloc[r,3]='gemischte Silage'
        if AnalysenBetriebFenster.iloc[r,3]=='1D':
            AnalysenBetriebFenster.iloc[r,3]='Leguminosen Silage'
        if AnalysenBetriebFenster.iloc[r,3]=='1E':
            AnalysenBetriebFenster.iloc[r,3]='Grasssilage'
        if AnalysenBetriebFenster.iloc[r,3]=='2':
            AnalysenBetriebFenster.iloc[r,3]='Maissilage' 
        if AnalysenBetriebFenster.iloc[r,3]=='3':
            AnalysenBetriebFenster.iloc[r,3]='Körnermais'
        if AnalysenBetriebFenster.iloc[r,3]=='4':
            AnalysenBetriebFenster.iloc[r,3]='Maiskolben'
        if AnalysenBetriebFenster.iloc[r,3]=='5':
            AnalysenBetriebFenster.iloc[r,3]='Getreide'
        if AnalysenBetriebFenster.iloc[r,3]=='6':
            AnalysenBetriebFenster.iloc[r,3]='Nebenprodukte Getreide'
        if AnalysenBetriebFenster.iloc[r,3]=='7':
            AnalysenBetriebFenster.iloc[r,3]='Getreide Silagen'
        if AnalysenBetriebFenster.iloc[r,3]=='8':
            AnalysenBetriebFenster.iloc[r,3]='Oelsamen und Nebenprodukte'
        if AnalysenBetriebFenster.iloc[r,3]=='9':
            AnalysenBetriebFenster.iloc[r,3]='TMR'
        if AnalysenBetriebFenster.iloc[r,3]=='10':
            AnalysenBetriebFenster.iloc[r,3]='sonstiges Futter'

    
    
    
    tkFenster = Tk()
    tkFenster.title('Auswahl Analysen')
    table=[]
    number_rows=AnalysenBetriebFenster.shape 
    for x in range(number_rows[0]):
        table.append('var_'+str(x))
        table[x]=IntVar()
    
    header = Label(master=tkFenster, text=' ', fg='gray85', bg='gray85', font='Arial 14 bold',width = 15, height = 2)
    header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
    Labelueberschrift=Label(master=tkFenster, text= "Welche Analysen sollen für die Ration " + str(NameRation) + " verwendet werden?", font='Arial 14 bold')
    Labelueberschrift.place(x=50, y=10)
    
    header = Label(master=tkFenster, text='ausgewählt', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
    header.grid(row=2, column=0, padx='1', pady='1', sticky='ew')
    header = Label(master=tkFenster, text='Datum', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
    header.grid(row=2, column=1, padx='1', pady='1', sticky='ew')
    header = Label(master=tkFenster, text='Kennung', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
    header.grid(row=2, column=2, padx='1', pady='1', sticky='ew')
    header = Label(master=tkFenster, text='Futter', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
    header.grid(row=2, column=3, padx='1', pady='1', sticky='ew')
    header = Label(master=tkFenster, text='Bezeichnung', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
    header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        
    for r in range(number_rows[0]):
        for c in range(number_rows[1]):
            if c == 0:
                checkbutton = Checkbutton(master=tkFenster, anchor='center',offvalue=0, onvalue=1, variable=table[r],height = 2)
                checkbutton.grid(row=r+3, column=c, padx='1', pady='1', sticky='ew')
            else:
                Kasten = Label(master=tkFenster, bg='white', text=AnalysenBetriebFenster.iloc[r,c],font='Arial 12 bold')
                Kasten.grid(row=r+3, column=c, padx='2', pady='2', sticky='ew')
        
    Buttonauswahlanalysen = Button(master=tkFenster, text='weiter', bg='#D5E88F',font='Arial 14 bold', command=Buttonauswahlanalysen)
    Buttonauswahlanalysen.grid(row=r+4, column=c, padx='5', pady='5', sticky='ew')
  
    tkFenster.mainloop()
    
    ration=AnalysenRation.head(0)
    for r in range(number_rows[0]):
        if table[r].get()==1:
            ration=ration.append(AnalysenRation.iloc[r], ignore_index = True)
                
    ration = ration.rename(columns={'Sampled For': 'Kennung', 'Product Type': 'Komponente','Description 1': 'Bezeichnung','Date Processed': 'Datum','Dry Matter': 'TS in %','NEL OARDC': 'MJ NEL','aNDFom': 'NDF','Starch': 'Staerke','IVSD7-o': 'Staerkeverdaulichkeit 7h','Soluble Protein': 'loesl. Protein', 'Adjusted CP': 'Rohprotein',
                                     'Ammonia CP%DM': 'Ammonium-Protein','Ash': 'Asche','Ca': 'Kalzium','P': 'Phosphor','Mg': 'Magnesium','K':'Kalium','Na':'Natrium','uNDFom30': 'uNDF30','uNDFom120': 'uNDF120','uNDFom240': 'uNDF240', 'S':'Schwefel'})
    
    ration["Bezeichnung"]=ration["Bezeichnung"].fillna("-")
    ration=ration.fillna(0)

    ration["Grundfutter NDF"] = ration["Grundfutter NDF"]/100
    ration["NDF"] = ration["Grundfutter NDF"]
    ration["uNDF30"] = ration["uNDF30"]/100
    ration["uNDF120"] = ration["uNDF120"]/100
    ration["uNDF240"] = ration["uNDF240"]/100
    ration["NFC"] = ration["NFC"]/100
    ration["Staerke"] = ration["Staerke"]/100
    ration["Staerkeverdaulichkeit 7h"] = ration["Staerkeverdaulichkeit 7h"]/100
    ration["Rohprotein"] = ration["Rohprotein"]/100
    ration["Asche"] = ration["Asche"]/100
    ration["Kalzium"] = ration["Kalzium"]/100
    ration["Phosphor"] = ration["Phosphor"]/100
    ration["Magnesium"] = ration["Magnesium"]/100
    ration["Natrium"] = ration["Natrium"]/100
    ration["Kalium"] = ration["Kalium"]/100
    ration["Schwefel"] = ration["Schwefel"]/100
    ration["loesl. Protein"] = ration["loesl. Protein"]/100
    ration["Ammonium-Protein"] = ration["Ammonium-Protein"]/100
    
    
    for y in range(3):           
        os.chdir('/home/thomas/.config/spyder-py3/Projekt1/Komponenten/')
        if y==0:
            filename='Mineralfutter.csv'
        if y==1:
            filename='feuchte Komponenten.csv'    
        if y==2:
            filename='trockene Komponenten.csv'    
        Komponenten = pd.read_csv(filename,encoding='latin-1')
        
        KomponentenFenster=pd.concat([Komponenten["Maske"], Komponenten["Kennung"], Komponenten["Komponente"],Komponenten["Bezeichnung"]], axis=1, ignore_index=False)
        KomponentenFenster=KomponentenFenster.fillna("-")
        root = Tk()
        if y==0:
            root.title("Auswahl Mineralfutter")
        if y==1:
            root.title("Auswahl feuchte Komponenten")    
        if y==2:
            root.title("Auswahl trockene Komponenten") 
        #root.geometry('1000x700')
        table=[]   
        root.grid_rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        frame_main = Frame(root,  bg="gray85")
        frame_main.grid(sticky='news')
        
        frame_header = Frame(frame_main)
        frame_header.grid(row=0, column=0, pady=(5, 0), sticky='nw')
        frame_header.grid_rowconfigure(0, weight=1)
        frame_header.grid_columnconfigure(0, weight=1)
        #
        canvas = Canvas(frame_header,width=1000, height=20, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
    
        frame_canvas = Frame(frame_main)
        frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        
        # Add a canvas in that frame
        canvas = Canvas(frame_canvas,width=1000, height=700, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
        
        # Link a scrollbar to the canvas
        vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)
        
    #    hsbar = Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
    #    hsbar.grid(row=1, column=0, sticky="EW")
    #    canvas.configure(xscrollcommand=hsbar.set)
        Labelueberschrift=Label(master=frame_header, text= "Welche Analysen sollen für die Ration " + str(NameRation) + " verwendet werden?", font='Arial 14 bold')
        Labelueberschrift.grid(row=0, column=0) 
        
        # Create a frame to contain the labels
        frame_labels = Frame(canvas, bg="gray85")
        canvas.create_window((0, 0), window=frame_labels, anchor='nw')
        header = Label(master=frame_labels, text='ausgewählt', fg='black', bg='white', font=('Arial 14 bold'),width = 12, height = 2,)
        header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Kennung', fg='black', bg='white', font=('Arial 14 bold'),width = 12, height = 2,)
        header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Futter', fg='black', bg='white', font=('Arial 14 bold'),width = 15, height = 2,)
        header.grid(row=0, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Bezeichnung', fg='black', bg='white', font=('Arial 14 bold'),width = 15, height = 2,)
        header.grid(row=0, column=3, padx='1', pady='1', sticky='ew')
        
        number_rows=KomponentenFenster.shape 
        for x in range(number_rows[0]):
            table.append('var_'+str(x))
            table[x]=IntVar()
            
        checkbutton=[Checkbutton() for r in range(number_rows[0])]  
        Kasten=[[Label() for c in range(number_rows[1])] for r in range(number_rows[0])] 
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c == 0:
                    checkbutton[r] = Checkbutton(master=frame_labels, anchor='center',offvalue=0, onvalue=1, variable=table[r],height = 2,)
                    checkbutton[r].grid(row=r+2, column=c, padx='1', pady='1', sticky='ew')
                else:
                    Kasten[r][c] = Label(master=frame_labels, bg='white', text=KomponentenFenster.iloc[r,c],font=('Arial 12 bold'))
                    Kasten[r][c].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
        
        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        frame_labels.update_idletasks()
        
        # Resize the canvas frame to show exactly 5-by-10 labels and the scrollbar
        first5columns_width = sum([Kasten[r][0].winfo_width() for r in range(0, 10)])
        first5rows_height = sum([Kasten[0][c].winfo_height() for c in range(0, 4)])
        frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                            height=first5rows_height)
        
        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))
            
           
        
        frame_button = Frame(frame_main)
        frame_button.grid(row=4, column=0, pady=(0), sticky='nw')
        frame_button.grid_rowconfigure(0, weight=1)
        frame_button.grid_columnconfigure(0, weight=1)
        #
        canvas = Canvas(frame_button,width=550, height=5, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
        if y==0:
            Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F',font='Arial 12 bold', command=Buttonauswahlmineral)
        if y==1:
            Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F',font='Arial 12 bold', command=Buttonauswahlfeucht)    
        if y==2:
            Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F',font='Arial 12 bold', command=Buttonauswahltrocken) 
                                           
        Buttonauswahlanalysen.grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')

    
        root.mainloop()     
        
                
        for r in range(number_rows[0]):
            if table[r].get()==1:
                ration=ration.append(Komponenten.iloc[r])
                
    ration["Bezeichnung"]=ration["Bezeichnung"].fillna("-")
    ration=ration.fillna(0)


if status=='aktualisieren':
    root = Tk()
    filename = filedialog.askopenfilename(initialdir = "/home/thomas/.config/spyder-py3/Projekt1/Gespeicherte Rationen",title = "Select file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))


    root.mainloop()
    
    xls = pd.ExcelFile(filename)
    ration = pd.read_excel(xls, 'Analysen')
    ration_hochleistend = pd.read_excel(xls, 'Ration_hochleistend')
    ration_frischmelker = pd.read_excel(xls, 'Ration_frischmelkend')
    ration_altmelker = pd.read_excel(xls, 'Ration_altmelkend')
    ration_trockensteher = pd.read_excel(xls, 'Ration_trockenstehend')
    ration_rinder = pd.read_excel(xls, 'Ration_Rinder')
    ration_bullen = pd.read_excel(xls, 'Ration_Bullen')
    
    ration = ration.set_index('index')
    ration_hochleistend = ration_hochleistend.set_index('index')
    ration_frischmelker = ration_frischmelker.set_index('index')
    ration_altmelker = ration_altmelker.set_index('index')
    ration_trockensteher = ration_trockensteher.set_index('index')
    ration_rinder = ration_rinder.set_index('index')
    ration_bullen = ration_bullen.set_index('index')
    

try:
    ration=ration.drop(["Maske"],axis=1)
except:
    print('a')

ration.dropna(axis=1, how='all', thresh=None, subset=None, inplace=True)    
ration, NAlist = reduce_mem_usage(ration)

number_rows=ration.shape
for r in range(number_rows[0]):
    if ration.iloc[r,1]=='1':
        ration.iloc[r,1]='Heu'
    if ration.iloc[r,1]=='1A':
        ration.iloc[r,1]='Leguminosen Heu'
    if ration.iloc[r,1]=='1B':
        ration.iloc[r,1]='Grassheu'
    if ration.iloc[r,1]=='1C':
        ration.iloc[r,1]='gemischte Silage'
    if ration.iloc[r,1]=='1D':
        ration.iloc[r,1]='Leguminosen Silage'
    if ration.iloc[r,1]=='1E':
        ration.iloc[r,1]='Grasssilage'
    if ration.iloc[r,1]=='2':
        ration.iloc[r,1]='Maissilage' 
    if ration.iloc[r,1]=='3':
        ration.iloc[r,1]='Körnermais'
    if ration.iloc[r,1]=='4':
        ration.iloc[r,1]='Maiskolben'
    if ration.iloc[r,1]=='5':
        ration.iloc[r,1]='Getreide'
    if ration.iloc[r,1]=='6':
        ration.iloc[r,1]='Nebenprodukte Getreide'
    if ration.iloc[r,1]=='7':
        ration.iloc[r,1]='Getreide Silagen'
    if ration.iloc[r,1]=='8':
        ration.iloc[r,1]='Oelsamen und Nebenprodukte'
    if ration.iloc[r,1]=='9':
        ration.iloc[r,1]='TMR'
    if ration.iloc[r,1]=='10':
        ration.iloc[r,1]='sonstiges Futter' 
        
print(ration)
# Kosten und TS eingeben
rationfenster=pd.concat([ration["Kennung"], ration["Komponente"],ration["Bezeichnung"],ration['Datum'],ration['Kosten ( € /dt )'],ration['TS in %']], axis=1, ignore_index=False)

number_rows=rationfenster.shape 

entryKosten=[0] * number_rows[0]
entryTS=[0] * number_rows[0]

rationfenster['Kosten ( € /dt )']=rationfenster['Kosten ( € /dt )'].fillna(0)
rationfenster['Bezeichnung']=rationfenster['Bezeichnung'].fillna("-")
number_rows=ration.shape



tkFenster = Tk()
tkFenster.title("Eintragen der Kosten und aktualisieren der TS")
#header = Label(master=tkFenster, text='Gib den Preis ein und aktualisiere gegebenenfalls die TS-Werte', fg='black', bg='white', font=('Arial'),width = 12, height = 2,)
#header.grid(row=0, sticky="news")
c=0
for col in rationfenster.columns: 
    Kasten = Label(master=tkFenster, bg='white', text=col, font=('Arial 14 bold'),width = 5, height = 2)
    Kasten.grid(row=1, column=c, padx='1', pady='1', sticky='ew')
    c=c+1

for r in range(number_rows[0]):
    for c in range(number_rows[1]):
        if c<4:
            Kasten = Label(master=tkFenster, bg='white', text=rationfenster.iloc[r,c],font='Arial 12 bold')
            Kasten.grid(row=r+2, column=c, padx='3', pady='3', sticky='ew')
        if c==4:
           entryKosten[r] = Entry(master=tkFenster, bg='white')
           entryKosten[r].config(font='Arial 12 bold',width=20)
           entryKosten[r].grid(row=r+2, column=c, padx='3', pady='3', sticky='ew')
           entryKosten[r].insert(0,rationfenster.iloc[r,c])
            
        if c==5:
            entryTS[r] = Entry(master=tkFenster, bg='white')
            entryTS[r].config(font='Arial 12 bold',width=10)
            entryTS[r].grid(row=r+2, column=c, padx='3', pady='3', sticky='ew')
            entryTS[r].insert(0,rationfenster.iloc[r,c])

asd=number_rows[0]
buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='weiter',font='Arial 12 bold', command=buttonKosten)
buttonBerechnen.grid(row=r+3, column=c, padx='5', pady='5', sticky='ew')

tkFenster.mainloop()

ration["TS in %"]=TS
ration['Kosten ( € /dt )']=Kosten

def Gruppenweiter():
    tkFenster.destroy()
    return 

Gruppen=[]
Gruppen=['Hochleistende Kuehe', 'Frischmelker','Altmelker','Trockensteher', 'Rinder','Bullen',] 

table1=[]
tkFenster = Tk()
tkFenster.title("Auswahl der Gruppen")
for x in range(len(Gruppen)):
        table1.append('var_'+str(x))
        table1[x]=IntVar()
        
header = Label(master=tkFenster, text=' ', fg='gray85', bg='gray85', font='Arial 2 bold',width = 15, height = 2)
header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
header = Label(master=tkFenster, text='ausgewählt', fg='black', bg='white', font=('Arial 14 bold'))
header.grid(row=1, column=0, padx='3', pady='3', sticky='ew')
header = Label(master=tkFenster, text='Gruppenname', fg='black', bg='white', font=('Arial 14 bold'))
header.grid(row=1, column=1, padx='3', pady='3', sticky='ew')

        
checkbutton=[Checkbutton() for r in range(len(Gruppen))]  
Kasten=[Label() for r in range(len(Gruppen))] 
for r in range(len(Gruppen)):
        checkbutton[r] = Checkbutton(master=tkFenster, anchor='center',offvalue=0, onvalue=1, variable=table1[r],height = 2)
        checkbutton[r].grid(row=r+2, column=0, padx='1', pady='1', sticky='ew')
        Kasten[r] = Label(master=tkFenster, bg='white', text=Gruppen[r],font='Arial 12 bold')
        Kasten[r].grid(row=r+2, column=1, padx='7', pady='3', sticky='ew')
        
Buttonauswahlanalysen = Button(master=tkFenster, text='weiter', bg='#D5E88F',font='Arial 12 bold', command=Gruppenweiter)                 
Buttonauswahlanalysen.grid(row=r+3, column=1, padx='5', pady='5', sticky='ew')
       
tkFenster.mainloop()
  

L=[]
L=['Kosten', 'kg Frischmasse','% der Ration TS','TS', 'MJ NEL', 'NDF','uNDF30','uNDF120','uNDF240', 'GNDF', 'NFC', 'Staerke','Staerkeverdaulichkeit 7h', 'Rohprotein', 'loesl. Protein','Ammonium-Protein', 'Asche' , 'Kalzium', 'Phosphor', 'Magnesium', 'Kalium', 'Natrium', 'Schwefel']        
ration_ziel=pd.concat([emptyDataFrame['Reihenfolge'],ration['Kennung'],ration['Komponente'],ration['Bezeichnung'],ration['Datum']], axis=1, ignore_index=False)
      
for col in L:
    ration_ziel[col] = 0
    
ration_ziel['Reihenfolge']=ration_ziel['Reihenfolge'].fillna(0)
ration_ziel=ration_ziel.fillna("-")
    
if status=='neu':
    L=[]
    L=['Kosten', 'kg Frischmasse','% der Ration TS','TS', 'MJ NEL', 'NDF','uNDF30','uNDF120','uNDF240', 'GNDF', 'NFC', 'Staerke','Staerkeverdaulichkeit 7h', 'Rohprotein', 'loesl. Protein','Ammonium-Protein', 'Asche' , 'Kalzium', 'Phosphor', 'Magnesium', 'Kalium', 'Natrium', 'Schwefel']    
    ration_bullen=pd.concat([emptyDataFrame['Reihenfolge'],ration['Kennung'],ration['Komponente'],ration['Bezeichnung'],ration['Datum']], axis=1, ignore_index=False)
    ration_rinder=pd.concat([emptyDataFrame['Reihenfolge'],ration['Kennung'],ration['Komponente'],ration['Bezeichnung'],ration['Datum']], axis=1, ignore_index=False)
    ration_trockensteher=pd.concat([emptyDataFrame['Reihenfolge'],ration['Kennung'],ration['Komponente'],ration['Bezeichnung'],ration['Datum']], axis=1, ignore_index=False)
    ration_altmelker=pd.concat([emptyDataFrame['Reihenfolge'],ration['Kennung'],ration['Komponente'],ration['Bezeichnung'],ration['Datum']], axis=1, ignore_index=False)
    ration_frischmelker=pd.concat([emptyDataFrame['Reihenfolge'],ration['Kennung'],ration['Komponente'],ration['Bezeichnung'],ration['Datum']], axis=1, ignore_index=False)
    ration_hochleistend=pd.concat([emptyDataFrame['Reihenfolge'],ration['Kennung'],ration['Komponente'],ration['Bezeichnung'],ration['Datum']], axis=1, ignore_index=False)
    
    mischung_bullen=pd.concat([emptyDataFrame['Reihenfolge'],ration['Komponente'],ration['Bezeichnung'],emptyDataFrame['kg Frischmasse'],emptyDataFrame['untere Lademenge'],emptyDataFrame['normale Lademenge'],emptyDataFrame['obere Lademenge']], axis=1, ignore_index=False)
    mischung_rinder=pd.concat([emptyDataFrame['Reihenfolge'],ration['Komponente'],ration['Bezeichnung'],emptyDataFrame['kg Frischmasse'],emptyDataFrame['untere Lademenge'],emptyDataFrame['normale Lademenge'],emptyDataFrame['obere Lademenge']], axis=1, ignore_index=False)
    mischung_trockensteher=pd.concat([emptyDataFrame['Reihenfolge'],ration['Komponente'],ration['Bezeichnung'],emptyDataFrame['kg Frischmasse'],emptyDataFrame['untere Lademenge'],emptyDataFrame['normale Lademenge'],emptyDataFrame['obere Lademenge']], axis=1, ignore_index=False)
    mischung_altmelker=pd.concat([emptyDataFrame['Reihenfolge'],ration['Komponente'],ration['Bezeichnung'],emptyDataFrame['kg Frischmasse'],emptyDataFrame['untere Lademenge'],emptyDataFrame['normale Lademenge'],emptyDataFrame['obere Lademenge']], axis=1, ignore_index=False)
    mischung_frischmelker=pd.concat([emptyDataFrame['Reihenfolge'],ration['Komponente'],ration['Bezeichnung'],emptyDataFrame['kg Frischmasse'],emptyDataFrame['untere Lademenge'],emptyDataFrame['normale Lademenge'],emptyDataFrame['obere Lademenge']], axis=1, ignore_index=False)
    mischung_hochleistend=pd.concat([emptyDataFrame['Reihenfolge'],ration['Komponente'],ration['Bezeichnung'],emptyDataFrame['kg Frischmasse'],emptyDataFrame['untere Lademenge'],emptyDataFrame['normale Lademenge'],emptyDataFrame['obere Lademenge']], axis=1, ignore_index=False)
    for col in L:
        ration_bullen[col] = 0
        ration_rinder[col] = 0
        ration_trockensteher[col] = 0
        ration_altmelker[col] = 0
        ration_frischmelker[col] = 0
        ration_hochleistend[col] = 0
        
    ration_ziel.reset_index(drop=True, inplace=True)
    ration_bullen.reset_index(drop=True, inplace=True)
    ration_rinder.reset_index(drop=True, inplace=True)
    ration_trockensteher.reset_index(drop=True, inplace=True)
    ration_altmelker.reset_index(drop=True, inplace=True)
    ration_frischmelker.reset_index(drop=True, inplace=True)
    ration_hochleistend.reset_index(drop=True, inplace=True)
    ration.reset_index(drop=True, inplace=True)
    
    ration_bullen['Reihenfolge']=ration_bullen['Reihenfolge'].fillna(0)
    ration_bullen=ration_bullen.fillna("-")
    ration_rinder['Reihenfolge']=ration_rinder['Reihenfolge'].fillna(0)
    ration_rinder=ration_rinder.fillna("-")
    ration_trockensteher['Reihenfolge']=ration_trockensteher['Reihenfolge'].fillna(0)
    ration_trockensteher=ration_trockensteher.fillna("-")
    ration_altmelker['Reihenfolge']=ration_altmelker['Reihenfolge'].fillna(0)
    ration_altmelker=ration_altmelker.fillna("-")
    ration_frischmelker['Reihenfolge']=ration_frischmelker['Reihenfolge'].fillna(0)
    ration_frischmelker=ration_frischmelker.fillna("-")
    ration_hochleistend['Reihenfolge']=ration_hochleistend['Reihenfolge'].fillna(0)
    ration_hochleistend=ration_hochleistend.fillna("-")
    
    mischung_bullen.reset_index(drop=True, inplace=True)
    mischung_rinder.reset_index(drop=True, inplace=True)
    mischung_trockensteher.reset_index(drop=True, inplace=True)
    mischung_altmelker.reset_index(drop=True, inplace=True)
    mischung_frischmelker.reset_index(drop=True, inplace=True)
    mischung_hochleistend.reset_index(drop=True, inplace=True)
    
    mischung_bullen['Bezeichnung']=mischung_bullen['Bezeichnung'].fillna("-")
    mischung_bullen=mischung_bullen.fillna(0)
    mischung_rinder['Bezeichnung']=mischung_rinder['Bezeichnung'].fillna("-")
    mischung_rinder=mischung_rinder.fillna(0)
    mischung_trockensteher['Bezeichnung']=mischung_trockensteher['Bezeichnung'].fillna("-")
    mischung_trockensteher=mischung_trockensteher.fillna(0)
    mischung_altmelker['Bezeichnung']=mischung_altmelker['Bezeichnung'].fillna("-")
    mischung_altmelker=mischung_altmelker.fillna(0)
    mischung_frischmelker['Bezeichnung']=mischung_frischmelker['Bezeichnung'].fillna("-")
    mischung_frischmelker=mischung_frischmelker.fillna(0)
    mischung_hochleistend['Bezeichnung']=mischung_hochleistend['Bezeichnung'].fillna("-")
    mischung_hochleistend=mischung_hochleistend.fillna(0)
    
    Anzahl_hochleistend=0
    Varianz_hochleistend=0
    Anzahl_frischmelker=0
    Varianz_frischmelker=0
    Anzahl_altmelker=0
    Varianz_altmelker=0
    Anzahl_trockensteher=0
    Varianz_trockensteher=0
    Anzahl_rinder=0
    Varianz_rinder=0
    Anzahl_bullen=0
    Varianz_bullen=0


ration['Bezeichnung']=ration['Bezeichnung'].fillna("-")
ration=ration.fillna(0)
number_rows=ration.shape
for r in range(number_rows[0]):
    if ration.iloc[r,1]=='1':
        ration.iloc[r,1]='Heu'
    if ration.iloc[r,1]=='1A':
        ration.iloc[r,1]='Leguminosen Heu'
    if ration.iloc[r,1]=='1B':
        ration.iloc[r,1]='Grassheu'
    if ration.iloc[r,1]=='1C':
        ration.iloc[r,1]='gemischte Silage'
    if ration.iloc[r,1]=='1D':
        ration.iloc[r,1]='Leguminosen Silage'
    if ration.iloc[r,1]=='1E':
        ration.iloc[r,1]='Grasssilage'
    if ration.iloc[r,1]=='2':
        ration.iloc[r,1]='Maissilage' 
    if ration.iloc[r,1]=='3':
        ration.iloc[r,1]='Körnermais'
    if ration.iloc[r,1]=='4':
        ration.iloc[r,1]='Maiskolben'
    if ration.iloc[r,1]=='5':
        ration.iloc[r,1]='Getreide'
    if ration.iloc[r,1]=='6':
        ration.iloc[r,1]='Nebenprodukte Getreide'
    if ration.iloc[r,1]=='7':
        ration.iloc[r,1]='Getreide Silagen'
    if ration.iloc[r,1]=='8':
        ration.iloc[r,1]='Oelsamen und Nebenprodukte'
    if ration.iloc[r,1]=='9':
        ration.iloc[r,1]='TMR'
    if ration.iloc[r,1]=='10':
        ration.iloc[r,1]='sonstiges Futter'

status=1
while status!='weiter': 
    
    def buttonBeenden():
        global status
        status='weiter'
        Tk.destroy(parent)
#        quit()
        return 
    
    def button_Kosten_ration():
        number_rows=ration_append.shape
        
        global Kosten, TS
        Kosten= [0] * number_rows[0]
        TS= [0] * number_rows[0]
        for x in range(number_rows[0]):
            Kosten[x] = entryKosten[x].get()
            TS[x] = entryTS[x].get()
            Kosten[x]=Kosten[x].replace(',','.')
            TS[x]=TS[x].replace(',','.')
            if Kosten[x]=='':
                Kosten[x]=0
            if TS[x]=='':
                TS[x]=ration.iloc[x,5]
            try:
                Kosten[x]=float(Kosten[x])
            except ValueError: 
                messagebox.showerror("Error","Eingegebene Kosten können nicht verarbeitet werden")
                return
            try:
                TS[x]=float(TS[x])
            except ValueError: 
                messagebox.showerror("Error","Ein eingegebener TS-Gehalt kann nicht verarbeitet werden")
                return
        Tk.destroy(tkFenster)
        return  

    def buttonMineral():
        parent.destroy()
        global status
        status='mineral'
        return
    
    def buttonFeucht():
        Tk.destroy(parent)
        global status
        status='feucht'
        return
    
    def buttonTrocken():
        parent.destroy()
        global status
        status='trocken'
        return
    
    def button_Kosten():
        parent.destroy()
        global status
        status='Kosten'
        return
    
    def buttonGruppen():
        parent.destroy()
        global status
        status='Gruppen'
        return
    
    def buttonAnalysen():
        parent.destroy()
        global status
        status='Analysen'
        return
    
    def buttonKomponenten():
        parent.destroy()
        global status
        status='Komponenten'
        return
                    
    def  button_hochleistend_menge():
        for row in Kasten_hochleistend:
                row.destroy()  

        for i in entryRf_hochleistend:
            i.destroy()    
           
        for i in entryFM_hochleistend:
            i.destroy()    

        global ration_hochleistend
        
        ration_hochleistend=ration_hochleistend.sort_values(by=['kg Frischmasse'], ascending=False)


        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_hochleistend[r] = Entry(master=tkFenster1, bg='white')
                    entryFM_hochleistend[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_hochleistend[r].insert(0,ration_hochleistend.iloc[r,c])
                    continue
                if c==0:
                    entryRf_hochleistend[r] = Entry(master=tkFenster1, bg='white')
                    entryRf_hochleistend[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_hochleistend[r].insert(0,ration_hochleistend.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=tkFenster1, bg='white', text=round(ration_hochleistend.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_hochleistend.append(Kasten)
                else:
                    Kasten = Label(master=tkFenster1, bg='white', text=ration_hochleistend.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_hochleistend.append(Kasten)
                    
        return
                    
    def button_frischmelker_menge():
        for row in Kasten_frischmelker:
            row.destroy() 
        
        for i in entryRf_frischmelker:
            i.destroy() 
        for i in entryFM_frischmelker:
            i.destroy() 
        
        global ration_frischmelker
        ration_frischmelker=ration_frischmelker.sort_values(by=['kg Frischmasse'], ascending=False)

        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_frischmelker[r] = Entry(master=Fenster_frisch1, bg='white')
                    entryFM_frischmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_frischmelker[r].insert(0,ration_frischmelker.iloc[r,c])
                    continue
                if c==0:
                    entryRf_frischmelker[r] = Entry(master=Fenster_frisch1, bg='white')
                    entryRf_frischmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_frischmelker[r].insert(0,ration_frischmelker.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=Fenster_frisch1, bg='white', text=round(ration_frischmelker.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_frischmelker.append(Kasten)
                else:
                    Kasten = Label(master=Fenster_frisch1, bg='white', text=ration_frischmelker.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_frischmelker.append(Kasten)
        return                
                        
    def  button_altmelker_menge():
        for row in Kasten_altmelker:
                row.destroy()  

        for i in entryRf_altmelker:
            i.destroy()    
           
        for i in entryFM_altmelker:
            i.destroy()    

        global ration_altmelker
        
        ration_altmelker=ration_altmelker.sort_values(by=['kg Frischmasse'], ascending=False)
        
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_altmelker[r] = Entry(master=Fenster_alt1, bg='white')
                    entryFM_altmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_altmelker[r].insert(0,ration_altmelker.iloc[r,c])
                    continue
                if c==0:
                    entryRf_altmelker[r] = Entry(master=Fenster_alt1, bg='white')
                    entryRf_altmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_altmelker[r].insert(0,ration_altmelker.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=Fenster_alt1, bg='white', text=round(ration_altmelker.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_altmelker.append(Kasten)
                else:
                    Kasten = Label(master=Fenster_alt1, bg='white', text=ration_altmelker.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_altmelker.append(Kasten)
                    
        return
    
    def  button_trockensteher_menge():
        for row in Kasten_trockensteher:
                row.destroy()  

        for i in entryRf_trockensteher:
            i.destroy()    
           
        for i in entryFM_trockensteher:
            i.destroy()    

        global ration_trockensteher
        
        ration_trockensteher=ration_trockensteher.sort_values(by=['kg Frischmasse'], ascending=False)
        
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_trockensteher[r] = Entry(master=Fenster_trocken1, bg='white')
                    entryFM_trockensteher[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_trockensteher[r].insert(0,ration_trockensteher.iloc[r,c])
                    continue
                if c==0:
                    entryRf_trockensteher[r] = Entry(master=Fenster_trocken1, bg='white')
                    entryRf_trockensteher[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_trockensteher[r].insert(0,ration_trockensteher.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=Fenster_trocken1, bg='white', text=round(ration_trockensteher.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_trockensteher.append(Kasten)
                else:
                    Kasten = Label(master=Fenster_trocken1, bg='white', text=ration_trockensteher.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_trockensteher.append(Kasten)
                    
        return

    def  button_rinder_menge():
        for row in Kasten_rinder:
                row.destroy()  

        for i in entryRf_rinder:
            i.destroy()    
           
        for i in entryFM_rinder:
            i.destroy()    

        global ration_rinder
        
        ration_rinder=ration_rinder.sort_values(by=['kg Frischmasse'], ascending=False)
        
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_rinder[r] = Entry(master=Fenster_rinder1, bg='white')
                    entryFM_rinder[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_rinder[r].insert(0,ration_rinder.iloc[r,c])
                    continue
                if c==0:
                    entryRf_rinder[r] = Entry(master=Fenster_rinder1, bg='white')
                    entryRf_rinder[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_rinder[r].insert(0,ration_rinder.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=Fenster_rinder1, bg='white', text=round(ration_rinder.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_rinder.append(Kasten)
                else:
                    Kasten = Label(master=Fenster_rinder1, bg='white', text=ration_rinder.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_rinder.append(Kasten)
                    
        return
    
    def  button_bullen_menge():
        for row in Kasten_bullen:
                row.destroy()  

        for i in entryRf_bullen:
            i.destroy()    
           
        for i in entryFM_bullen:
            i.destroy()    

        global ration_bullen
        
        ration_bullen=ration_bullen.sort_values(by=['kg Frischmasse'], ascending=False)
        
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_bullen[r] = Entry(master=Fenster_bullen1, bg='white')
                    entryFM_bullen[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_bullen[r].insert(0,ration_bullen.iloc[r,c])
                    continue
                if c==0:
                    entryRf_bullen[r] = Entry(master=Fenster_bullen1, bg='white')
                    entryRf_bullen[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_bullen[r].insert(0,ration_bullen.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=Fenster_bullen1, bg='white', text=round(ration_rinder.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_rinder.append(Kasten)
                else:
                    Kasten = Label(master=Fenster_bullen1, bg='white', text=ration_bullen.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_bullen.append(Kasten)
                    
        return
    
   
    def button_hochleistend_berechnen():

        global ration_hochleistend, Futterreste_hochleistend, Milchmenge_hochleistend,Milchpreis_hochleistend

        asd=ration_hochleistend.shape
        FM= [0] * asd[0]
        Rf= [1] * asd[0]
        for x in range(asd[0]):
            FM[x] = entryFM_hochleistend[x].get()
            Rf[x] = entryRf_hochleistend[x].get()
            FM[x]=FM[x].replace(',','.')
            Rf[x]=Rf[x].replace(',','.')
        
        for x in range(asd[0]):
            if FM[x]=='':
                FM[x]=0
                
            else:
                try:
                    FM[x]=float(FM[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Frischmasse ist keine Zahl")
                    return
            
            if Rf[x]=='':
                Rf[x]=0
                
            else:
                try:
                    Rf[x]=float(Rf[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Reihenfolge ist keine Zahl")
                    return
                
        ration_hochleistend['kg Frischmasse']=FM
        ration_hochleistend['Reihenfolge']=Rf
        ration_hochleistend['TS']=ration_hochleistend['kg Frischmasse'].mul(ration['TS in %'])/100
        ration_hochleistend['Kosten']= ration_hochleistend['kg Frischmasse'].mul(ration['Kosten ( € /dt )'])/100
        TS=ration_hochleistend["TS"].sum(axis = 0, skipna = True)
        ration_hochleistend['% der Ration TS']= ration_hochleistend['TS']/TS*100 
        ration_hochleistend['MJ NEL']=ration_hochleistend['TS'].mul(ration['MJ NEL'])
        ration_hochleistend['NDF']=ration_hochleistend['TS'].mul(ration['NDF']) 
        ration_hochleistend['uNDF30']=ration_hochleistend['TS'].mul(ration['uNDF30'])
        ration_hochleistend['uNDF120']=ration_hochleistend['TS'].mul(ration['uNDF120'])
        ration_hochleistend['uNDF240']=ration_hochleistend['TS'].mul(ration['uNDF240'])
        ration_hochleistend['GNDF']=ration_hochleistend['TS'].mul(ration['Grundfutter NDF'])
        ration_hochleistend['NFC']=ration_hochleistend['TS'].mul(ration['NFC'])
        ration_hochleistend['Staerke']=ration_hochleistend['TS'].mul(ration['Staerke'])
        ration_hochleistend['Staerkeverdaulichkeit 7h']=ration_hochleistend['TS'].mul(ration['Staerkeverdaulichkeit 7h'])        
        ration_hochleistend['NDF']=ration_hochleistend['TS'].mul(ration['NDF'])
        ration_hochleistend['Rohprotein']=ration_hochleistend['TS'].mul(ration['Rohprotein'])
        ration_hochleistend['loesl. Protein']=ration_hochleistend['TS'].mul(ration['loesl. Protein'])
        ration_hochleistend['Ammonium-Protein']=ration_hochleistend['TS'].mul(ration['Ammonium-Protein'])
        ration_hochleistend['Asche']=ration_hochleistend['TS'].mul(ration['Asche'])
        ration_hochleistend['Kalzium']=ration_hochleistend['TS'].mul(ration['Kalzium'])
        ration_hochleistend['Phosphor']=ration_hochleistend['TS'].mul(ration['Phosphor'])
        ration_hochleistend['Magnesium']=ration_hochleistend['TS'].mul(ration['Magnesium'])
        ration_hochleistend['Kalium']=ration_hochleistend['TS'].mul(ration['Kalium'])
        ration_hochleistend['Natrium']=ration_hochleistend['TS'].mul(ration['Natrium'])
        ration_hochleistend['Schwefel']=ration_hochleistend['TS'].mul(ration['Schwefel'])
#        ration_hochleistend['Kationen']=ration_hochleistend['TS'].mul(ration['Kationen'])
#        ration_hochleistend['Anionen']=ration_hochleistend['TS'].mul(ration['Anionen'])
#        ration_hochleistend['Zucker']=ration_hochleistend['TS'].mul(ration['Zucker'])
        
        Frischmasse=ration_hochleistend["kg Frischmasse"].sum(axis = 0, skipna = True)
        if Frischmasse ==0:
            messagebox.showerror("Error",'Frischmasse ist 0')
            return
    
        TS=ration_hochleistend["TS"].sum(axis = 0, skipna = True)
        MJNEL=ration_hochleistend["MJ NEL"].sum(axis = 0, skipna = True)
        PTS=TS/Frischmasse*100
        MJNEL=ration_hochleistend["MJ NEL"].sum(axis = 0, skipna = True)
        MJNELkg=MJNEL/TS
    
        NDF=ration_hochleistend["NDF"].sum(axis = 0, skipna = True)/TS*100
        GNDF=ration_hochleistend["GNDF"].sum(axis = 0, skipna = True)/TS*100
        NFC=ration_hochleistend["NFC"].sum(axis = 0, skipna = True)/TS*100
        RP=ration_hochleistend["Rohprotein"].sum(axis = 0, skipna = True)/TS*100
        Staerke=ration_hochleistend["Staerke"].sum(axis = 0, skipna = True)/TS*100
        
        Asche=ration_hochleistend["Asche"].sum(axis = 0, skipna = True)/TS*100
        Ca=ration_hochleistend["Kalzium"].sum(axis = 0, skipna = True)/TS*100
        P=ration_hochleistend["Phosphor"].sum(axis = 0, skipna = True)/TS*100
        Mg=ration_hochleistend["Magnesium"].sum(axis = 0, skipna = True)/TS*100
        K=ration_hochleistend["Kalium"].sum(axis = 0, skipna = True)/TS*100
        if Mg==0:
            KMg=0
        else:
            KMg=K/Mg
        
         
        Na=ration_hochleistend["Natrium"].sum(axis = 0, skipna = True)/TS*100
        S=ration_hochleistend["Schwefel"].sum(axis = 0, skipna = True)/TS*100
        Kosten=ration_hochleistend['Kosten'].sum(axis = 0, skipna = True)
        
        Futterreste_hochleistend = float(Futterresteentry_hochleistend.get())
        Milchmenge_hochleistend = float(Milchertragentry_hochleistend.get())
        Milchpreis_hochleistend = float(Milchpreisentry_hochleistend.get())

        Kostenplus=Kosten*(float(Futterreste_hochleistend)/100+1)
        Umsatz=Milchmenge_hochleistend*Milchpreis_hochleistend/100
        IOFC=Umsatz-Kosten
        header = Label(master=tkFenster, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(TS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(PTS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(MJNEL,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(MJNELkg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=1, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text=round(NDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(GNDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(NFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(RP,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(Staerke,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=4, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text=round(Asche,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(Ca,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(P,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(Mg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(K,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=7, padx='1', pady='1', sticky='ew')
    
        header = Label(master=tkFenster, text=round(Na,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(S,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(KMg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=10, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text=round(Kosten,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(Kostenplus,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(IOFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(Umsatz,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=16, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_hochleistend:
                row.destroy()  

        for i in entryRf_hochleistend:
            i.destroy()    
           
        for i in entryFM_hochleistend:
            i.destroy()  
            
       
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_hochleistend[r] = Entry(master=tkFenster1, bg='white')
                    entryFM_hochleistend[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_hochleistend[r].insert(0,round(ration_hochleistend.iloc[r,c],2))
                    continue
                if c==0:
                    entryRf_hochleistend[r] = Entry(master=tkFenster1, bg='white')
                    entryRf_hochleistend[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_hochleistend[r].insert(0,ration_hochleistend.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=tkFenster1, bg='white', text=round(ration_hochleistend.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_hochleistend.append(Kasten)
                else:
                    Kasten = Label(master=tkFenster1, bg='white', text=ration_hochleistend.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_hochleistend.append(Kasten)

        return
        
    def button_frischmelker_berechnen():
        
        global ration_frischmelker, Futterreste_frischmelker, Milchmenge_frischmelker, Milchpreis_frischmelker
        ration_ziel=ration_frischmelker

        asd=ration_frischmelker.shape
        FM= [0] * asd[0]
        Rf= [1] * asd[0]
        for x in range(asd[0]):
            FM[x] = entryFM_frischmelker[x].get()
            Rf[x] = entryRf_frischmelker[x].get()
            FM[x]=FM[x].replace(',','.')
            Rf[x]=Rf[x].replace(',','.')
        
        for x in range(asd[0]):
            if FM[x]=='':
                FM[x]=0
                
            else:
                try:
                    FM[x]=float(FM[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Frischmasse ist keine Zahl")
                    return
            
            if Rf[x]=='':
                Rf[x]=0
                
            else:
                try:
                    Rf[x]=float(Rf[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Reihenfolge ist keine Zahl")
                    return
                
        ration_ziel['kg Frischmasse']=FM
        ration_ziel['Reihenfolge']=Rf
        ration_frischmelker['kg Frischmasse']=FM
        ration_frischmelker['Reihenfolge']=Rf
        
        ration_ziel['TS']=ration_ziel['kg Frischmasse'].mul(ration['TS in %'])/100
        ration_ziel['Kosten']= ration_ziel['kg Frischmasse'].mul(ration['Kosten ( € /dt )'])/100
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        ration_ziel['% der Ration TS']= ration_ziel['TS']/TS *100
        ration_ziel['MJ NEL']=ration_ziel['TS'].mul(ration['MJ NEL'])
        ration_ziel['NDF']=ration_ziel['TS'].mul(ration['NDF']) 
        ration_ziel['GNDF']=ration_ziel['TS'].mul(ration['Grundfutter NDF'])
        ration_ziel['uNDF30']=ration_ziel['TS'].mul(ration['uNDF30'])
        ration_ziel['uNDF120']=ration_ziel['TS'].mul(ration['uNDF120'])
        ration_ziel['uNDF240']=ration_ziel['TS'].mul(ration['uNDF240'])
        ration_ziel['NFC']=ration_ziel['TS'].mul(ration['NFC'])
        ration_ziel['Staerke']=ration_ziel['TS'].mul(ration['Staerke'])
        ration_ziel['Staerkeverdaulichkeit 7h']=ration_ziel['TS'].mul(ration['Staerkeverdaulichkeit 7h'])        
        ration_ziel['Rohprotein']=ration_ziel['TS'].mul(ration['Rohprotein'])
        ration_ziel['loesl. Protein']=ration_ziel['TS'].mul(ration['loesl. Protein'])
        ration_ziel['Ammonium-Protein']=ration_ziel['TS'].mul(ration['Ammonium-Protein'])
        ration_ziel['Asche']=ration_ziel['TS'].mul(ration['Asche'])
        ration_ziel['Kalzium']=ration_ziel['TS'].mul(ration['Kalzium'])
        ration_ziel['Phosphor']=ration_ziel['TS'].mul(ration['Phosphor'])
        ration_ziel['Magnesium']=ration_ziel['TS'].mul(ration['Magnesium'])
        ration_ziel['Kalium']=ration_ziel['TS'].mul(ration['Kalium'])
        ration_ziel['Natrium']=ration_ziel['TS'].mul(ration['Natrium'])
        ration_ziel['Schwefel']=ration_ziel['TS'].mul(ration['Schwefel'])
#        ration_ziel['Kationen']=ration_ziel['TS'].mul(ration['Kationen'])
#        ration_ziel['Anionen']=ration_ziel['TS'].mul(ration['Anionen'])
#        ration_ziel['Zucker']=ration_ziel['TS'].mul(ration['Zucker'])
        
        Frischmasse=ration_ziel["kg Frischmasse"].sum(axis = 0, skipna = True)
        if Frischmasse ==0:
            messagebox.showerror("Error",'Frischmasse ist 0')
            return
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        PTS=TS/Frischmasse*100
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        MJNELkg=MJNEL/TS
    
        NDF=ration_ziel["NDF"].sum(axis = 0, skipna = True)/TS
        GNDF=ration_ziel["GNDF"].sum(axis = 0, skipna = True)/TS
        NFC=ration_ziel["NFC"].sum(axis = 0, skipna = True)/TS
        RP=ration_ziel["Rohprotein"].sum(axis = 0, skipna = True)/TS
        Staerke=ration_ziel["Staerke"].sum(axis = 0, skipna = True)/TS
        
        Asche=ration_ziel["Asche"].sum(axis = 0, skipna = True)/TS*100
        Ca=ration_ziel["Kalzium"].sum(axis = 0, skipna = True)/TS*100
        P=ration_ziel["Phosphor"].sum(axis = 0, skipna = True)/TS*100
        Mg=ration_ziel["Magnesium"].sum(axis = 0, skipna = True)/TS*100
        K=ration_ziel["Kalium"].sum(axis = 0, skipna = True)/TS*100
        if Mg==0:
            KMg=0
        else:
            KMg=K/Mg
         
        Na=ration_ziel["Natrium"].sum(axis = 0, skipna = True)/TS*100
        S=ration_ziel["Schwefel"].sum(axis = 0, skipna = True)/TS*100
        Kosten=ration_ziel['Kosten'].sum(axis = 0, skipna = True)
        
        Futterreste_frischmelker = float(Futterresteentry_frischmelkend.get())
        Milchmenge_frischmelker = float(Milchertragentry_frischmelkend.get())
        Milchpreis_frischmelker = float(Milchpreisentry_frischmelkend.get())

        
        Kostenplus=Kosten*(float(Futterreste_frischmelker)/100+1)
        Umsatz=Milchmenge_frischmelker*Milchpreis_frischmelker/100
        IOFC=Umsatz-Kosten
        
        header = Label(master=Fenster_frisch, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(TS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(PTS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(MJNEL,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(MJNELkg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=1, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_frisch, text=round(NDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(GNDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(NFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(RP,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(Staerke,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=4, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_frisch, text=round(Asche,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(Ca,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(P,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(Mg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(K,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=7, padx='1', pady='1', sticky='ew')
    
        header = Label(master=Fenster_frisch, text=round(Na,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(S,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(KMg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=10, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_frisch, text=round(Kosten,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(Kostenplus,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(IOFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_frisch, text=round(Umsatz,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=16, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_frischmelker:
            row.destroy()  

        for i in entryFM_frischmelker:
            i.destroy()    
           
        for i in entryRf_frischmelker:
            i.destroy() 
       
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_frischmelker[r] = Entry(master=Fenster_frisch1, bg='white')
                    entryFM_frischmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_frischmelker[r].insert(0,round(ration_ziel.iloc[r,c],2))
                    continue
                if c==0:
                    entryRf_frischmelker[r] = Entry(master=Fenster_frisch1, bg='white')
                    entryRf_frischmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_frischmelker[r].insert(0,ration_ziel.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=Fenster_frisch1, bg='white', text=round(ration_ziel.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_frischmelker.append(Kasten)
                else:
                    Kasten = Label(master=Fenster_frisch1, bg='white', text=ration_ziel.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_frischmelker.append(Kasten)
                    
        ration_frischmelker=ration_ziel
        return
        
    def button_altmelker_berechnen():
        
        global ration_altmelker, Futterreste_altmelker, Milchmenge_altmelker, Milchpreis_altmelker
        ration_ziel=ration_altmelker

        asd=ration_altmelker.shape
        FM= [0] * asd[0]
        Rf= [1] * asd[0]
        for x in range(asd[0]):
            FM[x] = entryFM_altmelker[x].get()
            Rf[x] = entryRf_altmelker[x].get()
            FM[x]=FM[x].replace(',','.')
            Rf[x]=Rf[x].replace(',','.')
        
        for x in range(asd[0]):
            if FM[x]=='':
                FM[x]=0
                
            else:
                try:
                    FM[x]=float(FM[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Frischmasse ist keine Zahl")
                    return
            
            if Rf[x]=='':
                Rf[x]=0
                
            else:
                try:
                    Rf[x]=float(Rf[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Reihenfolge ist keine Zahl")
                    return
                
        ration_ziel['kg Frischmasse']=FM
        ration_ziel['Reihenfolge']=Rf
        ration_altmelker['kg Frischmasse']=FM
        ration_altmelker['Reihenfolge']=Rf
        
        ration_ziel['TS']=ration_ziel['kg Frischmasse'].mul(ration['TS in %'])/100
        ration_ziel['TS']=ration_ziel['kg Frischmasse'].mul(ration['TS in %'])/100
        ration_ziel['Kosten']= ration_ziel['kg Frischmasse'].mul(ration['Kosten ( € /dt )'])/100
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        ration_ziel['% der Ration TS']= ration_ziel['TS']/TS *100
        ration_ziel['MJ NEL']=ration_ziel['TS'].mul(ration['MJ NEL'])
        ration_ziel['NDF']=ration_ziel['TS'].mul(ration['NDF']) 
        ration_ziel['GNDF']=ration_ziel['TS'].mul(ration['Grundfutter NDF'])
        ration_ziel['uNDF30']=ration_ziel['TS'].mul(ration['uNDF30'])
        ration_ziel['uNDF120']=ration_ziel['TS'].mul(ration['uNDF120'])
        ration_ziel['uNDF240']=ration_ziel['TS'].mul(ration['uNDF240'])
        ration_ziel['NFC']=ration_ziel['TS'].mul(ration['NFC'])
        ration_ziel['Staerke']=ration_ziel['TS'].mul(ration['Staerke'])
        ration_ziel['Staerkeverdaulichkeit 7h']=ration_ziel['TS'].mul(ration['Staerkeverdaulichkeit 7h'])        
        ration_ziel['Rohprotein']=ration_ziel['TS'].mul(ration['Rohprotein'])
        ration_ziel['loesl. Protein']=ration_ziel['TS'].mul(ration['loesl. Protein'])
        ration_ziel['Ammonium-Protein']=ration_ziel['TS'].mul(ration['Ammonium-Protein'])
        ration_ziel['Asche']=ration_ziel['TS'].mul(ration['Asche'])
        ration_ziel['Kalzium']=ration_ziel['TS'].mul(ration['Kalzium'])
        ration_ziel['Phosphor']=ration_ziel['TS'].mul(ration['Phosphor'])
        ration_ziel['Magnesium']=ration_ziel['TS'].mul(ration['Magnesium'])
        ration_ziel['Kalium']=ration_ziel['TS'].mul(ration['Kalium'])
        ration_ziel['Natrium']=ration_ziel['TS'].mul(ration['Natrium'])
        ration_ziel['Schwefel']=ration_ziel['TS'].mul(ration['Schwefel'])
        
        
        Frischmasse=ration_ziel["kg Frischmasse"].sum(axis = 0, skipna = True)
        if Frischmasse ==0:
            messagebox.showerror("Error",'Frischmasse ist 0')
            return
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        PTS=TS/Frischmasse*100
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        MJNELkg=MJNEL/TS
    
        NDF=ration_ziel["NDF"].sum(axis = 0, skipna = True)/TS
        GNDF=ration_ziel["GNDF"].sum(axis = 0, skipna = True)/TS
        NFC=ration_ziel["NFC"].sum(axis = 0, skipna = True)/TS
        RP=ration_ziel["Rohprotein"].sum(axis = 0, skipna = True)/TS
        Staerke=ration_ziel["Staerke"].sum(axis = 0, skipna = True)/TS
        
        Asche=ration_ziel["Asche"].sum(axis = 0, skipna = True)/TS*100
        Ca=ration_ziel["Kalzium"].sum(axis = 0, skipna = True)/TS*100
        P=ration_ziel["Phosphor"].sum(axis = 0, skipna = True)/TS*100
        Mg=ration_ziel["Magnesium"].sum(axis = 0, skipna = True)/TS*100
        K=ration_ziel["Kalium"].sum(axis = 0, skipna = True)/TS*100
        if Mg==0:
            KMg=0
        else:
            KMg=K/Mg
         
        Na=ration_ziel["Natrium"].sum(axis = 0, skipna = True)/TS*100
        S=ration_ziel["Schwefel"].sum(axis = 0, skipna = True)/TS*100
        Kosten=ration_ziel['Kosten'].sum(axis = 0, skipna = True)
        
        Futterreste_altmelker = float(Futterresteentry_altmelkend.get())
        Milchmenge_altmelker = float(Milchertragentry_altmelkend.get())
        Milchpreis_altmelker = float(Milchpreisentry_altmelkend.get())

        
        Kostenplus=Kosten*(float(Futterreste_altmelker)/100+1)
        Umsatz=Milchmenge_altmelker*Milchpreis_altmelker/100
        IOFC=Umsatz-Kosten
        
        header = Label(master=Fenster_alt, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(TS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(PTS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(MJNEL,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(MJNELkg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=1, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_alt, text=round(NDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(GNDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(NFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(RP,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(Staerke,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=4, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_alt, text=round(Asche,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(Ca,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(P,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(Mg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(K,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=7, padx='1', pady='1', sticky='ew')
    
        header = Label(master=Fenster_alt, text=round(Na,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(S,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(KMg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=10, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_alt, text=round(Kosten,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(Kostenplus,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(IOFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_alt, text=round(Umsatz,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=16, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_frischmelker:
            row.destroy()  

        for i in entryFM_altmelker:
            i.destroy()    
           
        for i in entryRf_altmelker:
            i.destroy() 
       
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_altmelker[r] = Entry(master=Fenster_alt1, bg='white')
                    entryFM_altmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_altmelker[r].insert(0,round(ration_ziel.iloc[r,c],2))
                    continue
                if c==0:
                    entryRf_altmelker[r] = Entry(master=Fenster_alt1, bg='white')
                    entryRf_altmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_altmelker[r].insert(0,ration_ziel.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=Fenster_alt1, bg='white', text=round(ration_ziel.iloc[r,c],2),font="Arial 10")
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_altmelker.append(Kasten)
                else:
                    Kasten = Label(master=Fenster_alt1, bg='white', text=ration_ziel.iloc[r,c],font="Arial 10")
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_altmelker.append(Kasten)
                    
        ration_altmelker=ration_ziel

        return
    
    def button_trockensteher_berechnen():

        global ration_trockensteher, Futterreste_trockensteher, Milchmenge_trockensteher, Milchpreis_trockensteher
        ration_ziel=ration_trockensteher

        asd=ration_trockensteher.shape
        FM= [0] * asd[0]
        Rf= [1] * asd[0]
        for x in range(asd[0]):
            FM[x] = entryFM_trockensteher[x].get()
            Rf[x] = entryRf_trockensteher[x].get()
            FM[x]=FM[x].replace(',','.')
            Rf[x]=Rf[x].replace(',','.')
        
        for x in range(asd[0]):
            if FM[x]=='':
                FM[x]=0
                
            else:
                try:
                    FM[x]=float(FM[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Frischmasse ist keine Zahl")
                    return
            
            if Rf[x]=='':
                Rf[x]=0
                
            else:
                try:
                    Rf[x]=float(Rf[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Reihenfolge ist keine Zahl")
                    return
                
        ration_ziel['kg Frischmasse']=FM
        ration_ziel['Reihenfolge']=Rf
        ration_ziel['TS']=ration_ziel['kg Frischmasse'].mul(ration['TS in %'])/100
        ration_ziel['Kosten']= ration_ziel['kg Frischmasse'].mul(ration['Kosten ( € /dt )'])/100
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        ration_ziel['% der Ration TS']= ration_ziel['TS']/TS *100
        ration_ziel['MJ NEL']=ration_ziel['TS'].mul(ration['MJ NEL'])
        ration_ziel['NDF']=ration_ziel['TS'].mul(ration['NDF']) 
        ration_ziel['GNDF']=ration_ziel['TS'].mul(ration['Grundfutter NDF'])
        ration_ziel['uNDF30']=ration_ziel['TS'].mul(ration['uNDF30'])
        ration_ziel['uNDF120']=ration_ziel['TS'].mul(ration['uNDF120'])
        ration_ziel['uNDF240']=ration_ziel['TS'].mul(ration['uNDF240'])
        ration_ziel['NFC']=ration_ziel['TS'].mul(ration['NFC'])
        ration_ziel['Staerke']=ration_ziel['TS'].mul(ration['Staerke'])
        ration_ziel['Staerkeverdaulichkeit 7h']=ration_ziel['TS'].mul(ration['Staerkeverdaulichkeit 7h'])        
        ration_ziel['Rohprotein']=ration_ziel['TS'].mul(ration['Rohprotein'])
        ration_ziel['loesl. Protein']=ration_ziel['TS'].mul(ration['loesl. Protein'])
        ration_ziel['Ammonium-Protein']=ration_ziel['TS'].mul(ration['Ammonium-Protein'])
        ration_ziel['Asche']=ration_ziel['TS'].mul(ration['Asche'])
        ration_ziel['Kalzium']=ration_ziel['TS'].mul(ration['Kalzium'])
        ration_ziel['Phosphor']=ration_ziel['TS'].mul(ration['Phosphor'])
        ration_ziel['Magnesium']=ration_ziel['TS'].mul(ration['Magnesium'])
        ration_ziel['Kalium']=ration_ziel['TS'].mul(ration['Kalium'])
        ration_ziel['Natrium']=ration_ziel['TS'].mul(ration['Natrium'])
        ration_ziel['Schwefel']=ration_ziel['TS'].mul(ration['Schwefel'])
        
        Frischmasse=ration_ziel["kg Frischmasse"].sum(axis = 0, skipna = True)
        if Frischmasse ==0:
            messagebox.showerror("Error",'Frischmasse ist 0')
            return
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        PTS=TS/Frischmasse*100
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        MJNELkg=MJNEL/TS
    
        NDF=ration_ziel["NDF"].sum(axis = 0, skipna = True)/TS
        GNDF=ration_ziel["GNDF"].sum(axis = 0, skipna = True)/TS
        
        NFC=ration_ziel["NFC"].sum(axis = 0, skipna = True)/TS
        RP=ration_ziel["Rohprotein"].sum(axis = 0, skipna = True)/TS
        Staerke=ration_ziel["Staerke"].sum(axis = 0, skipna = True)/TS
        
        Asche=ration_ziel["Asche"].sum(axis = 0, skipna = True)/TS*100
        Ca=ration_ziel["Kalzium"].sum(axis = 0, skipna = True)/TS*100
        P=ration_ziel["Phosphor"].sum(axis = 0, skipna = True)/TS*100
        Mg=ration_ziel["Magnesium"].sum(axis = 0, skipna = True)/TS*100
        K=ration_ziel["Kalium"].sum(axis = 0, skipna = True)/TS*100
        if Mg==0:
            KMg=0
        else:
            KMg=K/Mg
         
        Na=ration_ziel["Natrium"].sum(axis = 0, skipna = True)/TS*100
        S=ration_ziel["Schwefel"].sum(axis = 0, skipna = True)/TS*100
        Kosten=ration_ziel['Kosten'].sum(axis = 0, skipna = True)
        
        Futterreste_trockensteher = float(Futterresteentry_trockenstehend.get())
        Milchmenge_trockensteher = float(Milchertragentry_trockenstehend.get())
        Milchpreis_trockensteher = float(Milchpreisentry_trockenstehend.get())
        
        Kostenplus=Kosten*(float(Futterreste_trockensteher)/100+1)
        Umsatz=Milchmenge_trockensteher*Milchpreis_trockensteher/100
        IOFC=Umsatz-Kosten
        
        header = Label(master=Fenster_trocken, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(TS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(PTS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(MJNEL,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(MJNELkg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=1, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_trocken, text=round(NDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(GNDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(NFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(RP,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(Staerke,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=4, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_trocken, text=round(Asche,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(Ca,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(P,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(Mg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(K,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=7, padx='1', pady='1', sticky='ew')
    
        header = Label(master=Fenster_trocken, text=round(Na,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(S,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(KMg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=10, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_trocken, text=round(Kosten,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(Kostenplus,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(IOFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_trocken, text=round(Umsatz,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=16, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_trockensteher:
            row.destroy()  

        for i in entryFM_trockensteher:
            i.destroy()    
           
        for i in entryRf_trockensteher:
            i.destroy() 
       
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_trockensteher[r] = Entry(master=Fenster_trocken1, bg='white')
                    entryFM_trockensteher[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_trockensteher[r].insert(0,round(ration_ziel.iloc[r,c],2))
                    continue
                if c==0:
                    entryRf_trockensteher[r] = Entry(master=Fenster_trocken1, bg='white')
                    entryRf_trockensteher[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_trockensteher[r].insert(0,ration_ziel.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=Fenster_trocken1, bg='white', text=round(ration_ziel.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_trockensteher.append(Kasten)
                else:
                    Kasten = Label(master=Fenster_trocken1, bg='white', text=ration_ziel.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_trockensteher.append(Kasten)
                    
        ration_trockensteher=ration_ziel

        return
    
    def button_rinder_berechnen():

        global ration_rinder, Futterreste_rinder, Milchpreis_rinder, Milchmenge_rinder
        ration_ziel=ration_rinder
        
        asd=ration_rinder.shape
        
        FM= [0] * asd[0]
        Rf= [1] * asd[0]
        for x in range(asd[0]):
            FM[x] = entryFM_rinder[x].get()
            Rf[x] = entryRf_rinder[x].get()
            FM[x]=FM[x].replace(',','.')
            Rf[x]=Rf[x].replace(',','.')
        
        for x in range(asd[0]):
            if FM[x]=='':
                FM[x]=0
                
            else:
                try:
                    FM[x]=float(FM[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Frischmasse ist keine Zahl")
                    return
            
            if Rf[x]=='':
                Rf[x]=0
                
            else:
                try:
                    Rf[x]=float(Rf[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Reihenfolge ist keine Zahl")
                    return

        ration_ziel['kg Frischmasse']=FM
        ration_ziel['Reihenfolge']=Rf
        #    ration_ziel=ration_ziel.sort_values(by=['kg Frischmasse'], ascending=False)
        #    ration=ration.sort_values(by=['kg Frischmasse'], ascending=False)
        ration_ziel['TS']=ration_ziel['kg Frischmasse'].mul(ration['TS in %'])/100
        ration_ziel['Kosten']= ration_ziel['kg Frischmasse'].mul(ration['Kosten ( € /dt )'])/100
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        ration_ziel['% der Ration TS']= ration_ziel['TS']/TS *100
        ration_ziel['MJ NEL']=ration_ziel['TS'].mul(ration['MJ NEL'])
        ration_ziel['NDF']=ration_ziel['TS'].mul(ration['NDF']) 
        ration_ziel['GNDF']=ration_ziel['TS'].mul(ration['Grundfutter NDF'])
        ration_ziel['uNDF30']=ration_ziel['TS'].mul(ration['uNDF30'])
        ration_ziel['uNDF120']=ration_ziel['TS'].mul(ration['uNDF120'])
        ration_ziel['uNDF240']=ration_ziel['TS'].mul(ration['uNDF240'])
        ration_ziel['NFC']=ration_ziel['TS'].mul(ration['NFC'])
        ration_ziel['Staerke']=ration_ziel['TS'].mul(ration['Staerke'])
        ration_ziel['Staerkeverdaulichkeit 7h']=ration_ziel['TS'].mul(ration['Staerkeverdaulichkeit 7h'])        
        ration_ziel['Rohprotein']=ration_ziel['TS'].mul(ration['Rohprotein'])
        ration_ziel['loesl. Protein']=ration_ziel['TS'].mul(ration['loesl. Protein'])
        ration_ziel['Ammonium-Protein']=ration_ziel['TS'].mul(ration['Ammonium-Protein'])
        ration_ziel['Asche']=ration_ziel['TS'].mul(ration['Asche'])
        ration_ziel['Kalzium']=ration_ziel['TS'].mul(ration['Kalzium'])
        ration_ziel['Phosphor']=ration_ziel['TS'].mul(ration['Phosphor'])
        ration_ziel['Magnesium']=ration_ziel['TS'].mul(ration['Magnesium'])
        ration_ziel['Kalium']=ration_ziel['TS'].mul(ration['Kalium'])
        ration_ziel['Natrium']=ration_ziel['TS'].mul(ration['Natrium'])
        ration_ziel['Schwefel']=ration_ziel['TS'].mul(ration['Schwefel'])
        
        Frischmasse=ration_ziel["kg Frischmasse"].sum(axis = 0, skipna = True)
        if Frischmasse ==0:
            messagebox.showerror("Error",'Frischmasse ist 0')
            return
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        PTS=TS/Frischmasse*100
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        MJNELkg=MJNEL/TS    
        NDF=ration_ziel["NDF"].sum(axis = 0, skipna = True)/TS
        GNDF=ration_ziel["GNDF"].sum(axis = 0, skipna = True)/TS
        NFC=ration_ziel["NFC"].sum(axis = 0, skipna = True)/TS
        RP=ration_ziel["Rohprotein"].sum(axis = 0, skipna = True)/TS
        Staerke=ration_ziel["Staerke"].sum(axis = 0, skipna = True)/TS        
        Asche=ration_ziel["Asche"].sum(axis = 0, skipna = True)/TS*100
        Ca=ration_ziel["Kalzium"].sum(axis = 0, skipna = True)/TS*100
        P=ration_ziel["Phosphor"].sum(axis = 0, skipna = True)/TS*100
        Mg=ration_ziel["Magnesium"].sum(axis = 0, skipna = True)/TS*100
        K=ration_ziel["Kalium"].sum(axis = 0, skipna = True)/TS*100         
        Na=ration_ziel["Natrium"].sum(axis = 0, skipna = True)/TS*100
        S=ration_ziel["Schwefel"].sum(axis = 0, skipna = True)/TS*100
        Kosten=ration_ziel['Kosten'].sum(axis = 0, skipna = True)
        if Mg==0:
            KMg=0
        else:
            KMg=K/Mg
       
        Futterreste_rinder = float(Futterresteentry_rinder.get())
        Milchmenge_rinder = float(Milchertragentry_rinder.get())
        Milchpreis_rinder = float(Milchpreisentry_rinder.get())
        
        Kostenplus=Kosten*(float(Futterreste_rinder)/100+1)
        Umsatz=Milchmenge_rinder*Milchpreis_rinder/100
        IOFC=Umsatz-Kosten
        
        header = Label(master=Fenster_rinder, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(TS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(PTS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(MJNEL,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(MJNELkg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=1, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_rinder, text=round(NDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(GNDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(NFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(RP,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(Staerke,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=4, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_rinder, text=round(Asche,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(Ca,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(P,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(Mg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(K,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=7, padx='1', pady='1', sticky='ew')
    
        header = Label(master=Fenster_rinder, text=round(Na,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(S,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(KMg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=10, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_rinder, text=round(Kosten,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(Kostenplus,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(IOFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_rinder, text=round(Umsatz,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=16, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_rinder:
            row.destroy()  

        for i in entryFM_rinder:
            i.destroy()    
           
        for i in entryRf_rinder:
            i.destroy() 
       
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_rinder[r] = Entry(master=Fenster_rinder1, bg='white')
                    entryFM_rinder[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_rinder[r].insert(0,round(ration_ziel.iloc[r,c],2))
                    continue
                if c==0:
                    entryRf_rinder[r] = Entry(master=Fenster_rinder1, bg='white')
                    entryRf_rinder[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_rinder[r].insert(0,ration_ziel.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=Fenster_rinder1, bg='white', text=round(ration_ziel.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_rinder.append(Kasten)
                else:
                    Kasten = Label(master=Fenster_rinder1, bg='white', text=ration_ziel.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_rinder.append(Kasten)
                    
        ration_rinder=ration_ziel

        return
    
    def button_bullen_berechnen():

        global ration_bullen, Futterreste_bullen, Milchpreis_bullen, Milchmenge_bullen
        ration_ziel=ration_bullen
        asd=ration_bullen.shape
        FM= [0] * asd[0]
        Rf= [1] * asd[0]
        for x in range(asd[0]):
            FM[x] = entryFM_bullen[x].get()
            Rf[x] = entryRf_bullen[x].get()
            FM[x]=FM[x].replace(',','.')
            Rf[x]=Rf[x].replace(',','.')
        
        for x in range(asd[0]):
            if FM[x]=='':
                FM[x]=0
                
            else:
                try:
                    FM[x]=float(FM[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Frischmasse ist keine Zahl")
                    return
            
            if Rf[x]=='':
                Rf[x]=0
                
            else:
                try:
                    Rf[x]=float(Rf[x])
                except ValueError: 
                    messagebox.showerror("Error","Eingegebene Reihenfolge ist keine Zahl")
                    return
                
        ration_ziel['kg Frischmasse']=FM
        ration_ziel['Reihenfolge']=Rf
        ration_ziel['TS']=ration_ziel['kg Frischmasse'].mul(ration['TS in %'])/100
        ration_ziel['Kosten']= ration_ziel['kg Frischmasse'].mul(ration['Kosten ( € /dt )'])/100
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        ration_ziel['% der Ration TS']= ration_ziel['TS']/TS *100
        ration_ziel['MJ NEL']=ration_ziel['TS'].mul(ration['MJ NEL'])
        ration_ziel['NDF']=ration_ziel['TS'].mul(ration['NDF']) 
        ration_ziel['GNDF']=ration_ziel['TS'].mul(ration['Grundfutter NDF'])
        ration_ziel['uNDF30']=ration_ziel['TS'].mul(ration['uNDF30'])
        ration_ziel['uNDF120']=ration_ziel['TS'].mul(ration['uNDF120'])
        ration_ziel['uNDF240']=ration_ziel['TS'].mul(ration['uNDF240'])
        ration_ziel['NFC']=ration_ziel['TS'].mul(ration['NFC'])
        ration_ziel['Staerke']=ration_ziel['TS'].mul(ration['Staerke'])
        ration_ziel['Staerkeverdaulichkeit 7h']=ration_ziel['TS'].mul(ration['Staerkeverdaulichkeit 7h'])        
        ration_ziel['Rohprotein']=ration_ziel['TS'].mul(ration['Rohprotein'])
        ration_ziel['loesl. Protein']=ration_ziel['TS'].mul(ration['loesl. Protein'])
        ration_ziel['Ammonium-Protein']=ration_ziel['TS'].mul(ration['Ammonium-Protein'])
        ration_ziel['Asche']=ration_ziel['TS'].mul(ration['Asche'])
        ration_ziel['Kalzium']=ration_ziel['TS'].mul(ration['Kalzium'])
        ration_ziel['Phosphor']=ration_ziel['TS'].mul(ration['Phosphor'])
        ration_ziel['Magnesium']=ration_ziel['TS'].mul(ration['Magnesium'])
        ration_ziel['Kalium']=ration_ziel['TS'].mul(ration['Kalium'])
        ration_ziel['Natrium']=ration_ziel['TS'].mul(ration['Natrium'])
        ration_ziel['Schwefel']=ration_ziel['TS'].mul(ration['Schwefel'])
        
        Frischmasse=ration_ziel["kg Frischmasse"].sum(axis = 0, skipna = True)
        if Frischmasse ==0:
            messagebox.showerror("Error",'Frischmasse ist 0')
            return
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        PTS=TS/Frischmasse*100
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        MJNELkg=MJNEL/TS    
        NDF=ration_ziel["NDF"].sum(axis = 0, skipna = True)/TS
        GNDF=ration_ziel["GNDF"].sum(axis = 0, skipna = True)/TS
        NFC=ration_ziel["NFC"].sum(axis = 0, skipna = True)/TS
        RP=ration_ziel["Rohprotein"].sum(axis = 0, skipna = True)/TS
        Staerke=ration_ziel["Staerke"].sum(axis = 0, skipna = True)/TS        
        Asche=ration_ziel["Asche"].sum(axis = 0, skipna = True)/TS*100
        Ca=ration_ziel["Kalzium"].sum(axis = 0, skipna = True)/TS*100
        P=ration_ziel["Phosphor"].sum(axis = 0, skipna = True)/TS*100
        Mg=ration_ziel["Magnesium"].sum(axis = 0, skipna = True)/TS*100
        K=ration_ziel["Kalium"].sum(axis = 0, skipna = True)/TS*100         
        Na=ration_ziel["Natrium"].sum(axis = 0, skipna = True)/TS*100
        S=ration_ziel["Schwefel"].sum(axis = 0, skipna = True)/TS*100
        Kosten=ration_ziel['Kosten'].sum(axis = 0, skipna = True)
        if Mg==0:
            KMg=0
        else:
            KMg=K/Mg        
        Futterreste_bullen = float(Futterresteentry_bullen.get())
        Milchmenge_bullen = float(Milchertragentry_bullen.get())
        Milchpreis_bullen = float(Milchpreisentry_bullen.get())
        
        Kostenplus=Kosten*(float(Futterreste_bullen)/100+1)
        Umsatz=Milchmenge_bullen*Milchpreis_bullen/100
        IOFC=Umsatz-Kosten
        
        header = Label(master=Fenster_bullen, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(TS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(PTS,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(MJNEL,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(MJNELkg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=1, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_bullen, text=round(NDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(GNDF,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(NFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(RP,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(Staerke,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=4, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_bullen, text=round(Asche,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(Ca,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(P,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(Mg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(K,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=4, column=7, padx='1', pady='1', sticky='ew')
    
        header = Label(master=Fenster_bullen, text=round(Na,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(S,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(KMg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=10, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster_bullen, text=round(Kosten,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(Kostenplus,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(IOFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster_bullen, text=round(Umsatz,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=16, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_bullen:
            row.destroy()  

        for i in entryFM_bullen:
            i.destroy()    
           
        for i in entryRf_bullen:
            i.destroy()
       
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==6:
                    entryFM_bullen[r] = Entry(master=Fenster_bullen1, bg='white')
                    entryFM_bullen[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM_bullen[r].insert(0,round(ration_ziel.iloc[r,c],2))
                    continue
                if c==0:
                    entryRf_bullen[r] = Entry(master=Fenster_bullen1, bg='white')
                    entryRf_bullen[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf_bullen[r].insert(0,ration_ziel.iloc[r,0])
                elif c>4:
                    Kasten = Label(master=Fenster_bullen1, bg='white', text=round(ration_ziel.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_bullen.append(Kasten)
                else:
                    Kasten = Label(master=Fenster_bullen1, bg='white', text=ration_ziel.iloc[r,c])
                    Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    Kasten_bullen.append(Kasten)
        ration_bullen=ration_ziel
        return
    
    
    def button_hochleistend_weiter():
        global status
        status='weiter'
        Tk.destroy(parent)
        return
    
    def button_frischmelker_weiter():
        global status
        status='weiter'
        Tk.destroy(parent)
        return
    
    def button_altmelker_weiter():
        global status
        status='weiter'
        Tk.destroy(parent)
        return
    
    def button_trockensteher_weiter():
        global status
        status='weiter'
        Tk.destroy(parent)
        return
    
    def button_rinder_weiter():
        global status
        status='weiter'
        Tk.destroy(parent)
        return
    
    def button_bullen_weiter():
        global status
        status='weiter'
        Tk.destroy(parent)
        return
    
    def buttonAktualisierenMischung_hochleistend():
        global Anzahl_hochleistend, Varianz_hochleistend, mischung_hochleistend
        Anzahl_hochleistend = EntryAnzahl_hochleistend.get()
        Varianz_hochleistend = EntryVar_hochleistend.get()
        Anzahl_hochleistend=Anzahl_hochleistend.replace(',','.')
        Varianz_hochleistend=Varianz_hochleistend.replace(',','.')
        
        try:
            Anzahl_hochleistend=float(Anzahl_hochleistend)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Anzahl ist keine Zahl")
                return
    
        try:
            Varianz_hochleistend=float(Varianz_hochleistend)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Varianz ist keine Zahl")
                return
                         
        mischung_hochleistend['Reihenfolge']=ration_hochleistend['Reihenfolge']
        mischung_hochleistend['Komponente']=ration_hochleistend['Komponente']
        mischung_hochleistend['Bezeichnung']=ration_hochleistend['Bezeichnung']
        mischung_hochleistend['kg Frischmasse']=ration_hochleistend['kg Frischmasse']
        mischung_hochleistend['untere Lademenge']=mischung_hochleistend['kg Frischmasse']*(Anzahl_hochleistend-Varianz_hochleistend)
        mischung_hochleistend['normale Lademenge']=ration_hochleistend['kg Frischmasse']*Anzahl_hochleistend
        mischung_hochleistend['obere Lademenge']=ration_hochleistend['kg Frischmasse']*(Anzahl_hochleistend+Varianz_hochleistend)
        mischung_hochleistend=mischung_hochleistend.sort_values(by=['Reihenfolge'], ascending=True)
                
        header = Label(master=Mischung, text=Anzahl_hochleistend-Varianz_hochleistend, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung, text=Anzahl_hochleistend, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung, text=Anzahl_hochleistend +Varianz_hochleistend, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_Mischung_hochleistend:
            row.destroy()  
        number_rows=mischung_hochleistend.shape
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c>3:
                    Kasten = Label(master=Mischung, bg='white',text=round(mischung_hochleistend.iloc[r,c],2))
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_hochleistend.append(Kasten)
                else:   
                    Kasten = Label(master=Mischung, bg='white', text=mischung_hochleistend.iloc[r,c])            
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_hochleistend.append(Kasten)
        
        Frischmasse=mischung_hochleistend["kg Frischmasse"].sum(axis = 0, skipna = True)
        header = Label(master=Mischung, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung, text=round(Frischmasse*(Anzahl_hochleistend-Varianz_hochleistend),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung, text=round(Frischmasse*Anzahl_hochleistend,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung, text=round(Frischmasse*(Anzahl_hochleistend+Varianz_hochleistend),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
        
        return

    def buttonAktualisierenMischung_Frischmelker():
        global Anzahl_frischmelker, Varianz_frischmelker, mischung_frischmelker
        Anzahl_frischmelker = EntryAnzahl_Frischmelker.get()
        Varianz_frischmelker = EntryVar_Frischmelker.get()
        Anzahl_frischmelker=Anzahl_frischmelker.replace(',','.')
        Varianz_frischmelker=Varianz_frischmelker.replace(',','.')
        
        try:
            Anzahl_frischmelker=float(Anzahl_frischmelker)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Anzahl ist keine Zahl")
                return
    
        try:
            Varianz_frischmelker=float(Varianz_frischmelker)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Varianz ist keine Zahl")
                return
                
        mischung_frischmelker['Reihenfolge']=ration_frischmelker['Reihenfolge']
        mischung_frischmelker['Komponente']=ration_frischmelker['Komponente']
        mischung_frischmelker['Bezeichnung']=ration_frischmelker['Bezeichnung']
        mischung_frischmelker['kg Frischmasse']=ration_frischmelker['kg Frischmasse']
        mischung_frischmelker['untere Lademenge']=mischung_frischmelker['kg Frischmasse']*(Anzahl_frischmelker-Varianz_frischmelker)
        mischung_frischmelker['normale Lademenge']=mischung_frischmelker['kg Frischmasse']*Anzahl_frischmelker
        mischung_frischmelker['obere Lademenge']=mischung_frischmelker['kg Frischmasse']*(Anzahl_frischmelker+Varianz_frischmelker) 
        mischung_frischmelker=mischung_frischmelker.sort_values(by=['Reihenfolge'], ascending=True)
                
        header = Label(master=Mischung_Frischmelker, text=Anzahl_frischmelker-Varianz_frischmelker, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Frischmelker, text=Anzahl_frischmelker, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Frischmelker, text=Anzahl_frischmelker +Varianz_frischmelker, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_Mischung_frischmelker:
            row.destroy()  
        number_rows=mischung_frischmelker.shape
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c>3:
                    Kasten = Label(master=Mischung_Frischmelker, bg='white',text=round(mischung_frischmelker.iloc[r,0],2))
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_frischmelker.append(Kasten)
                else:   
                    Kasten = Label(master=Mischung_Frischmelker, bg='white', text=mischung_frischmelker.iloc[r,1])            
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_frischmelker.append(Kasten)
        
        Frischmasse=mischung_frischmelker["kg Frischmasse"].sum(axis = 0, skipna = True)
        header = Label(master=Mischung_Frischmelker, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Frischmelker, text=round(Frischmasse*(Anzahl_frischmelker-Varianz_frischmelker),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Frischmelker, text=round(Frischmasse*Anzahl_frischmelker,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Frischmelker, text=round(Frischmasse*(Anzahl_frischmelker+Varianz_frischmelker),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
        
        return

    def buttonAktualisierenMischung_Altmelker():
        global Anzahl_altmelker, Varianz_altmelker, mischung_altmelker
        Anzahl_altmelker = EntryAnzahl_Altmelker.get()
        Varianz_altmelker = EntryVar_Altmelker.get()
        Anzahl_altmelker=Anzahl_altmelker.replace(',','.')
        Varianz_altmelker=Varianz_altmelker.replace(',','.')
        
        try:
            Anzahl=float(Anzahl)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Anzahl ist keine Zahl")
                return
    
        try:
            Varianz=float(Varianz)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Varianz ist keine Zahl")
                return
                
        mischung_altmelker['Reihenfolge']=ration_altmelker['Reihenfolge']
        mischung_altmelker['Komponente']=ration_altmelker['Komponente']
        mischung_altmelker['Bezeichnung']=ration_altmelker['Bezeichnung']
        mischung_altmelker['kg Frischmasse']=ration_altmelker['kg Frischmasse']
        mischung_altmelker['untere Lademenge']=mischung_altmelker['kg Frischmasse']*(Anzahl_altmelker-Varianz_altmelker)
        mischung_altmelker['normale Lademenge']=mischung_altmelker['kg Frischmasse']*Anzahl_altmelker
        mischung_altmelker['obere Lademenge']=mischung_altmelker['kg Frischmasse']*(Anzahl_altmelker+Varianz_altmelker) 
        mischung_altmelker=mischung_altmelker.sort_values(by=['Reihenfolge'], ascending=True)
                
        header = Label(master=Mischung_Altmelker, text=Anzahl_altmelker-Varianz_altmelker, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Altmelker, text=Anzahl_altmelker, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Altmelker, text=Anzahl_altmelker +Varianz_altmelker, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_Mischung_altmelker:
            row.destroy()  
        number_rows=mischung_altmelker.shape
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c>3:
                    Kasten = Label(master=Mischung_Altmelker, bg='white',text=round(mischung_altmelker.iloc[r,0],2))
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_altmelker.append(Kasten)
                else:   
                    Kasten = Label(master=Mischung_Altmelker, bg='white', text=mischung_altmelker.iloc[r,1])            
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_altmelker.append(Kasten)
        
        Frischmasse=mischung_altmelker["kg Frischmasse"].sum(axis = 0, skipna = True)
        header = Label(master=Mischung_Altmelker, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Altmelker, text=round(Frischmasse*(Anzahl_altmelker-Varianz_altmelker),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Altmelker, text=round(Frischmasse*Anzahl_altmelker,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Altmelker, text=round(Frischmasse*(Anzahl_altmelker+Varianz_altmelker),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
        return
    
    def buttonAktualisierenMischung_Trockensteher():
        global Anzahl_trockensteher, Varianz_trockensteher, mischung_trockensteher
        Anzahl_trockensteher = EntryAnzahl_Trockensteher.get()
        Varianz_trockensteher = EntryVar_Trockensteher.get()
        Anzahl_trockensteher=Anzahl_trockensteher.replace(',','.')
        Varianz_trockensteher=Varianz_trockensteher.replace(',','.')
        
        try:
            Anzahl_trockensteher=float(Anzahl_trockensteher)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Anzahl ist keine Zahl")
                return
    
        try:
            Varianz_trockensteher=float(Varianz_trockensteher)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Varianz ist keine Zahl")
                return
                
                
        mischung_trockensteher['Reihenfolge']=ration_trockensteher['Reihenfolge']
        mischung_trockensteher['Komponente']=ration_trockensteher['Komponente']
        mischung_trockensteher['Bezeichnung']=ration_trockensteher['Bezeichnung']
        mischung_trockensteher['kg Frischmasse']=ration_trockensteher['kg Frischmasse']
        mischung_trockensteher['untere Lademenge']=mischung_trockensteher['kg Frischmasse']*(Anzahl_trockensteher-Varianz_trockensteher)
        mischung_trockensteher['normale Lademenge']=mischung_trockensteher['kg Frischmasse']*Anzahl_trockensteher
        mischung_trockensteher['obere Lademenge']=mischung_trockensteher['kg Frischmasse']*(Anzahl_trockensteher+Varianz_trockensteher) 
        mischung_trockensteher=mischung_trockensteher.sort_values(by=['Reihenfolge'], ascending=True)
                
        header = Label(master=Mischung_Trockensteher, text=Anzahl_trockensteher-Varianz_trockensteher, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Trockensteher, text=Anzahl_trockensteher, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Trockensteher, text=Anzahl_trockensteher +Varianz_trockensteher, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_Mischung_trockensteher:
            row.destroy()  
        number_rows=mischung_trockensteher.shape
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c>3:
                    Kasten = Label(master=Mischung_Trockensteher, bg='white',text=round(mischung_trockensteher.iloc[r,0],2))
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_trockensteher.append(Kasten)
                else:   
                    Kasten = Label(master=Mischung_Trockensteher, bg='white', text=mischung_trockensteher.iloc[r,1])            
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_trockensteher.append(Kasten)
        
        Frischmasse=mischung_trockensteher["kg Frischmasse"].sum(axis = 0, skipna = True)
        header = Label(master=Mischung_Trockensteher, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Trockensteher, text=round(Frischmasse*(Anzahl_trockensteher-Varianz_trockensteher),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Trockensteher, text=round(Frischmasse*Anzahl_trockensteher,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Trockensteher, text=round(Frischmasse*(Anzahl_trockensteher+Varianz_trockensteher),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
        
        return
    
    def buttonAktualisierenMischung_Rinder():
        global Anzahl_rinder, Varianz_rinder, mischung_rinder
        Anzahl_rinder = EntryAnzahl_Rinder.get()
        Varianz_rinder = EntryVar_Rinder.get()
        Anzahl_rinder=Anzahl_rinder.replace(',','.')
        Varianz_rinder=Varianz_rinder.replace(',','.')
        
        try:
            Anzahl_rinder=float(Anzahl_rinder)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Anzahl ist keine Zahl")
                return
    
        try:
            Varianz_rinder=float(Varianz_rinder)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Varianz ist keine Zahl")
                return
                                
        mischung_rinder['Reihenfolge']=ration_rinder['Reihenfolge']
        mischung_rinder['Komponente']=ration_rinder['Komponente']
        mischung_rinder['Bezeichnung']=ration_rinder['Bezeichnung']
        mischung_rinder['kg Frischmasse']=ration_rinder['kg Frischmasse']
        mischung_rinder['untere Lademenge']=mischung_rinder['kg Frischmasse']*(Anzahl_rinder-Varianz_rinder)
        mischung_rinder['normale Lademenge']=mischung_rinder['kg Frischmasse']*Anzahl_rinder
        mischung_rinder['obere Lademenge']=mischung_rinder['kg Frischmasse']*(Anzahl_rinder+Varianz_rinder) 
        mischung_rinder=mischung_rinder.sort_values(by=['Reihenfolge'], ascending=True)
                
        header = Label(master=Mischung_Rinder, text=Anzahl_rinder-Varianz_rinder, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Rinder, text=Anzahl_rinder, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Rinder, text=Anzahl_rinder +Varianz_rinder, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_Mischung_rinder:
            row.destroy()  
        number_rows=mischung_rinder.shape
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c>3:
                    Kasten = Label(master=Mischung_Rinder, bg='white',text=round(mischung_rinder.iloc[r,0],2))
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_rinder.append(Kasten)
                else:   
                    Kasten = Label(master=Mischung_Rinder, bg='white', text=mischung_rinder.iloc[r,1])            
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_rinder.append(Kasten)
        
        Frischmasse=mischung_rinder["kg Frischmasse"].sum(axis = 0, skipna = True)
        header = Label(master=Mischung_Rinder, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Rinder, text=round(Frischmasse*(Anzahl_rinder-Varianz_rinder),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Rinder, text=round(Frischmasse*Anzahl_rinder,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Rinder, text=round(Frischmasse*(Anzahl_rinder+Varianz_rinder),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
        
        return
    
    def buttonAktualisierenMischung_Bullen():
        global Anzahl_bullen, Varianz_bullen, mischung_bullen
        Anzahl_bullen = EntryAnzahl_Bullen.get()
        Varianz_bullen = EntryVar_Bullen.get()
        Anzahl_bullen=Anzahl_bullen.replace(',','.')
        Varianz_bullen=Varianz_bullen.replace(',','.')
        
        try:
            Anzahl_bullen=float(Anzahl_bullen)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Anzahl ist keine Zahl")
                return
    
        try:
            Varianz_bullen=float(Varianz_bullen)
        except ValueError: 
                messagebox.showerror("Error","Eingegebene Varianz ist keine Zahl")
                return
                
                
        mischung_bullen['Reihenfolge']=ration_bullen['Reihenfolge']
        mischung_bullen['Komponente']=ration_bullen['Komponente']
        mischung_bullen['Bezeichnung']=ration_bullen['Bezeichnung']
        mischung_bullen['kg Frischmasse']=ration_bullen['kg Frischmasse']
        mischung_bullen['untere Lademenge']=mischung_bullen['kg Frischmasse']*(Anzahl_bullen-Varianz_bullen)
        mischung_bullen['normale Lademenge']=mischung_bullen['kg Frischmasse']*Anzahl_bullen
        mischung_bullen['obere Lademenge']=mischung_bullen['kg Frischmasse']*(Anzahl_bullen+Varianz_bullen) 
        mischung_bullen=mischung_bullen.sort_values(by=['Reihenfolge'], ascending=True)
                
        header = Label(master=Mischung_Bullen, text=Anzahl_bullen-Varianz_bullen, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Bullen, text=Anzahl_bullen, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Bullen, text=Anzahl_bullen +Varianz_bullen, fg='black', bg='white',font="Arial 10 bold")
        header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
        
        for row in Kasten_Mischung_bullen:
            row.destroy()  
        number_rows=mischung_bullen.shape
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c>3:
                    Kasten = Label(master=Mischung_Bullen, bg='white',text=round(mischung_bullen.iloc[r,0],2))
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_bullen.append(Kasten)
                else:   
                    Kasten = Label(master=Mischung_Bullen, bg='white', text=mischung_bullen.iloc[r,1])            
                    Kasten.grid(row=r+4, column=c)
                    Kasten_Mischung_bullen.append(Kasten)
            
        
        Frischmasse=mischung_bullen["kg Frischmasse"].sum(axis = 0, skipna = True)
        header = Label(master=Mischung_Bullen, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Bullen, text=round(Frischmasse*(Anzahl_bullen-Varianz_bullen),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Bullen, text=round(Frischmasse*Anzahl_bullen,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Mischung_Bullen, text=round(Frischmasse*(Anzahl_bullen+Varianz_bullen),2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
        
        
        return

    def buttonKosten_ration():
        number_rows=ration.shape
        
        global Kosten, TS
        Kosten= [0] * number_rows[0]
        TS= [0] * number_rows[0]
        for x in range(number_rows[0]):
            Kosten[x] = entryKosten[x].get()
            TS[x] = entryTS[x].get()
            Kosten[x]=Kosten[x].replace(',','.')
            TS[x]=TS[x].replace(',','.')
            if Kosten[x]=='':
                Kosten[x]=0
            if TS[x]=='':
                TS[x]=ration.iloc[x,4]
            try:
                Kosten[x]=float(Kosten[x])
            except ValueError: 
                messagebox.showerror("Error","Eingegebene Kosten können nicht verarbeitet werden")
                return
            try:
                TS[x]=float(TS[x])
            except ValueError: 
                messagebox.showerror("Error","Ein eingegebener TS-Gehalt kann nicht verarbeitet werden")
                return
        Tk.destroy(tkFenster)
        return
    
    def buttonauswählen_ration():
        global Betrieb
        Betrieb=EingabeBetrieb.get()
        Tk.destroy(tkFenster)
        return 
    
    def buttonauswählen_ration():
        global Komponente
        Komponente=EingabeKomponente.get()
        Tk.destroy(tkFenster)
        return
    
    def Buttonauswahlanalysen_ration():
        global status1
        status1 ='fertig'
        Tk.destroy(tkFenster)
        return 

    def button_bullen_skalieren():
        TS_neu=Faktorentry_bullen.get()
        TS_alt=ration_bullen["TS"].sum(axis = 0, skipna = True)
        if TS_alt==0:
            return
        try:
           TS_neu=float(TS_neu)
        except ValueError: 
                messagebox.showerror("Error","Eingegebener Skalierfakor kann nicht verarbeitet werden")
                return
        FM_neu=TS_neu/float(TS_alt)*ration_bullen['kg Frischmasse']
        rows=FM_neu.shape
        for r in range(rows[0]):        
            entryFM_bullen[r] = Entry(master=Fenster_bullen1, bg='white')
            entryFM_bullen[r].grid(row=r+6, column=6, padx='5', pady='5', sticky='ew')
            entryFM_bullen[r].insert(0,round(FM_neu[r],2))
        return
    
    def button_rinder_skalieren():
        TS_neu=Faktorentry_rinder.get()
        TS_alt=ration_rinder["TS"].sum(axis = 0, skipna = True)
        if TS_alt==0:
            return
        try:
           TS_neu=float(TS_neu)
        except ValueError: 
                messagebox.showerror("Error","Eingegebener Skalierfakor kann nicht verarbeitet werden")
                return
        FM_neu=TS_neu/float(TS_alt)*ration_rinder['kg Frischmasse']
        rows=FM_neu.shape
        for r in range(rows[0]):        
            entryFM_rinder[r] = Entry(master=Fenster_rinder1, bg='white')
            entryFM_rinder[r].grid(row=r+6, column=6, padx='5', pady='5', sticky='ew')
            entryFM_rinder[r].insert(0,round(FM_neu[r],2))
        return
    
    def button_trockensteher_skalieren():
        TS_neu=Faktorentry_trockenstehend.get()
        TS_alt=ration_trockensteher["TS"].sum(axis = 0, skipna = True)
        if TS_alt==0:
            return
        try:
           TS_neu=float(TS_neu)
        except ValueError: 
                messagebox.showerror("Error","Eingegebener Skalierfakor kann nicht verarbeitet werden")
                return
        FM_neu=TS_neu/float(TS_alt)*ration_trockensteher['kg Frischmasse']
        rows=FM_neu.shape
        for r in range(rows[0]):        
            entryFM_trockensteher[r] = Entry(master=Fenster_trocken1, bg='white')
            entryFM_trockensteher[r].grid(row=r+6, column=6, padx='5', pady='5', sticky='ew')
            entryFM_trockensteher[r].insert(0,round(FM_neu[r],2))
        return
    
    def button_altmelker_skalieren():
        TS_neu=Faktorentry_altmelkend.get()
        TS_alt=ration_altmelker["TS"].sum(axis = 0, skipna = True)
        if TS_alt==0:
            return
        try:
           TS_neu=float(TS_neu)
        except ValueError: 
                messagebox.showerror("Error","Eingegebener Skalierfakor kann nicht verarbeitet werden")
                return
        FM_neu=TS_neu/float(TS_alt)*ration_altmelker['kg Frischmasse']
        rows=FM_neu.shape
        for r in range(rows[0]):        
            entryFM_altmelker[r] = Entry(master=Fenster_alt1, bg='white')
            entryFM_altmelker[r].grid(row=r+6, column=6, padx='5', pady='5', sticky='ew')
            entryFM_altmelker[r].insert(0,round(FM_neu[r],2))
        return
    
    def button_frischmelker_skalieren():
        TS_neu=Faktorentry_frischmelkend.get()
        TS_alt=ration_frischmelker["TS"].sum(axis = 0, skipna = True)
        if TS_alt==0:
            return
        try:
           TS_neu=float(TS_neu)
        except ValueError: 
                messagebox.showerror("Error","Eingegebener Skalierfakor kann nicht verarbeitet werden")
                return
        FM_neu=TS_neu/float(TS_alt)*ration_frischmelker['kg Frischmasse']
        rows=FM_neu.shape
        for r in range(rows[0]):        
            entryFM_frischmelker[r] = Entry(master=Fenster_frisch1, bg='white')
            entryFM_frischmelker[r].grid(row=r+6, column=6, padx='5', pady='5', sticky='ew')
            entryFM_frischmelker[r].insert(0,round(FM_neu[r],2))
        return
    
    def button_hochleistend_skalieren():
        TS_neu=Faktorentry_hochleistend.get()
        TS_alt=ration_hochleistend["TS"].sum(axis = 0, skipna = True)
        if TS_alt==0:
            return
        try:
           TS_neu=float(TS_neu)
        except ValueError: 
                messagebox.showerror("Error","Eingegebener Skalierfakor kann nicht verarbeitet werden")
                return
        FM_neu=TS_neu/float(TS_alt)*ration_hochleistend['kg Frischmasse']
        rows=FM_neu.shape
        for r in range(rows[0]):        
            entryFM_hochleistend[r] = Entry(master=tkFenster1, bg='white')
            entryFM_hochleistend[r].grid(row=r+6, column=6, padx='5', pady='5', sticky='ew')
            entryFM_hochleistend[r].insert(0,round(FM_neu[r],2))
        return
        

    print(ration)    
    Varianz=Anzahl=Milchpreis=Futterreste=Faktor=Milchmenge=Milchmenge=0    
    parent = Tk()
    n = ttk.Notebook(parent)
    f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
    n.add(f1, text='Analysen')
    if table1[0].get()==1:
        Ration  = ttk.Frame(n)   # second page
        Mischung= ttk.Frame(n)#
        n.add(Ration, text='Ration_hochleistend')
        n.add(Mischung, text='Mischung_hochleistend')
    if table1[1].get()==1:
        Ration_Frischmelker= ttk.Frame(n)   # second page
        Mischung_Frischmelker= ttk.Frame(n)#
        n.add(Ration_Frischmelker, text='Ration_Frischmelker')
        n.add(Mischung_Frischmelker, text='Mischung_Frischmelker')
    if table1[2].get()==1:
        Ration_Altmelker = ttk.Frame(n)   # second page
        Mischung_Altmelker= ttk.Frame(n)#
        n.add(Ration_Altmelker, text='Ration_Altmelker')
        n.add(Mischung_Altmelker, text='Mischung_Altmelker')
    if table1[3].get()==1:
        Ration_Trockensteher= ttk.Frame(n)   # second page
        Mischung_Trockensteher= ttk.Frame(n)#
        n.add(Ration_Trockensteher, text='Ration_Trockensteher')
        n.add(Mischung_Trockensteher, text='Mischung_Trockensteher')
    if table1[4].get()==1:
        Ration_Rinder= ttk.Frame(n)   # second page
        Mischung_Rinder= ttk.Frame(n)#
        n.add(Ration_Rinder, text='Ration_Rinder')
        n.add(Mischung_Rinder, text='Mischung_Rinder')
    if table1[5].get()==1:
        Ration_Bullen  = ttk.Frame(n)   # second page
        Mischung_Bullen= ttk.Frame(n)#
        n.add(Ration_Bullen, text='Ration_Bullen')
        n.add(Mischung_Bullen, text='Mischung_Bullen')
    
    n.grid(row=1)
    
    number_rows=ration.shape 
    f1.grid_rowconfigure(0, weight=1)
    f1.columnconfigure(0, weight=1)
    frame_main = Frame(f1,  bg="gray85")
    frame_main.grid(sticky='news')
    
    
    frame_canvas = Frame(frame_main)
    frame_canvas.grid(row=0, column=0, pady=(5, 0), sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    frame_buttons = Frame(frame_main)
    frame_buttons.grid(row=1, column=0, pady=(5, 0), sticky='nw')
    frame_buttons.grid_rowconfigure(0, weight=1)
    frame_buttons.grid_columnconfigure(0, weight=1)
    canvas = Canvas(frame_canvas,width=1500, height=32*(number_rows[0]+1), bg="gray85")
    canvas.grid(row=1, column=0, sticky="news")
    
    hsbar = Scrollbar(frame_canvas, orient='horizontal', command=canvas.xview)
    hsbar.grid(row=2, column=0, sticky='ew')
    canvas.configure(xscrollcommand=hsbar.set)
    
    vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    vsb.grid(row=1, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)
    
    frame_labels = Frame(canvas, bg="gray85")
    canvas.create_window((0, 0), window=frame_labels, anchor='nw')
    
    for r in range(number_rows[0]):
        for c in range(25):
            if c>3:
                Kasten = Label(master=frame_labels, bg='white', text=round(ration.iloc[r,c],2))
                Kasten.grid(row=r+1, column=c, padx='5', pady='5', sticky='ew')
            else:
                Kasten = Label(master=frame_labels, bg='white', text=ration.iloc[r,c])
                Kasten.grid(row=r+1, column=c, padx='5', pady='5', sticky='ew')
    c=0
    for col in ration.columns: 
        if c>=25:
            continue
        else:
            Kasten = Label(master=frame_labels, bg='white', text=col,font='Arial 12 bold', height = 1)
            Kasten.grid(row=0, column=c, padx='3', pady='3')
            c=c+1
    
    buttonmineral = Button(master=frame_buttons, bg='#FBD975', text='Mineralfutter\n hinzufügen',font='Arial 12 bold', command=buttonMineral)
    buttonmineral.grid(row=3, column=0, padx='5', pady='5', sticky='ew')
    buttonTrocken = Button(master=frame_buttons, bg='#FBD975', text='Trockene Komponente\n hinzufügen',font='Arial 12 bold', command=buttonTrocken)
    buttonTrocken.grid(row=3, column=1, padx='5', pady='5', sticky='ew')
    buttonFeucht = Button(master=frame_buttons, bg='#FBD975', text='Feuchte Komponente\n hinzufügen',font='Arial 12 bold', command=buttonFeucht)
    buttonFeucht.grid(row=3, column=2, padx='5', pady='5', sticky='ew')
    buttonKosten = Button(master=frame_buttons, bg='#FBD975', text='Kosten oder TS\n ändern',font='Arial 12 bold', command=button_Kosten)
    buttonKosten.grid(row=3, column=3, padx='5', pady='5', sticky='ew')
    buttonGruppen= Button(master=frame_buttons, bg='#FBD975', text='Gruppen hinzufügen\n oder löschen',font='Arial 12 bold', command=buttonGruppen)
    buttonGruppen.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
    buttonAnalysen= Button(master=frame_buttons, bg='#FBD975', text='Grundfutteranalysen',font='Arial 12 bold', command=buttonAnalysen)
    buttonAnalysen.grid(row=4, column=1, padx='5', pady='5', sticky='ew')    
    buttonKomponenten= Button(master=frame_buttons, bg='#FBD975', text='Komponentensuche',font='Arial 12 bold', command=buttonKomponenten)
    buttonKomponenten.grid(row=4, column=2, padx='5', pady='5', sticky='ew')
    buttonBeenden= Button(master=frame_buttons, bg='#FBD975', text='Beenden',font='Arial 12 bold', command=buttonBeenden)
    buttonBeenden.grid(row=4, column=3, padx='5', pady='5', sticky='ew')
    
    
    table=[]
    number_rows=ration.shape 
    Frischmasse=0
    TS=0
    MJNEL=0
    PTS=0
    MJNELkg=0
    NDF=0
    GNDF=0
    NFC=0
    RP=0
    Staerke=0    
    Asche=0
    Ca=0
    P=0
    Mg=0
    K=0     
    Na=0
    S=0    
    Kosten=0
    KMg=0
    Kosten=0
    if Mg==0:
        KMg=0
    else:
        KMg=K/Mg
    
    
    Kostenplus=Kosten*(float(Futterreste)/100+1)
    Umsatz=Milchmenge*Milchpreis
    IOFC=Umsatz-Kosten
    for x in range(len(table1)):
        if x==0 and table1[x].get()==1:
            Ration.grid_rowconfigure(0, weight=1)
            Ration.columnconfigure(0, weight=1)
            frame_main = Frame(Ration,  bg="gray85")
            frame_main.grid(sticky='nw')
        
            frame_canvas = Frame(frame_main)
            frame_canvas.grid(row=0, column=0, pady=(0, 0), sticky='nw')
            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)
            
            frame_canvas1 = Frame(frame_main)
            frame_canvas1.grid(row=1, column=0, pady=(5, 0), sticky='nw')
            frame_canvas1.grid_rowconfigure(0, weight=1)
            frame_canvas1.grid_columnconfigure(0, weight=1)
        #    
            canvas = Canvas(frame_canvas,width=1500, height=190, bg="gray85")
            canvas.grid(row=1, column=0, sticky="news")
        #    
            canvas1 = Canvas(frame_canvas1,width=1500, height=number_rows[0]*30, bg="green")
            canvas1.grid(row=2, column=0, sticky="news")
        #    
            hsbar = Scrollbar(frame_canvas, orient='horizontal', command=canvas.xview)
            hsbar.grid(row=2, column=0, sticky='ew')
            canvas.configure(xscrollcommand=hsbar.set)
            
            vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
            vsb.grid(row=1, column=1, sticky='ns')
            canvas.configure(yscrollcommand=vsb.set)
        #    
            vsb1 = Scrollbar(frame_canvas1, orient="vertical", command=canvas1.yview)
            vsb1.grid(row=2, column=1, sticky='ns')
            canvas1.configure(yscrollcommand=vsb1.set)
            
            hsbar1 = Scrollbar(frame_canvas1, orient='horizontal', command=canvas1.xview)
            hsbar1.grid(row=3, column=0, sticky='ew')
            canvas1.configure(xscrollcommand=hsbar1.set)
        #    
            tkFenster = Frame(canvas, bg="gray85")
            canvas.create_window((0, 0), window=tkFenster, anchor='nw')
        #    
            tkFenster1 = Frame(canvas1, bg="gray85")
            canvas1.create_window((0, 0), window=tkFenster1, anchor='nw')
            
            Richtwert_Frischmasse=24
            Richtwert_Energie=7.1
            Richtwert_NDF=30
            Richtwert_GNDF="21-24"
            Richtwert_NFC= 40
            Richtwert_RP="17-17.5"
            Richtwert_Staerke="24-28"
            Richtwert_Ca=0.7
            Richtwert_P=0.45
            Richtwert_Mg=0.35
            Richtwert_K=">1"
            Richtwert_Na=0.35
            Richtwert_S=""
            Richtwert_KMG=""
            
            Fenster=tkFenster
            Fenster1=tkFenster1
        
        if x==0 and table1[x].get()!=1:
            continue
        
        if x==1 and table1[x].get()==1:
            Ration_Frischmelker.grid_rowconfigure(0, weight=1)
            Ration_Frischmelker.columnconfigure(0, weight=1)
            frame_main_frisch = Frame(Ration_Frischmelker,  bg="gray85")
            frame_main_frisch.grid(sticky='nw')
        
            frame_canvas = Frame(frame_main_frisch)
            frame_canvas.grid(row=0, column=0, pady=(0, 0), sticky='nw')
            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)
            
            frame_canvas1 = Frame(frame_main_frisch)
            frame_canvas1.grid(row=1, column=0, pady=(5, 0), sticky='nw')
            frame_canvas1.grid_rowconfigure(0, weight=1)
            frame_canvas1.grid_columnconfigure(0, weight=1)
        #    
            canvas = Canvas(frame_canvas,width=1500, height=190, bg="gray85")
            canvas.grid(row=1, column=0, sticky="news")
        #    
            canvas1 = Canvas(frame_canvas1,width=1500, height=number_rows[0]*30, bg="green")
            canvas1.grid(row=2, column=0, sticky="news")
        #    
            hsbar = Scrollbar(frame_canvas, orient='horizontal', command=canvas.xview)
            hsbar.grid(row=2, column=0, sticky='ew')
            canvas.configure(xscrollcommand=hsbar.set)
            
            vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
            vsb.grid(row=1, column=1, sticky='ns')
            canvas.configure(yscrollcommand=vsb.set)
        #    
            vsb1 = Scrollbar(frame_canvas1, orient="vertical", command=canvas1.yview)
            vsb1.grid(row=2, column=1, sticky='ns')
            canvas1.configure(yscrollcommand=vsb1.set)
            
            hsbar1 = Scrollbar(frame_canvas1, orient='horizontal', command=canvas1.xview)
            hsbar1.grid(row=3, column=0, sticky='ew')
            canvas1.configure(xscrollcommand=hsbar1.set)
        #    
            Fenster_frisch = Frame(canvas, bg="gray85")
            canvas.create_window((0, 0), window=Fenster_frisch, anchor='nw')
        #    
            Fenster_frisch1 = Frame(canvas1, bg="gray85")
            canvas1.create_window((0, 0), window=Fenster_frisch1, anchor='nw')
            
            Richtwert_Frischmasse=19
            Richtwert_Energie=6.9
            Richtwert_NDF="30-34"
            Richtwert_GNDF=24
            Richtwert_NFC= "35-38"
            Richtwert_RP="15.5-16"
            Richtwert_Staerke="22"
            Richtwert_Ca=0.7
            Richtwert_P=0.45
            Richtwert_Mg=0.35
            Richtwert_K=">1"
            Richtwert_Na=0.35
            Richtwert_S=""
            Richtwert_KMG=""
            Richtwert_S=""
            
            Fenster=Fenster_frisch
            Fenster1=Fenster_frisch1
            
        if x==1 and table1[x].get()!=1:
            continue
            
        if x==2 and table1[x].get()==1:
            Ration_Altmelker.grid_rowconfigure(0, weight=1)
            Ration_Altmelker.columnconfigure(0, weight=1)
            frame_main_alt = Frame(Ration_Altmelker,  bg="gray85")
            frame_main_alt.grid(sticky='nw')
        
            frame_canvas = Frame(frame_main_alt)
            frame_canvas.grid(row=0, column=0, pady=(0, 0), sticky='nw')
            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)
            
            frame_canvas1 = Frame(frame_main_alt)
            frame_canvas1.grid(row=1, column=0, pady=(5, 0), sticky='nw')
            frame_canvas1.grid_rowconfigure(0, weight=1)
            frame_canvas1.grid_columnconfigure(0, weight=1)
        #    
            canvas = Canvas(frame_canvas,width=1500, height=190, bg="gray85")
            canvas.grid(row=1, column=0, sticky="news")
        #    
            canvas1 = Canvas(frame_canvas1,width=1500, height=number_rows[0]*30, bg="green")
            canvas1.grid(row=2, column=0, sticky="news")
        #    
            hsbar = Scrollbar(frame_canvas, orient='horizontal', command=canvas.xview)
            hsbar.grid(row=2, column=0, sticky='ew')
            canvas.configure(xscrollcommand=hsbar.set)
            
            vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
            vsb.grid(row=1, column=1, sticky='ns')
            canvas.configure(yscrollcommand=vsb.set)
        #    
            vsb1 = Scrollbar(frame_canvas1, orient="vertical", command=canvas1.yview)
            vsb1.grid(row=2, column=1, sticky='ns')
            canvas1.configure(yscrollcommand=vsb1.set)
            
            hsbar1 = Scrollbar(frame_canvas1, orient='horizontal', command=canvas1.xview)
            hsbar1.grid(row=3, column=0, sticky='ew')
            canvas1.configure(xscrollcommand=hsbar1.set)
        #    
            Fenster_alt = Frame(canvas, bg="gray85")
            canvas.create_window((0, 0), window=Fenster_alt, anchor='nw')
        #    
            Fenster_alt1 = Frame(canvas1, bg="gray85")
            canvas1.create_window((0, 0), window=Fenster_alt1, anchor='nw')
            
            Richtwert_Frischmasse=19
            Richtwert_Energie=6.9
            Richtwert_NDF="30-34"
            Richtwert_GNDF=24
            Richtwert_NFC= "35-38"
            Richtwert_RP="15.5-16"
            Richtwert_Staerke="22"
            Richtwert_Ca=0.7
            Richtwert_P=0.45
            Richtwert_Mg=0.35
            Richtwert_K=">1"
            Richtwert_Na=0.35
            Richtwert_S=""
            Richtwert_KMG=""
            Richtwert_S=""
            
            Fenster=Fenster_alt
            Fenster1=Fenster_alt1
        
        if x==2 and table1[x].get()!=1:
            continue
            
        if x==3 and table1[x].get()==1:
            Ration_Trockensteher.grid_rowconfigure(0, weight=1)
            Ration_Trockensteher.columnconfigure(0, weight=1)
            frame_main_trocken = Frame(Ration_Trockensteher,  bg="gray85")
            frame_main_trocken.grid(sticky='nw')
        
            frame_canvas = Frame(frame_main_trocken)
            frame_canvas.grid(row=0, column=0, pady=(0, 0), sticky='nw')
            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)
            
            frame_canvas1 = Frame(frame_main_trocken)
            frame_canvas1.grid(row=1, column=0, pady=(5, 0), sticky='nw')
            frame_canvas1.grid_rowconfigure(0, weight=1)
            frame_canvas1.grid_columnconfigure(0, weight=1)
        #    
            canvas = Canvas(frame_canvas,width=1500, height=190, bg="gray85")
            canvas.grid(row=1, column=0, sticky="news")
        #    
            canvas1 = Canvas(frame_canvas1,width=1500, height=number_rows[0]*30, bg="green")
            canvas1.grid(row=2, column=0, sticky="news")
        #    
            hsbar = Scrollbar(frame_canvas, orient='horizontal', command=canvas.xview)
            hsbar.grid(row=2, column=0, sticky='ew')
            canvas.configure(xscrollcommand=hsbar.set)
            
            vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
            vsb.grid(row=1, column=1, sticky='ns')
            canvas.configure(yscrollcommand=vsb.set)
        #    
            vsb1 = Scrollbar(frame_canvas1, orient="vertical", command=canvas1.yview)
            vsb1.grid(row=2, column=1, sticky='ns')
            canvas1.configure(yscrollcommand=vsb1.set)
            
            hsbar1 = Scrollbar(frame_canvas1, orient='horizontal', command=canvas1.xview)
            hsbar1.grid(row=3, column=0, sticky='ew')
            canvas1.configure(xscrollcommand=hsbar1.set)
        #    
            Fenster_trocken = Frame(canvas, bg="gray85")
            canvas.create_window((0, 0), window=Fenster_trocken, anchor='nw')
        #    
            Fenster_trocken1 = Frame(canvas1, bg="gray85")
            canvas1.create_window((0, 0), window=Fenster_trocken1, anchor='nw')
            
            Richtwert_Frischmasse=12.5
            Richtwert_Energie=5.7
            Richtwert_NDF="48"
            Richtwert_GNDF="45-49"
            Richtwert_NFC= 28
            Richtwert_RP="14"
            Richtwert_Staerke=15
            Richtwert_Ca=">1"
            Richtwert_P="<0.4"
            Richtwert_Mg="<0.4"
            Richtwert_K=""
            Richtwert_Na=0.1
            Richtwert_S=0.2
            Richtwert_KMG=">4"
            
            Fenster=Fenster_trocken
            Fenster1=Fenster_trocken1
                
        if x==3 and table1[x].get()!=1:
            continue
            
        if x==4 and table1[x].get()==1:
            Ration_Rinder.grid_rowconfigure(0, weight=1)
            Ration_Rinder.columnconfigure(0, weight=1)
            frame_main_rinder = Frame(Ration_Rinder,  bg="gray85")
            frame_main_rinder.grid(sticky='nw')
        
            frame_canvas = Frame(frame_main_rinder)
            frame_canvas.grid(row=0, column=0, pady=(0, 0), sticky='nw')
            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)
            
            frame_canvas1 = Frame(frame_main_rinder)
            frame_canvas1.grid(row=1, column=0, pady=(5, 0), sticky='nw')
            frame_canvas1.grid_rowconfigure(0, weight=1)
            frame_canvas1.grid_columnconfigure(0, weight=1)
        #    
            canvas = Canvas(frame_canvas,width=1500, height=190, bg="gray85")
            canvas.grid(row=1, column=0, sticky="news")
        #    
            canvas1 = Canvas(frame_canvas1,width=1500, height=number_rows[0]*30, bg="green")
            canvas1.grid(row=2, column=0, sticky="news")
        #    
            hsbar = Scrollbar(frame_canvas, orient='horizontal', command=canvas.xview)
            hsbar.grid(row=2, column=0, sticky='ew')
            canvas.configure(xscrollcommand=hsbar.set)
            
            vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
            vsb.grid(row=1, column=1, sticky='ns')
            canvas.configure(yscrollcommand=vsb.set)
        #    
            vsb1 = Scrollbar(frame_canvas1, orient="vertical", command=canvas1.yview)
            vsb1.grid(row=2, column=1, sticky='ns')
            canvas1.configure(yscrollcommand=vsb1.set)
            
            hsbar1 = Scrollbar(frame_canvas1, orient='horizontal', command=canvas1.xview)
            hsbar1.grid(row=3, column=0, sticky='ew')
            canvas1.configure(xscrollcommand=hsbar1.set)
        #    
            Fenster_rinder = Frame(canvas, bg="gray85")
            canvas.create_window((0, 0), window=Fenster_rinder, anchor='nw')
        #    
            Fenster_rinder1 = Frame(canvas1, bg="gray85")
            canvas1.create_window((0, 0), window=Fenster_rinder1, anchor='nw')
            
            Richtwert_Frischmasse=10
            Richtwert_Energie=5.5
            Richtwert_NDF="45"
            Richtwert_GNDF="45"
            Richtwert_NFC= ""
            Richtwert_RP="12"
            Richtwert_Staerke=""
            Richtwert_Ca=0.3
            Richtwert_P=""
            Richtwert_Mg=0.2
            Richtwert_K=""
            Richtwert_Na=""
            Richtwert_S=""
            Richtwert_KMG=""
            Richtwert_S=""
            
            Fenster=Fenster_rinder
            Fenster1=Fenster_rinder1
            
        if x==4 and table1[x].get()!=1:
            continue
            
        if x==5 and table1[x].get()==1:
            Ration_Bullen.grid_rowconfigure(0, weight=1)
            Ration_Bullen.columnconfigure(0, weight=1)
            frame_main_bullen = Frame(Ration_Bullen,  bg="blue")
            frame_main_bullen.grid(sticky='nw')
        
            frame_canvas = Frame(frame_main_bullen)
            frame_canvas.grid(row=0, column=0, pady=(0, 0), sticky='nw')
            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)
            
            frame_canvas1 = Frame(frame_main_bullen)
            frame_canvas1.grid(row=1, column=0, pady=(5, 0), sticky='nw')
            frame_canvas1.grid_rowconfigure(0, weight=1)
            frame_canvas1.grid_columnconfigure(0, weight=1)
        #    
            canvas = Canvas(frame_canvas,width=1500, height=190, bg="gray85")
            canvas.grid(row=1, column=0, sticky="news")
        #    
            canvas1 = Canvas(frame_canvas1,width=1500, height=number_rows[0]*30, bg="green")
            canvas1.grid(row=2, column=0, sticky="news")
        #    
            hsbar = Scrollbar(frame_canvas, orient='horizontal', command=canvas.xview)
            hsbar.grid(row=2, column=0, sticky='ew')
            canvas.configure(xscrollcommand=hsbar.set)
            
            vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
            vsb.grid(row=1, column=1, sticky='ns')
            canvas.configure(yscrollcommand=vsb.set)
        #    
            vsb1 = Scrollbar(frame_canvas1, orient="vertical", command=canvas1.yview)
            vsb1.grid(row=2, column=1, sticky='ns')
            canvas1.configure(yscrollcommand=vsb1.set)
            
            hsbar1 = Scrollbar(frame_canvas1, orient='horizontal', command=canvas1.xview)
            hsbar1.grid(row=3, column=0, sticky='ew')
            canvas1.configure(xscrollcommand=hsbar1.set)
        #    
            Fenster_bullen = Frame(canvas, bg="gray85")
            canvas.create_window((0, 0), window=Fenster_bullen, anchor='nw')
        #    
            Fenster_bullen1 = Frame(canvas1, bg="gray85")
            canvas1.create_window((0, 0), window=Fenster_bullen1, anchor='nw')
            
            Richtwert_Frischmasse=""
            Richtwert_Energie=""
            Richtwert_NDF=""
            Richtwert_GNDF=""
            Richtwert_NFC= ""
            Richtwert_RP=""
            Richtwert_Staerke=""
            Richtwert_Ca=""
            Richtwert_P=""
            Richtwert_Mg=""
            Richtwert_K=""
            Richtwert_Na=""
            Richtwert_S=""
            Richtwert_KMG=""
            Richtwert_S=""
            
            Fenster=Fenster_bullen
            Fenster1=Fenster_bullen1
            
        if x==5 and table1[x].get()!=1:
            continue
            
        
        header = Label(master=Fenster, text='Frischmasse:\n (realer Wert)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='TS (kg)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=1, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='% TS', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=2, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='MJ NEL', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=3, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='MJ NEL/kg TS', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=4, column=0, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text=round(Frischmasse,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(TS,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(PTS,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(MJNEL,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(MJNELkg,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=1, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold ")
        header.grid(row=0, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=Richtwert_Frischmasse, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=Richtwert_Energie, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=2, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text='NDF (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=0, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='GNDF (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='NFC (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=2, column=3, padx='1', pady='1', sticky='ew') 
        header = Label(master=Fenster, text='RP (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=3, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='Stärke', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=4, column=3, padx='1', pady='1', sticky='ew')   
        
        header = Label(master=Fenster, text=round(NDF,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(GNDF,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(NFC,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(RP,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(Staerke,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=4, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text=Richtwert_NDF, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=Richtwert_GNDF, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=Richtwert_NFC, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=Richtwert_RP, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=Richtwert_Staerke, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=5, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text='Asche (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=0, column=6, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='Ca (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=1, column=6, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='P', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=2, column=6, padx='1', pady='1', sticky='ew') 
        header = Label(master=Fenster, text='Mg (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=3, column=6, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='K (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=4, column=6, padx='1', pady='1', sticky='ew')   
        
        header = Label(master=Fenster, text=round(Asche,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(Ca,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(P,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(Mg,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=7, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(K,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=7, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text=" ", fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=8, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=Richtwert_Ca, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=8, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=Richtwert_P, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=8, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=Richtwert_Mg, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=8, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=Richtwert_K, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=8, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text='Na (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=0, column=9, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='S (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=1, column=9, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='K/Mg', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=2, column=9, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='Skalierung', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=4, column=9, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text=round(Na,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(S,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(KMg,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=10, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text=Richtwert_Na, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=11, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster,text=Richtwert_S, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=11, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster,text=Richtwert_KMG, fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=11, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster,text="Kg in TS", fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=11, padx='1', pady='1', sticky='ew')
        
        #header = Label(master=tkFenster, text='Annahmen', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        #header.grid(row=0, column=12-14, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='Futterreste', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=0, column=12, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='Milchmenge', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=1, column=12, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='Milchpreis', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=2, column=12, padx='1', pady='1', sticky='ew')

        
        if x==0:
            Futterresteentry_hochleistend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Futterresteentry_hochleistend.grid(row=0, column=13, padx='1', pady='1', sticky='ew')
            Futterresteentry_hochleistend.insert(0,Futterreste)
            Milchertragentry_hochleistend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchertragentry_hochleistend.grid(row=1, column=13, padx='1', pady='1', sticky='ew')
            Milchertragentry_hochleistend.insert(0,Milchmenge)
            Milchpreisentry_hochleistend= Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchpreisentry_hochleistend.grid(row=2, column=13, padx='1', pady='1', sticky='ew')
            Milchpreisentry_hochleistend.insert(0,Milchpreis)
            Faktorentry_hochleistend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Faktorentry_hochleistend.grid(row=4, column=10, padx='1', pady='1', sticky='ew')
            Faktorentry_hochleistend.insert(0,Faktor)
            ButtonSkala = Button(master=Fenster, bg='#FBD975', text='skalieren', font='Arial 12 bold',command=button_hochleistend_skalieren)
            ButtonSkala.grid(row=4, column=12, padx='5', pady='5', sticky='ew')
            
        if x==1:
            Futterresteentry_frischmelkend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Futterresteentry_frischmelkend.grid(row=0, column=13, padx='1', pady='1', sticky='ew')
            Futterresteentry_frischmelkend.insert(0,Futterreste)
            Milchertragentry_frischmelkend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchertragentry_frischmelkend.grid(row=1, column=13, padx='1', pady='1', sticky='ew')
            Milchertragentry_frischmelkend.insert(0,Milchmenge)
            Milchpreisentry_frischmelkend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchpreisentry_frischmelkend.grid(row=2, column=13, padx='1', pady='1', sticky='ew')
            Milchpreisentry_frischmelkend.insert(0,Milchpreis)
            Faktorentry_frischmelkend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Faktorentry_frischmelkend.grid(row=4, column=10, padx='1', pady='1', sticky='ew')
            Faktorentry_frischmelkend.insert(0,Faktor)
            ButtonSkala = Button(master=Fenster, bg='#FBD975', text='skalieren', font='Arial 12 bold',command=button_frischmelker_skalieren)
            ButtonSkala.grid(row=4, column=12, padx='5', pady='5', sticky='ew')
            
        if x==2:
            Futterresteentry_altmelkend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Futterresteentry_altmelkend.grid(row=0, column=13, padx='1', pady='1', sticky='ew')
            Futterresteentry_altmelkend.insert(0,Futterreste)
            Milchertragentry_altmelkend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchertragentry_altmelkend.grid(row=1, column=13, padx='1', pady='1', sticky='ew')
            Milchertragentry_altmelkend.insert(0,Milchmenge)
            Milchpreisentry_altmelkend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchpreisentry_altmelkend.grid(row=2, column=13, padx='1', pady='1', sticky='ew')
            Milchpreisentry_altmelkend.insert(0,Milchpreis)
            Faktorentry_altmelkend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Faktorentry_altmelkend.grid(row=4, column=10, padx='1', pady='1', sticky='ew')
            Faktorentry_altmelkend.insert(0,Faktor)
            ButtonSkala = Button(master=Fenster, bg='#FBD975', text='skalieren', font='Arial 12 bold',command=button_altmelker_skalieren)
            ButtonSkala.grid(row=4, column=12, padx='5', pady='5', sticky='ew')
        
        if x==3:
            Futterresteentry_trockenstehend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Futterresteentry_trockenstehend.grid(row=0, column=13, padx='1', pady='1', sticky='ew')
            Futterresteentry_trockenstehend.insert(0,Futterreste)
            Milchertragentry_trockenstehend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchertragentry_trockenstehend.grid(row=1, column=13, padx='1', pady='1', sticky='ew')
            Milchertragentry_trockenstehend.insert(0,Milchmenge)
            Milchpreisentry_trockenstehend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchpreisentry_trockenstehend.grid(row=2, column=13, padx='1', pady='1', sticky='ew')
            Milchpreisentry_trockenstehend.insert(0,Milchpreis)
            Faktorentry_trockenstehend = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Faktorentry_trockenstehend.grid(row=4, column=10, padx='1', pady='1', sticky='ew')
            Faktorentry_trockenstehend.insert(0,Faktor)
            ButtonSkala = Button(master=Fenster, bg='#FBD975', text='skalieren', font='Arial 12 bold',command=button_trockensteher_skalieren)
            ButtonSkala.grid(row=4, column=12, padx='5', pady='5', sticky='ew')
            
        if x==4:
            Futterresteentry_rinder = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Futterresteentry_rinder.grid(row=0, column=13, padx='1', pady='1', sticky='ew')
            Futterresteentry_rinder.insert(0,Futterreste)
            Milchertragentry_rinder = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchertragentry_rinder.grid(row=1, column=13, padx='1', pady='1', sticky='ew')
            Milchertragentry_rinder.insert(0,Milchmenge)
            Milchpreisentry_rinder = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchpreisentry_rinder.grid(row=2, column=13, padx='1', pady='1', sticky='ew')
            Milchpreisentry_rinder.insert(0,Milchpreis)
            Faktorentry_rinder = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Faktorentry_rinder.grid(row=4, column=10, padx='1', pady='1', sticky='ew')
            Faktorentry_rinder.insert(0,Faktor)
            ButtonSkala = Button(master=Fenster, bg='#FBD975', text='skalieren', font='Arial 12 bold',command=button_rinder_skalieren)
            ButtonSkala.grid(row=4, column=12, padx='5', pady='5', sticky='ew')
            
        if x==5:
            Futterresteentry_bullen = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Futterresteentry_bullen.grid(row=0, column=13, padx='1', pady='1', sticky='ew')
            Futterresteentry_bullen.insert(0,Futterreste)
            Milchertragentry_bullen = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchertragentry_bullen.grid(row=1, column=13, padx='1', pady='1', sticky='ew')
            Milchertragentry_bullen.insert(0,Milchmenge)
            Milchpreisentry_bullen = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Milchpreisentry_bullen.grid(row=2, column=13, padx='1', pady='1', sticky='ew')
            Milchpreisentry_bullen.insert(0,Milchpreis)
            Faktorentry_bullen = Entry(master=Fenster, fg='black', bg='white',width = 12,font="Arial 10 bold")
            Faktorentry_bullen.grid(row=4, column=10, padx='1', pady='1', sticky='ew')
            Faktorentry_bullen.insert(0,Faktor)
            ButtonSkala = Button(master=Fenster, bg='#FBD975', text='skalieren', font='Arial 12 bold',command=button_bullen_skalieren)
            ButtonSkala.grid(row=4, column=12, padx='5', pady='5', sticky='ew')
        
        #header = Label(master=tkFenster, text="€/Kuh/Tag", fg='black', bg='yellow',width = 12, height = 2,)
        #header.grid(row=0, column=14, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text="%", fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=14, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text="kg Milch/\nKuh/Tag", fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=14, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text="ct/kg Milch", fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=14, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=" ", fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=14, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text='Kosten', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=0, column=15, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='Kosten +\n Futterreste', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=1, column=15, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='IOFC', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=2, column=15, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text='Umsatz', fg='black', bg='white',width = 12, height = 2,font="Arial 11 bold")
        header.grid(row=3, column=15, padx='1', pady='1', sticky='ew')
        #header = Label(master=tkFenster, text='Faktor', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        #header.grid(row=4, column=15, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text=round(Kosten,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(Kostenplus,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(IOFC,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text=round(Umsatz,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=16, padx='1', pady='1', sticky='ew')
        
        header = Label(master=Fenster, text="€/Kuh/Tag", fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=17, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text="€/Kuh/Tag", fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=17, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text="€/Kuh/Tag", fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=17, padx='1', pady='1', sticky='ew')
        header = Label(master=Fenster, text="€/Kuh/Tag", fg='black', bg='yellow',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=17, padx='1', pady='1', sticky='ew')
        #header = Label(master=tkFenster, text=" ", fg='black', bg='yellow',width = 12, height = 2,)
        #header.grid(row=4, column=14, padx='1', pady='1', sticky='ew')
        
        #s = ttk.Separator(header, orient=HORIZONTAL)
        number_rows=ration_hochleistend.shape 
        

        
        if x==0:
            Kasten_hochleistend=[]
            entryRf_hochleistend=[0] * number_rows[0]
            entryFM_hochleistend=[0] * number_rows[0]
            c=0
            for col in ration_hochleistend.columns: 
                Kasten = Label(master=Fenster1, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=5, column=c, padx='5', pady='5')
                c=c+1
            
            for r in range(number_rows[0]):
                for c in range(number_rows[1]):        
                    if c==0:
                        entryRf_hochleistend[r] = Entry(master=Fenster1, bg='white')
                        entryRf_hochleistend[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryRf_hochleistend[r].insert(0,ration_hochleistend.iloc[r,c])
                    elif c==6:
                        entryFM_hochleistend[r] = Entry(master=Fenster1, bg='white')
                        entryFM_hochleistend[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryFM_hochleistend[r].insert(0,ration_hochleistend.iloc[r,c])
                    elif c>5:
                        Kasten = Label(master=Fenster1, bg='white', text=round(ration_hochleistend.iloc[r,c],2))
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_hochleistend.append(Kasten)
                    else:
                        Kasten = Label(master=Fenster1, bg='white', text=ration_hochleistend.iloc[r,c])
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_hochleistend.append(Kasten)
                        
        if x==1:
            Kasten_frischmelker=[]
            entryRf_frischmelker=[0] * number_rows[0]
            entryFM_frischmelker=[0] * number_rows[0]
            c=0
            for col in ration_frischmelker.columns: 
                Kasten = Label(master=Fenster1, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=5, column=c, padx='5', pady='5')
                c=c+1
            
            for r in range(number_rows[0]):
                for c in range(number_rows[1]):        
                    if c==0:
                        entryRf_frischmelker[r] = Entry(master=Fenster1, bg='white')
                        entryRf_frischmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryRf_frischmelker[r].insert(0,ration_frischmelker.iloc[r,c])
                    elif c==6:
                        entryFM_frischmelker[r] = Entry(master=Fenster1, bg='white')
                        entryFM_frischmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryFM_frischmelker[r].insert(0,ration_frischmelker.iloc[r,c])
                    elif c>5:
                        Kasten = Label(master=Fenster1, bg='white', text=round(ration_frischmelker.iloc[r,c],2))
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_frischmelker.append(Kasten)
                    else:
                        Kasten = Label(master=Fenster1, bg='white', text=ration_frischmelker.iloc[r,c])
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_frischmelker.append(Kasten)
                        
        if x==2:
            Kasten_altmelker=[]
            entryRf_altmelker=[0] * number_rows[0]
            entryFM_altmelker=[0] * number_rows[0]
            c=0
            for col in ration_altmelker.columns: 
                Kasten = Label(master=Fenster1, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=5, column=c, padx='5', pady='5')
                c=c+1
            
            for r in range(number_rows[0]):
                for c in range(number_rows[1]):        
                    if c==0:
                        entryRf_altmelker[r] = Entry(master=Fenster1, bg='white')
                        entryRf_altmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryRf_altmelker[r].insert(0,ration_altmelker.iloc[r,c])
                    elif c==6:
                        entryFM_altmelker[r] = Entry(master=Fenster1, bg='white')
                        entryFM_altmelker[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryFM_altmelker[r].insert(0,ration_altmelker.iloc[r,c])
                    elif c>5:
                        Kasten = Label(master=Fenster1, bg='white', text=round(ration_altmelker.iloc[r,c],2))
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_altmelker.append(Kasten)
                    else:
                        Kasten = Label(master=Fenster1, bg='white', text=ration_altmelker.iloc[r,c])
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_altmelker.append(Kasten)
        
        if x==3:
            Kasten_trockensteher=[]
            entryRf_trockensteher=[0] * number_rows[0]
            entryFM_trockensteher=[0] * number_rows[0]
            c=0
            for col in ration_trockensteher.columns: 
                Kasten = Label(master=Fenster1, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=5, column=c, padx='5', pady='5')
                c=c+1
            
            for r in range(number_rows[0]):
                for c in range(number_rows[1]):        
                    if c==0:
                        entryRf_trockensteher[r] = Entry(master=Fenster1, bg='white')
                        entryRf_trockensteher[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryRf_trockensteher[r].insert(0,ration_trockensteher.iloc[r,c])
                    elif c==6:
                        entryFM_trockensteher[r] = Entry(master=Fenster1, bg='white')
                        entryFM_trockensteher[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryFM_trockensteher[r].insert(0,ration_trockensteher.iloc[r,c])
                    elif c>5:
                        Kasten = Label(master=Fenster1, bg='white', text=round(ration_trockensteher.iloc[r,c],2))
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_trockensteher.append(Kasten)
                    else:
                        Kasten = Label(master=Fenster1, bg='white', text=ration_trockensteher.iloc[r,c])
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_trockensteher.append(Kasten)
                        
        if x==4:
            Kasten_rinder=[]
            entryRf_rinder=[0] * number_rows[0]
            entryFM_rinder=[0] * number_rows[0]
            c=0
            for col in ration_rinder.columns: 
                Kasten = Label(master=Fenster1, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=5, column=c, padx='5', pady='5')
                c=c+1
            
            for r in range(number_rows[0]):
                for c in range(number_rows[1]):        
                    if c==0:
                        entryRf_rinder[r] = Entry(master=Fenster1, bg='white')
                        entryRf_rinder[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryRf_rinder[r].insert(0,ration_rinder.iloc[r,c])
                    elif c==6:
                        entryFM_rinder[r] = Entry(master=Fenster1, bg='white')
                        entryFM_rinder[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryFM_rinder[r].insert(0,ration_rinder.iloc[r,c])
                    elif c>5:
                        Kasten = Label(master=Fenster1, bg='white', text=round(ration_rinder.iloc[r,c],2))
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_rinder.append(Kasten)
                    else:
                        Kasten = Label(master=Fenster1, bg='white', text=ration_rinder.iloc[r,c])
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_rinder.append(Kasten)
                        
        if x==5:
            Kasten_bullen=[]
            entryRf_bullen=[0] * number_rows[0]
            entryFM_bullen=[0] * number_rows[0]
            c=0
            for col in ration_bullen.columns: 
                Kasten = Label(master=Fenster1, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=5, column=c, padx='5', pady='5')
                c=c+1
            
            for r in range(number_rows[0]):
                for c in range(number_rows[1]):        
                    if c==0:
                        entryRf_bullen[r] = Entry(master=Fenster1, bg='white')
                        entryRf_bullen[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryRf_bullen[r].insert(0,ration_bullen.iloc[r,c])
                    elif c==6:
                        entryFM_bullen[r] = Entry(master=Fenster1, bg='white')
                        entryFM_bullen[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        entryFM_bullen[r].insert(0,ration_bullen.iloc[r,c])
                    elif c>5:
                        Kasten = Label(master=Fenster1, bg='white', text=round(ration_bullen.iloc[r,c],2))
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_bullen.append(Kasten)
                    else:
                        Kasten = Label(master=Fenster1, bg='white', text=ration_bullen.iloc[r,c])
                        Kasten.grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                        Kasten_bullen.append(Kasten)
    #                
        if x==0 and table1[x].get()==1:
            buttonBerechnen1 = Button(master=Ration, bg='#FBD975', text='aktualisieren', font='Arial 12 bold',command=button_hochleistend_berechnen)
            buttonBerechnen1.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
            buttonWeiter = Button(master=Ration, bg='#FBD975', text='speichern und beenden',font='Arial 12 bold', command=button_hochleistend_weiter)
            buttonWeiter.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
            ButtonMenge = Button(master=Ration, bg='#FBD975', text='Sortieren nach Menge', font='Arial 12 bold',command=button_hochleistend_menge)
            ButtonMenge.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
        
        if x==1 and table1[x].get()==1:
            buttonBerechnen1 = Button(master=Ration_Frischmelker, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=button_frischmelker_berechnen)
            buttonBerechnen1.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
            buttonWeiter = Button(master=Ration_Frischmelker, bg='#FBD975', text='speichern und beenden',font='Arial 12 bold', command=button_frischmelker_weiter)
            buttonWeiter.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
            ButtonMenge = Button(master=Ration_Frischmelker, bg='#FBD975', text='Sortieren nach Menge',font='Arial 12 bold', command=button_frischmelker_menge)
            ButtonMenge.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
            
        if x==2 and table1[x].get()==1:
            buttonBerechnen1 = Button(master=Ration_Altmelker, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=button_altmelker_berechnen)
            buttonBerechnen1.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
            buttonWeiter = Button(master=Ration_Altmelker, bg='#FBD975', text='speichern und beenden',font='Arial 12 bold', command=button_altmelker_weiter)
            buttonWeiter.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
            ButtonMenge = Button(master=Ration_Altmelker, bg='#FBD975', text='Sortieren nach Menge',font='Arial 12 bold', command=button_altmelker_menge)
            ButtonMenge.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
            
        if x==3 and table1[x].get()==1:
            buttonBerechnen = Button(master=Ration_Trockensteher, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=button_trockensteher_berechnen)
            buttonBerechnen.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
            buttonWeiter = Button(master=Ration_Trockensteher, bg='#FBD975', text='speichern und beenden',font='Arial 12 bold', command=button_trockensteher_weiter)
            buttonWeiter.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
            ButtonMenge = Button(master=Ration_Trockensteher, bg='#FBD975', text='Sortieren nach Menge',font='Arial 12 bold', command=button_trockensteher_menge)
            ButtonMenge.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
#            
        if x==4 and table1[x].get()==1:
            buttonBerechnen = Button(master=Ration_Rinder, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=button_rinder_berechnen)
            buttonBerechnen.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
            buttonWeiter = Button(master=Ration_Rinder, bg='#FBD975', text='speichern und beenden',font='Arial 12 bold', command=button_rinder_weiter)
            buttonWeiter.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
            ButtonMenge = Button(master=Ration_Rinder, bg='#FBD975', text='Sortieren nach Menge',font='Arial 12 bold', command=button_rinder_menge)
            ButtonMenge.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
                     
        if x==5 and table1[x].get()==1:
            buttonBerechnen = Button(master=Ration_Bullen, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=button_bullen_berechnen)
            buttonBerechnen.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
            buttonWeiter = Button(master=Ration_Bullen, bg='#FBD975', text='speichern und beenden',font='Arial 12 bold', command=button_bullen_weiter)
            buttonWeiter.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
            ButtonMenge = Button(master=Ration_Bullen, bg='#FBD975', text='Sortieren nach Menge',font='Arial 12 bold', command=button_bullen_menge)
            ButtonMenge.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
    
      
    for x in range(len(table1)):
        if x==0 and table1[x].get()==1:
            Kasten_Mischung_hochleistend=[]
            header = Label(master=Mischung, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text=NameRation, fg='black', bg='white',width = 12, height = 2,font="Arial 12 bold")
            header.grid(row=0,column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl_hochleistend = Entry(master=Mischung, bg='white')
            EntryAnzahl_hochleistend.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            EntryAnzahl_hochleistend.insert(0,Anzahl_hochleistend)
            header = Label(master=Mischung, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar_hochleistend = Entry(master=Mischung, bg='white')
            EntryVar_hochleistend.grid(row=1, column=4, padx='1', pady='1', sticky='ew') 
            EntryVar_hochleistend.insert(0,Varianz_hochleistend)
            c=0
            for col in mischung_hochleistend.columns:
                Kasten = Label(master=Mischung, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=3, column=c, padx='5', pady='5')
                c=c+1

            header = Label(master=Mischung, text="Kuhzahl:", fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung, text=Anzahl_hochleistend-Varianz_hochleistend, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=4, padx='1', pady='1', sticky='ew') 
            Kasten_Mischung_hochleistend.append(header)
            header = Label(master=Mischung, text=Anzahl_hochleistend, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_hochleistend.append(header)
            header = Label(master=Mischung, text=Anzahl_hochleistend +Varianz_hochleistend, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_hochleistend.append(header)
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung, bg='white', text=mischung_hochleistend.iloc[r,0])
                Kasten.grid(row=r+4, column=0)
                Kasten_Mischung_hochleistend.append(Kasten)
                Kasten = Label(master=Mischung, bg='white', text=mischung_hochleistend.iloc[r,1])
                Kasten.grid(row=r+4, column=1)
                Kasten_Mischung_hochleistend.append(Kasten)
                Kasten = Label(master=Mischung, bg='white', text=mischung_hochleistend.iloc[r,2])
                Kasten.grid(row=r+4, column=2)
                Kasten_Mischung_hochleistend.append(Kasten)
                Kasten = Label(master=Mischung, bg='white', text=mischung_hochleistend.iloc[r,3])
                Kasten.grid(row=r+4, column=3) 
                Kasten_Mischung_hochleistend.append(Kasten)
                Kasten = Label(master=Mischung, bg='white', text=mischung_hochleistend.iloc[r,4])
                Kasten.grid(row=r+4, column=4)
                Kasten_Mischung_hochleistend.append(Kasten)
                Kasten = Label(master=Mischung, bg='white', text=mischung_hochleistend.iloc[r,5])
                Kasten.grid(row=r+4, column=5)
                Kasten_Mischung_hochleistend.append(Kasten)
                Kasten = Label(master=Mischung, bg='white', text=mischung_hochleistend.iloc[r,6])
                Kasten.grid(row=r+4, column=6)
                Kasten_Mischung_hochleistend.append(Kasten)
                
            header = Label(master=Mischung, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text=Frischmasse, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text=Frischmasse*(Anzahl_hochleistend-Varianz_hochleistend), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text=Frischmasse*Anzahl_hochleistend, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text=Frischmasse*(Anzahl_hochleistend+Varianz_hochleistend), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=buttonAktualisierenMischung_hochleistend)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
    
        
        if x==1 and table1[x].get()==1:
            Kasten_Mischung_frischmelker=[]
            header = Label(master=Mischung_Frischmelker, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text=NameRation, fg='black', bg='white',width = 12, height = 2,font="Arial 12 bold")
            header.grid(row=0,column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl_Frischmelker = Entry(master=Mischung_Frischmelker, bg='white')
            EntryAnzahl_Frischmelker.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            EntryAnzahl_Frischmelker.insert(0,Anzahl_frischmelker)
            header = Label(master=Mischung_Frischmelker, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar_Frischmelker = Entry(master=Mischung_Frischmelker, bg='white')
            EntryVar_Frischmelker.grid(row=1, column=4, padx='1', pady='1', sticky='ew') 
            EntryVar_Frischmelker.insert(0,Varianz_frischmelker)
            c=0
            for col in mischung_frischmelker.columns:
                    Kasten = Label(master=Mischung_Frischmelker, bg='white', text=col,font='Arial 12 bold')
                    Kasten.grid(row=3, column=c, padx='5', pady='5')
                    c=c+1
  
            header = Label(master=Mischung_Frischmelker, text="Kuhzahl:", fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung_Frischmelker, text=Anzahl_frischmelker-Varianz_frischmelker, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=4, padx='1', pady='1', sticky='ew') 
            Kasten_Mischung_frischmelker.append(header)
            header = Label(master=Mischung_Frischmelker, text=Anzahl_frischmelker, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_frischmelker.append(header)
            header = Label(master=Mischung_Frischmelker, text=Anzahl_frischmelker +Varianz_frischmelker, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_frischmelker.append(header)
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=mischung_frischmelker.iloc[r,0])
                Kasten.grid(row=r+4, column=0)
                Kasten_Mischung_frischmelker.append(Kasten)
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=mischung_frischmelker.iloc[r,1])
                Kasten.grid(row=r+4, column=1)
                Kasten_Mischung_frischmelker.append(Kasten)
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=mischung_frischmelker.iloc[r,2])
                Kasten.grid(row=r+4, column=2) 
                Kasten_Mischung_frischmelker.append(Kasten)
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=mischung_frischmelker.iloc[r,3])
                Kasten.grid(row=r+4, column=3)
                Kasten_Mischung_frischmelker.append(Kasten)
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=mischung_frischmelker.iloc[r,4])
                Kasten.grid(row=r+4, column=4)
                Kasten_Mischung_frischmelker.append(Kasten)
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=mischung_frischmelker.iloc[r,5])
                Kasten.grid(row=r+4, column=5)
                Kasten_Mischung_frischmelker.append(Kasten)
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=mischung_frischmelker.iloc[r,6])
                Kasten.grid(row=r+4, column=6)
                Kasten_Mischung_frischmelker.append(Kasten)
                
            header = Label(master=Mischung_Frischmelker, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text=Frischmasse, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text=Frischmasse*(Anzahl_frischmelker-Varianz_frischmelker), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text=Frischmasse*Anzahl_frischmelker, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text=Frischmasse*(Anzahl_frischmelker+Varianz_frischmelker), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung_Frischmelker, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=buttonAktualisierenMischung_Frischmelker)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
            
        if x==2 and table1[x].get()==1:
            Kasten_Mischung_altmelker=[]
            header = Label(master=Mischung_Altmelker, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text=NameRation, fg='black', bg='white',width = 12, height = 2,font="Arial 12 bold")
            header.grid(row=0,column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl_Altmelker = Entry(master=Mischung_Altmelker, bg='white')
            EntryAnzahl_Altmelker.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            EntryAnzahl_Altmelker.insert(0,Anzahl_altmelker)
            header = Label(master=Mischung_Altmelker, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar_Altmelker = Entry(master=Mischung_Altmelker, bg='white')
            EntryVar_Altmelker.grid(row=1, column=4, padx='1', pady='1', sticky='ew') 
            EntryVar_Altmelker.insert(0,Varianz_altmelker)
            c=0
            for col in mischung_altmelker.columns:
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=3, column=c, padx='5', pady='5')
                c=c+1
                
            header = Label(master=Mischung_Altmelker, text="Kuhzahl:", fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung_Altmelker, text=Anzahl_altmelker-Varianz_altmelker, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=4, padx='1', pady='1', sticky='ew') 
            Kasten_Mischung_altmelker.append(header)
            header = Label(master=Mischung_Altmelker, text=Anzahl_altmelker, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_altmelker.append(header)
            header = Label(master=Mischung_Altmelker, text=Anzahl_altmelker +Varianz_altmelker, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_altmelker.append(header)
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=mischung_altmelker.iloc[r,0])
                Kasten.grid(row=r+4, column=0)
                Kasten_Mischung_altmelker.append(Kasten)
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=mischung_altmelker.iloc[r,1])
                Kasten.grid(row=r+4, column=1)
                Kasten_Mischung_altmelker.append(Kasten)
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=mischung_altmelker.iloc[r,2])
                Kasten.grid(row=r+4, column=2) 
                Kasten_Mischung_altmelker.append(Kasten)
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=mischung_altmelker.iloc[r,3])
                Kasten.grid(row=r+4, column=3)
                Kasten_Mischung_altmelker.append(Kasten)
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=mischung_altmelker.iloc[r,4])
                Kasten.grid(row=r+4, column=4)
                Kasten_Mischung_altmelker.append(Kasten)
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=mischung_altmelker.iloc[r,5])
                Kasten.grid(row=r+4, column=5)
                Kasten_Mischung_altmelker.append(Kasten)
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=mischung_altmelker.iloc[r,6])
                Kasten.grid(row=r+4, column=6)
                Kasten_Mischung_altmelker.append(Kasten)
                
            header = Label(master=Mischung_Altmelker, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text=Frischmasse, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text=Frischmasse*(Anzahl_altmelker-Varianz_altmelker), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text=Frischmasse*Anzahl_altmelker, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text=Frischmasse*(Anzahl_altmelker+Varianz_altmelker), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung_Altmelker, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=buttonAktualisierenMischung_Altmelker)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
            
        if x==3 and table1[x].get()==1:
            Kasten_Mischung_trockensteher=[]
            header = Label(master=Mischung_Trockensteher, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text=NameRation, fg='black', bg='white',width = 12, height = 2,font="Arial 12 bold")
            header.grid(row=0,column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl_Trockensteher = Entry(master=Mischung_Trockensteher, bg='white')
            EntryAnzahl_Trockensteher.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            EntryAnzahl_Trockensteher.insert(0,Anzahl_trockensteher)
            header = Label(master=Mischung_Trockensteher, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar_Trockensteher = Entry(master=Mischung_Trockensteher, bg='white')
            EntryVar_Trockensteher.grid(row=1, column=4, padx='1', pady='1', sticky='ew') 
            EntryVar_Trockensteher.insert(0,Varianz_trockensteher)
            c=0
            for col in mischung_trockensteher.columns:
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=3, column=c, padx='5', pady='5')
                c=c+1
                
            header = Label(master=Mischung_Trockensteher, text="Kuhzahl:", fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung_Trockensteher, text=Anzahl_trockensteher-Varianz_trockensteher, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=4, padx='1', pady='1', sticky='ew') 
            Kasten_Mischung_trockensteher.append(header)
            header = Label(master=Mischung_Trockensteher, text=Anzahl_trockensteher, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_trockensteher.append(header)
            header = Label(master=Mischung_Trockensteher, text=Anzahl_trockensteher +Varianz_trockensteher, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_trockensteher.append(header)
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=mischung_trockensteher.iloc[r,0])
                Kasten.grid(row=r+4, column=0)
                Kasten_Mischung_trockensteher.append(Kasten)
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=mischung_trockensteher.iloc[r,1])
                Kasten.grid(row=r+4, column=1)
                Kasten_Mischung_trockensteher.append(Kasten)
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=mischung_trockensteher.iloc[r,2])
                Kasten.grid(row=r+4, column=2) 
                Kasten_Mischung_trockensteher.append(Kasten)
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=mischung_trockensteher.iloc[r,3])
                Kasten.grid(row=r+4, column=3)
                Kasten_Mischung_trockensteher.append(Kasten)
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=mischung_trockensteher.iloc[r,4])
                Kasten.grid(row=r+4, column=4)
                Kasten_Mischung_trockensteher.append(Kasten)
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=mischung_trockensteher.iloc[r,5])
                Kasten.grid(row=r+4, column=5)
                Kasten_Mischung_trockensteher.append(Kasten)
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=mischung_trockensteher.iloc[r,6])
                Kasten.grid(row=r+4, column=6)
                Kasten_Mischung_trockensteher.append(Kasten)
                
            header = Label(master=Mischung_Trockensteher, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text=Frischmasse, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text=Frischmasse*(Anzahl_trockensteher-Varianz_trockensteher), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text=Frischmasse*Anzahl_trockensteher, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text=Frischmasse*(Anzahl_trockensteher+Varianz_trockensteher), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung_Trockensteher, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=buttonAktualisierenMischung_Trockensteher)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
            
        if x==4 and table1[x].get()==1:
            Kasten_Mischung_rinder=[]
            header = Label(master=Mischung_Rinder, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text=NameRation, fg='black', bg='white',width = 12, height = 2,font="Arial 12 bold")
            header.grid(row=0,column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl_Rinder = Entry(master=Mischung_Rinder, bg='white')
            EntryAnzahl_Rinder.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            EntryAnzahl_Rinder.insert(0,Anzahl_rinder)
            header = Label(master=Mischung_Rinder, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar_Rinder = Entry(master=Mischung_Rinder, bg='white')
            EntryVar_Rinder.grid(row=1, column=4, padx='1', pady='1', sticky='ew') 
            EntryVar_Rinder.insert(0,Varianz_rinder)
            c=0
            for col in mischung_rinder.columns:
                Kasten = Label(master=Mischung_Rinder, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=3, column=c, padx='5', pady='5')
                c=c+1
                
            header = Label(master=Mischung_Rinder, text="Kuhzahl:", fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung_Rinder, text=Anzahl_rinder-Varianz_rinder, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=4, padx='1', pady='1', sticky='ew') 
            Kasten_Mischung_hochleistend.append(header)
            header = Label(master=Mischung_Rinder, text=Anzahl_rinder, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_hochleistend.append(header)
            header = Label(master=Mischung_Rinder, text=Anzahl_rinder +Varianz_rinder, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_hochleistend.append(header)
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung_Rinder, bg='white', text=mischung_rinder.iloc[r,0])
                Kasten.grid(row=r+4, column=0)
                Kasten_Mischung_rinder.append(Kasten)
                Kasten = Label(master=Mischung_Rinder, bg='white', text=mischung_rinder.iloc[r,1])
                Kasten.grid(row=r+4, column=1)
                Kasten_Mischung_rinder.append(Kasten)
                Kasten = Label(master=Mischung_Rinder, bg='white', text=mischung_rinder.iloc[r,2])
                Kasten.grid(row=r+4, column=2) 
                Kasten_Mischung_rinder.append(Kasten)
                Kasten = Label(master=Mischung_Rinder, bg='white', text=mischung_rinder.iloc[r,3])
                Kasten.grid(row=r+4, column=3)
                Kasten_Mischung_rinder.append(Kasten)
                Kasten = Label(master=Mischung_Rinder, bg='white', text=mischung_rinder.iloc[r,4])
                Kasten.grid(row=r+4, column=4)
                Kasten_Mischung_rinder.append(Kasten)
                Kasten = Label(master=Mischung_Rinder, bg='white', text=mischung_rinder.iloc[r,5])
                Kasten.grid(row=r+4, column=5)
                Kasten_Mischung_rinder.append(Kasten)
                Kasten = Label(master=Mischung_Rinder, bg='white', text=mischung_rinder.iloc[r,6])
                Kasten.grid(row=r+4, column=6)
                Kasten_Mischung_rinder.append(Kasten)
                
            header = Label(master=Mischung_Rinder, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text=Frischmasse, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text=Frischmasse*(Anzahl_rinder-Varianz_rinder), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text=Frischmasse*Anzahl_rinder, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text=Frischmasse*(Anzahl_rinder+Varianz_rinder), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung_Rinder, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=buttonAktualisierenMischung_Rinder)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
            
        if x==5 and table1[x].get()==1:
            Kasten_Mischung_bullen=[]
            header = Label(master=Mischung_Bullen, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text=NameRation, fg='black', bg='white',width = 12, height = 2,font="Arial 12 bold")
            header.grid(row=0,column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl_Bullen = Entry(master=Mischung_Bullen, bg='white')
            EntryAnzahl_Bullen.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            EntryAnzahl_Bullen.insert(0,Anzahl_bullen)
            header = Label(master=Mischung_Bullen, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar_Bullen = Entry(master=Mischung_Bullen, bg='white')
            EntryVar_Bullen.grid(row=1, column=4, padx='1', pady='1', sticky='ew') 
            EntryVar_Bullen.insert(0,Varianz_bullen)
            c=0
            for col in mischung_bullen.columns:
                Kasten = Label(master=Mischung_Bullen, bg='white', text=col,font='Arial 12 bold')
                Kasten.grid(row=3, column=c, padx='5', pady='5')
                c=c+1
                
            header = Label(master=Mischung_Bullen, text="Kuhzahl:", fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung_Bullen, text=Anzahl_bullen-Varianz_bullen, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=4, padx='1', pady='1', sticky='ew') 
            Kasten_Mischung_bullen.append(header)
            header = Label(master=Mischung_Bullen, text=Anzahl_bullen, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_bullen.append(header)
            header = Label(master=Mischung_Bullen, text=Anzahl_bullen +Varianz_bullen, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=2, column=6, padx='1', pady='1', sticky='ew')
            Kasten_Mischung_bullen.append(header)
            
            for r in range(number_rows[0]):
                Kasten_Mischung_bullen.append(Kasten)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=mischung_bullen.iloc[r,0])
                Kasten.grid(row=r+4, column=0)
                Kasten_Mischung_bullen.append(Kasten)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=mischung_bullen.iloc[r,1])
                Kasten.grid(row=r+4, column=1)
                Kasten_Mischung_bullen.append(Kasten)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=mischung_bullen.iloc[r,2])
                Kasten.grid(row=r+4, column=2) 
                Kasten_Mischung_bullen.append(Kasten)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=mischung_bullen.iloc[r,3])
                Kasten.grid(row=r+4, column=3)
                Kasten_Mischung_bullen.append(Kasten)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=mischung_bullen.iloc[r,4])
                Kasten.grid(row=r+4, column=4)
                Kasten_Mischung_bullen.append(Kasten)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=mischung_bullen.iloc[r,5])
                Kasten.grid(row=r+4, column=5)
                Kasten_Mischung_bullen.append(Kasten)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=mischung_bullen.iloc[r,6])
                Kasten.grid(row=r+4, column=6)
                Kasten_Mischung_bullen.append(Kasten)
                
            header = Label(master=Mischung_Bullen, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text=Frischmasse, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text=Frischmasse*(Anzahl_bullen-Varianz_bullen), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text=Frischmasse*Anzahl_bullen, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text=Frischmasse*(Anzahl_bullen+Varianz_bullen), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=6, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung_Bullen, bg='#FBD975', text='aktualisieren',font='Arial 12 bold', command=buttonAktualisierenMischung_Bullen)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
            
        else:
            continue
        
    parent.mainloop()

    
    if status=='mineral' or status=='feucht' or status=='trocken' :        
        os.chdir('/home/thomas/.config/spyder-py3/Projekt1/Komponenten/')
        if status=='mineral':
            filename='Mineralfutter.csv'
            y=0
        if status=='feucht':
            filename='feuchte Komponenten.csv' 
            y=1
        if status=='trocken':
            filename='trockene Komponenten.csv'
            y=2
        Komponenten = pd.read_csv(filename,encoding='latin-1')
        
        KomponentenFenster=pd.concat([Komponenten["Maske"], Komponenten["Kennung"], Komponenten["Komponente"],Komponenten["Bezeichnung"]], axis=1, ignore_index=False)
        KomponentenFenster=KomponentenFenster.fillna("-")
        root = Tk()
        if y==0:
            root.title("Auswahl Mineralfutter")
        if y==1:
            root.title("Auswahl feuchte Komponenten")    
        if y==2:
            root.title("Auswahl trockene Komponenten") 
        table=[]   
        root.grid_rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        frame_main = Frame(root,  bg="gray85")
        frame_main.grid(sticky='news')
        
        frame_header = Frame(frame_main)
        frame_header.grid(row=0, column=0, pady=(5, 0), sticky='nw')
        frame_header.grid_rowconfigure(0, weight=1)
        frame_header.grid_columnconfigure(0, weight=1)
        #
        canvas = Canvas(frame_header,width=1000, height=20, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
    
        frame_canvas = Frame(frame_main)
        frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        
        # Add a canvas in that frame
        canvas = Canvas(frame_canvas,width=1000, height=700, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
        
        # Link a scrollbar to the canvas
        vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)
        
    #    hsbar = Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
    #    hsbar.grid(row=1, column=0, sticky="EW")
    #    canvas.configure(xscrollcommand=hsbar.set)
        Labelueberschrift=Label(master=frame_header, text= "Welche Analysen sollen für die Ration " + str(NameRation) + " verwendet werden?", font='Arial 12 bold')
        Labelueberschrift.grid(row=0, column=0) 
        
        # Create a frame to contain the labels
        frame_labels = Frame(canvas, bg="gray85")
        canvas.create_window((0, 0), window=frame_labels, anchor='nw')
        header = Label(master=frame_labels, text='ausgewählt', fg='black', bg='white', font=('Arial 14 bold'),width = 12, height = 2,)
        header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Kennung', fg='black', bg='white', font=('Arial 14 bold'),width = 12, height = 2,)
        header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Futter', fg='black', bg='white', font=('Arial 14 bold'),width = 12, height = 2,)
        header.grid(row=0, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Bezeichnung', fg='black', bg='white', font=('Arial 14 bold'),width = 12, height = 2,)
        header.grid(row=0, column=3, padx='1', pady='1', sticky='ew')
        
        number_rows=KomponentenFenster.shape 
        for x in range(number_rows[0]):
            table.append('var_'+str(x))
            table[x]=IntVar()
            
        checkbutton=[Checkbutton() for r in range(number_rows[0])]  
        Kasten=[[Label() for c in range(number_rows[1])] for r in range(number_rows[0])] 
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c == 0:
                    checkbutton[r] = Checkbutton(master=frame_labels, anchor='center',offvalue=0, onvalue=1, variable=table[r],height = 2,)
                    checkbutton[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                else:
                    Kasten[r][c] = Label(master=frame_labels, bg='white', text=KomponentenFenster.iloc[r,c],font=('Arial 12 bold'))
                    Kasten[r][c].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
        
        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        frame_labels.update_idletasks()
        
        # Resize the canvas frame to show exactly 5-by-10 labels and the scrollbar
        first5columns_width = sum([Kasten[r][0].winfo_width() for r in range(0, 10)])
        first5rows_height = sum([Kasten[0][c].winfo_height() for c in range(0, 4)])
        frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                            height=first5rows_height)
        
        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))
            
           
        
        frame_button = Frame(frame_main)
        frame_button.grid(row=4, column=0, pady=(0), sticky='nw')
        frame_button.grid_rowconfigure(0, weight=1)
        frame_button.grid_columnconfigure(0, weight=1)
        #
        canvas = Canvas(frame_button,width=550, height=5, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
        if y==0:
            Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F',font='Arial 12 bold', command=Buttonauswahlmineral)
        if y==1:
            Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F',font='Arial 12 bold', command=Buttonauswahlfeucht)    
        if y==2:
            Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F',font='Arial 12 bold', command=Buttonauswahltrocken) 
                                           
        Buttonauswahlanalysen.grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')


        root.mainloop()     
        
        ration_append=ration.head(0)        
        for r in range(number_rows[0]):
            if table[r].get()==1:
                ration_append=ration_append.append(Komponenten.iloc[r], ignore_index = True)

                
        rationfenster=pd.concat([ration_append["Kennung"], ration_append["Komponente"],ration_append["Bezeichnung"],ration_append['Kosten ( € /dt )'],ration_append['TS in %']], axis=1, ignore_index=False)
        
        # Kosten und TS eingeben
        
        number_rows=rationfenster.shape 
        rationfenster["Bezeichnung"]=rationfenster["Bezeichnung"].fillna("-")
        rationfenster['Kosten ( € /dt )']=rationfenster['Kosten ( € /dt )'].fillna(0)
        
        entryKosten=[0] * number_rows[0]
        entryTS=[0] * number_rows[0]

        tkFenster = Tk()
        tkFenster.title("Eintragen der Kosten und aktualisieren der TS")
        #header = Label(master=tkFenster, text='Gib den Preis ein und aktualisiere gegebenenfalls die TS-Werte', fg='black', bg='white', font=('Arial'),width = 12, height = 2,)
        #header.grid(row=0, sticky="news")
        c=0
        for col in rationfenster.columns: 
            Kasten = Label(master=tkFenster, bg='white', text=col, font=('Arial 12 bold'))
            Kasten.grid(row=1, column=c)
            c=c+1
        
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c<3:
                    Kasten = Label(master=tkFenster, bg='white', text=rationfenster.iloc[r,c])
                    Kasten.grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                if c==3:
                   entryKosten[r] = Entry(master=tkFenster, bg='white')
                   entryKosten[r].config(font='Arial 12 bold',width=20)
                   entryKosten[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                   entryKosten[r].insert(0,rationfenster.iloc[r,c])
                   
                if c==4:
                    entryTS[r] = Entry(master=tkFenster, bg='white')
                    entryTS[r].config(font='Arial 12 bold',width=10)
                    entryTS[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                    entryTS[r].insert(0,rationfenster.iloc[r,c])
        
        asd=number_rows[0]
        buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='weiter',font='Arial 12 bold', command=button_Kosten_ration)
        buttonBerechnen.grid(row=r+3, column=c, padx='5', pady='5', sticky='ew')
        
        tkFenster.mainloop()

        ration_append['Kosten ( € /dt )']=Kosten
        ration_append['TS in %']=TS
        
        number_rows_append=ration_append.shape
        number_rows_alt=ration.shape
        for r in range(number_rows_append[0]):
            ration=ration.append(ration_append.iloc[r,0:24])
        
        ration.reset_index(drop=True, inplace=True)
        for r in range(number_rows_append[0]):
            ration_hochleistend = ration_hochleistend.append(ration.iloc[number_rows_alt[0]+r,0:3])
            ration_frischmelker = ration_frischmelker.append(ration.iloc[number_rows_alt[0]+r,0:3])
            ration_altmelker = ration_altmelker.append(ration.iloc[number_rows_alt[0]+r,0:3])
            ration_trockensteher = ration_trockensteher.append(ration.iloc[number_rows_alt[0]+r,0:3])
            ration_rinder = ration_rinder.append(ration.iloc[number_rows_alt[0]+r,0:3])
            ration_bullen = ration_bullen.append(ration.iloc[number_rows_alt[0]+r,0:3])
            
            mischung_hochleistend = mischung_hochleistend.append(ration.iloc[number_rows_alt[0]+r,0:2])
            mischung_frischmelker = mischung_frischmelker.append(ration.iloc[number_rows_alt[0]+r,0:2])
            mischung_altmelker = mischung_altmelker.append(ration.iloc[number_rows_alt[0]+r,0:2])
            mischung_trockensteher = mischung_trockensteher.append(ration.iloc[number_rows_alt[0]+r,0:2])
            mischung_rinder = mischung_rinder.append(ration.iloc[number_rows_alt[0]+r,0:2])
            mischung_bullen = mischung_bullen.append(ration.iloc[number_rows_alt[0]+r,0:2])

                
        ration["Bezeichnung"] = ration["Bezeichnung"].fillna("-")        
        ration_hochleistend["Bezeichnung"] = ration_hochleistend["Bezeichnung"].fillna("-")
        ration_frischmelker["Bezeichnung"] = ration_frischmelker["Bezeichnung"].fillna("-")
        ration_altmelker["Bezeichnung"] = ration_altmelker["Bezeichnung"].fillna("-")
        ration_trockensteher["Bezeichnung"] = ration_trockensteher["Bezeichnung"].fillna("-")
        ration_rinder["Bezeichnung"] = ration_rinder["Bezeichnung"].fillna("-")
        ration_bullen["Bezeichnung"] = ration_bullen["Bezeichnung"].fillna("-")
        
        ration = ration.fillna(0)
        ration_hochleistend = ration_hochleistend.fillna(0)
        ration_frischmelker = ration_frischmelker.fillna(0)
        ration_altmelker = ration_altmelker.fillna(0)
        ration_trockensteher = ration_trockensteher.fillna(0)
        ration_rinder = ration_rinder.fillna(0)
        ration_bullen = ration_bullen.fillna(0)
        
        mischung_hochleistend["Bezeichnung"] = mischung_hochleistend["Bezeichnung"].fillna("-")
        mischung_frischmelker["Bezeichnung"] = mischung_frischmelker["Bezeichnung"].fillna("-")
        mischung_altmelker["Bezeichnung"] = mischung_altmelker["Bezeichnung"].fillna("-")
        mischung_trockensteher["Bezeichnung"] = mischung_trockensteher["Bezeichnung"].fillna("-")
        mischung_rinder["Bezeichnung"] = mischung_rinder["Bezeichnung"].fillna("-")
        mischung_bullen["Bezeichnung"] = mischung_bullen["Bezeichnung"].fillna("-")
        
        mischung_hochleistend = mischung_hochleistend.fillna(0)
        mischung_frischmelker = mischung_frischmelker.fillna(0)
        mischung_altmelker = mischung_altmelker.fillna(0)
        mischung_trockensteher = mischung_trockensteher.fillna(0)
        mischung_rinder = mischung_rinder.fillna(0)
        mischung_bullen = mischung_bullen.fillna(0)
        
    if status=='Kosten':
        number_rows=ration.shape
        entryKosten=[0] * number_rows[0]
        entryTS=[0] * number_rows[0]
        tkFenster = Tk()
        tkFenster.title("Eintragen der Kosten und aktualisieren der TS")
        
        c=0
        for col in rationfenster.columns: 
            Kasten = Label(master=tkFenster, bg='white', text=col, font=('Arial 14 bold'),width = 5, height = 2)
            Kasten.grid(row=1, column=c, padx='5', pady='5', sticky='ew')
            c=c+1
        
        for r in range(number_rows[0]):
            for c in range(6):
                if c<4:
                    Kasten = Label(master=tkFenster, bg='white', text=ration.iloc[r,c],font='Arial 12 bold')
                    Kasten.grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                if c==4:
                   entryKosten[r] = Entry(master=tkFenster, bg='white')
                   entryKosten[r].config(font='Arial 12 bold',width=20)
                   entryKosten[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                   entryKosten[r].insert(0,ration.iloc[r,c])
                    
                if c==5:
                    entryTS[r] = Entry(master=tkFenster, bg='white')
                    entryTS[r].config(font='Arial 12 bold',width=10)
                    entryTS[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                    entryTS[r].insert(0,ration.iloc[r,c])
        
        asd=number_rows[0]
        buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='weiter',font='Arial 12 bold', command=buttonKosten_ration)
        buttonBerechnen.grid(row=r+3, column=c, padx='5', pady='5', sticky='ew')
        
        tkFenster.mainloop()
        
        ration['TS in %']=TS
        ration['Kosten ( € /dt )']=Kosten
        
    if status=='Gruppen':
        table2=[]
        for x in range(len(Gruppen)):
            table2.append(table1[x].get())
            

        tkFenster = Tk()
        tkFenster.title("Auswahl der Gruppen")
        for x in range(len(Gruppen)):
            table1[x]=IntVar()
            table1[x].set(table2[x])
            
        header = Label(master=tkFenster, text=' ', fg='gray85', bg='gray85', font='Arial 2 bold',width = 15, height = 2)
        header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='ausgewählt', fg='black', bg='white', font=('Arial 14 bold'))
        header.grid(row=1, column=0, padx='3', pady='3', sticky='ew')
        header = Label(master=tkFenster, text='Gruppenname', fg='black', bg='white', font=('Arial 14 bold'))
        header.grid(row=1, column=1, padx='3', pady='3', sticky='ew')
        
                
        checkbutton=[Checkbutton() for r in range(len(Gruppen))]  
        Kasten=[Label() for r in range(len(Gruppen))] 
        for r in range(len(Gruppen)):
                checkbutton[r] = Checkbutton(master=tkFenster, anchor='center',offvalue=0, onvalue=1, variable=table1[r],height = 2)
                checkbutton[r].grid(row=r+2, column=0, padx='5', pady='5', sticky='ew')
                if table1[r].get()==1:
                    checkbutton[r].select()
                Kasten[r] = Label(master=tkFenster, bg='white', text=Gruppen[r],font='Arial 12 bold')
                Kasten[r].grid(row=r+2, column=1, padx='5', pady='5', sticky='ew')
                
        Buttonauswahlanalysen = Button(master=tkFenster, text='weiter', bg='#D5E88F',font='Arial 12 bold', command=Gruppenweiter)                 
        Buttonauswahlanalysen.grid(row=r+3, column=1, padx='5', pady='5', sticky='ew')
               
        tkFenster.mainloop()
    
    if status=='Analysen':
        os.chdir('/home/thomas/.config/spyder-py3/Projekt1/queries/')
        filename='latest_query.csv'
        Analysen = pd.read_csv(filename,encoding='latin-1')
        list1 = Analysen['Sampled For'].astype(str)
        autocompleteList=list(set(list1))
    
        tkFenster = Tk()
        tkFenster.title('Auswahl des Betriebes')
        tkFenster.geometry('520x250')
        
        Labelueberschrift=Label(master=tkFenster, text= "Die Analysen welches Betriebs soll genutzt werden?", font='Arial 12 bold')
        Labelueberschrift.place(x=10, y=20)
        EingabeBetrieb = AutocompleteEntry(autocompleteList, tkFenster, listboxLength=12, width=70, x=10,  matchesFunction=matches)
        EingabeBetrieb.place(x=10, y=50) 
        ButtonAuswahl=Button(master=tkFenster, text='auswählen',bg='#D5E88F',font='Arial 12 bold', command=buttonauswählen_ration)
        ButtonAuswahl.place(x=400, y=100, width=100, height=30)
        ButtonAbbruch=Button(master=tkFenster, text='abbrechen',bg='#FFCFC9',font='Arial 12 bold', command=buttonabbrechen)
        ButtonAbbruch.place(x=10, y=100, width=100, height=30)
        
        tkFenster.mainloop()
        
        
        AnalysenBetrieb=Analysen.head(0)
        i=0
        for x in range(list1.size):
            if Betrieb==Analysen.iloc[x]['Sampled For']:
                AnalysenBetrieb=AnalysenBetrieb.append(Analysen.iloc[x])
                
        #Kennung	Komponente Bezeichnung	Kosten     	kg Frichmasse	 % der Ration in TS	TS in% 	MJ NEL	NDF	G NDF	ADF	Lignin	NSC	Stärke	Zucker	Roh- protein	lösl. Protein	Asche	Ca	P	Mg	K	Na	S	Kationen	Anionen
        AnalysenRation=pd.concat([emptyDataFrame['Maske'],AnalysenBetrieb["Sampled For"], AnalysenBetrieb["Product Type"],AnalysenBetrieb["Description 1"], AnalysenBetrieb["Date Processed"], emptyDataFrame['Kosten ( € /dt )'],
                             AnalysenBetrieb["Dry Matter"],AnalysenBetrieb["NEL OARDC"]/100*2.2/0.236, AnalysenBetrieb["aNDFom"],emptyDataFrame["Grundfutter NDF"], AnalysenBetrieb["uNDFom30"],AnalysenBetrieb["uNDFom120"],AnalysenBetrieb["uNDFom240"],AnalysenBetrieb["NFC"],
                             AnalysenBetrieb["Starch"],AnalysenBetrieb["IVSD7-o"],AnalysenBetrieb['Adjusted CP'], AnalysenBetrieb["Soluble Protein"],AnalysenBetrieb["Ammonia CP%DM"], AnalysenBetrieb["Ash"],AnalysenBetrieb["Ca"],AnalysenBetrieb["P"],
                             AnalysenBetrieb["Mg"],AnalysenBetrieb["Na"],AnalysenBetrieb["K"],AnalysenBetrieb["S"]], axis=1, ignore_index=False)
    
        AnalysenRation["Grundfutter NDF"]=AnalysenRation["aNDFom"]
        AnalysenRation, NAlist = reduce_mem_usage(AnalysenRation)
        AnalysenBetriebFenster=pd.concat([AnalysenBetrieb["Field Name"], AnalysenBetrieb["Date Processed"],AnalysenBetrieb["Sampled For"], AnalysenBetrieb["Product Type"],AnalysenBetrieb["Description 1"]], axis=1, ignore_index=False)
        number_rows=AnalysenBetriebFenster.shape
        for r in range(number_rows[0]):
            if AnalysenBetriebFenster.iloc[r,2]=='1':
                AnalysenBetriebFenster.iloc[r,2]='Heu'
            if AnalysenBetriebFenster.iloc[r,2]=='1A':
                AnalysenBetriebFenster.iloc[r,2]='Leguminosen Heu'
            if AnalysenBetriebFenster.iloc[r,2]=='1B':
                AnalysenBetriebFenster.iloc[r,2]='Grassheu'
            if AnalysenBetriebFenster.iloc[r,2]=='1C':
                AnalysenBetriebFenster.iloc[r,2]='gemischte Silage'
            if AnalysenBetriebFenster.iloc[r,2]=='1D':
                AnalysenBetriebFenster.iloc[r,2]='Leguminosen Silage'
            if AnalysenBetriebFenster.iloc[r,2]=='1E':
                AnalysenBetriebFenster.iloc[r,2]='Grasssilage'
            if AnalysenBetriebFenster.iloc[r,2]=='2':
                AnalysenBetriebFenster.iloc[r,2]='Maissilage' 
            if AnalysenBetriebFenster.iloc[r,2]=='3':
                AnalysenBetriebFenster.iloc[r,2]='Körnermais'
            if AnalysenBetriebFenster.iloc[r,2]=='4':
                AnalysenBetriebFenster.iloc[r,2]='Maiskolben'
            if AnalysenBetriebFenster.iloc[r,2]=='5':
                AnalysenBetriebFenster.iloc[r,2]='Getreide'
            if AnalysenBetriebFenster.iloc[r,2]=='6':
                AnalysenBetriebFenster.iloc[r,2]='Nebenprodukte Getreide'
            if AnalysenBetriebFenster.iloc[r,2]=='7':
                AnalysenBetriebFenster.iloc[r,2]='Getreide Silagen'
            if AnalysenBetriebFenster.iloc[r,2]=='8':
                AnalysenBetriebFenster.iloc[r,2]='Oelsamen und Nebenprodukte'
            if AnalysenBetriebFenster.iloc[r,2]=='9':
                AnalysenBetriebFenster.iloc[r,2]='TMR'
            if AnalysenBetriebFenster.iloc[r,2]=='10':
                AnalysenBetriebFenster.iloc[r,2]='sonstiges Futter'
        
        tkFenster = Tk()
        tkFenster.title('Auswahl Analysen')
        table=[]
        number_rows=AnalysenBetriebFenster.shape 
        for x in range(number_rows[0]):
            table.append('var_'+str(x))
            table[x]=IntVar()
        
        header = Label(master=tkFenster, text=' ', fg='gray85', bg='gray85', font='Arial 14 bold',width = 15, height = 2)
        header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
        Labelueberschrift=Label(master=tkFenster, text= "Welche Analysen sollen für die Ration " + str(NameRation) + " verwendet werden?", font='Arial 14 bold')
        Labelueberschrift.place(x=50, y=10)
        
        header = Label(master=tkFenster, text='ausgewählt', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
        header.grid(row=2, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Datum', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
        header.grid(row=2, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Kennung', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
        header.grid(row=2, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Futter', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
        header.grid(row=2, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Bezeichnung', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
            
            
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c == 0:
                    checkbutton = Checkbutton(master=tkFenster, anchor='center',offvalue=0, onvalue=1, variable=table[r],height = 2)
                    checkbutton.grid(row=r+3, column=c, padx='1', pady='1', sticky='ew')
                else:
                    Kasten = Label(master=tkFenster, bg='white', text=AnalysenBetriebFenster.iloc[r,c],font='Arial 12 bold')
                    Kasten.grid(row=r+3, column=c, padx='2', pady='2', sticky='ew')
                
        Buttonauswahlanalysen = Button(master=tkFenster, text='weiter', bg='#D5E88F',font='Arial 12 bold', command=Buttonauswahlanalysen_ration)
        Buttonauswahlanalysen.grid(row=r+4, column=c, padx='5', pady='5', sticky='ew')
            
        tkFenster.mainloop()
                                    
        AnalysenRation = AnalysenRation.rename(columns={'Sampled For': 'Kennung', 'Product Type': 'Komponente','Description 1': 'Bezeichnung','Date Processed': 'Datum','Dry Matter': 'TS in %','NEL OARDC': 'MJ NEL','aNDFom': 'NDF','Starch': 'Staerke','IVSD7-o': 'Staerkeverdaulichkeit 7h','Soluble Protein': 'loesl. Protein', 'Adjusted CP': 'Rohprotein',
                                     'Ammonia CP%DM': 'Ammonium-Protein','Ash': 'Asche','Ca': 'Kalzium','P': 'Phosphor','Mg': 'Magnesium','K':'Kalium','Na':'Natrium','uNDFom30': 'uNDF30','uNDFom120': 'uNDF120','uNDFom240': 'uNDF240', 'S':'Schwefel'})
        ration_append=ration.head(0)
        for r in range(number_rows[0]):
            if table[r].get()==1:
                ration_append=ration_append.append(AnalysenRation.iloc[r], ignore_index = False)
                
        ration_append["Bezeichnung"]=ration_append["Bezeichnung"].fillna("-")
        ration_append=ration_append.fillna(0)
    
        ration_append["Grundfutter NDF"] = ration_append["Grundfutter NDF"]/100
        ration_append["NDF"] = ration_append["Grundfutter NDF"]
        ration_append["uNDF30"] = ration_append["uNDF30"]/100
        ration_append["uNDF120"] = ration_append["uNDF120"]/100
        ration_append["uNDF240"] = ration_append["uNDF240"]/100
        ration_append["NFC"] = ration_append["NFC"]/100
        ration_append["Staerke"] = ration_append["Staerke"]/100
        ration_append["Staerkeverdaulichkeit 7h"] = ration_append["Staerkeverdaulichkeit 7h"]/100
        ration_append["Rohprotein"] = ration_append["Rohprotein"]/100
        ration_append["Asche"] = ration_append["Asche"]/100
        ration_append["Kalzium"] = ration_append["Kalzium"]/100
        ration_append["Phosphor"] = ration_append["Phosphor"]/100
        ration_append["Magnesium"] = ration_append["Magnesium"]/100
        ration_append["Natrium"] = ration_append["Natrium"]/100
        ration_append["Kalium"] = ration_append["Kalium"]/100
        ration_append["Schwefel"] = ration_append["Schwefel"]/100
        ration_append["loesl. Protein"] = ration_append["loesl. Protein"]/100
        ration_append["Ammonium-Protein"] = ration_append["Ammonium-Protein"]/100
        
        rationfenster1=pd.DataFrame()
        rationfenster1=pd.concat([ration_append["Kennung"], ration_append["Komponente"],ration_append['Datum'],ration_append["Bezeichnung"],emptyDataFrame['Kosten ( € /dt )'],ration_append['TS in %']], axis=1, ignore_index=False)
        
        # Kosten und TS eingeben
        
        number_rows=ration_append.shape 
        rationfenster1["Bezeichnung"]=rationfenster1["Bezeichnung"].fillna("-")
        rationfenster1['Kosten ( € /dt )']=rationfenster1['Kosten ( € /dt )'].fillna(0)
        ration_append["Bezeichnung"]=ration_append["Bezeichnung"].fillna("-")
        ration_append=ration_append.fillna(0)
        
        entryKosten=[0] * number_rows[0]
        entryTS=[0] * number_rows[0]

        tkFenster = Tk()
        tkFenster.title("Eintragen der Kosten und aktualisieren der TS")

        c=0
        for col in rationfenster1.columns: 
            Kasten = Label(master=tkFenster, bg='white', text=col, font=('Arial 14 bold'),width = 5, height = 2)
            Kasten.grid(row=1, column=c)
            c=c+1
        
        for r in range(number_rows[0]):
            for c in range(5):
                if c<4:
                    Kasten = Label(master=tkFenster, bg='white', text=rationfenster1.iloc[r,c])
                    Kasten.grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                if c==4:
                   entryKosten[r] = Entry(master=tkFenster, bg='white')
                   entryKosten[r].config(font='Arial 12 bold',width=20)
                   entryKosten[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                   entryKosten[r].insert(0,rationfenster1.iloc[r,c])
                   
                if c==4:
                    entryTS[r] = Entry(master=tkFenster, bg='white')
                    entryTS[r].config(font='Arial 12 bold',width=10)
                    entryTS[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                    entryTS[r].insert(0,rationfenster1.iloc[r,c])
        
        buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='weiter',font='Arial 12 bold', command=button_Kosten_ration)
        buttonBerechnen.grid(row=r+3, column=c, padx='5', pady='5', sticky='ew')
        
        tkFenster.mainloop()

        ration_append['Kosten ( € /dt )']=Kosten
        ration_append['TS in %']=TS
        
        number_rows_append=ration_append.shape
        number_rows_alt=ration.shape
        for r in range(number_rows_append[0]):
            ration=ration.append(ration_append.iloc[r,0:24])
        
        ration.reset_index(drop=True, inplace=True)
        for r in range(number_rows_append[0]):
            ration_hochleistend = ration_hochleistend.append(ration.iloc[number_rows_alt[0]+r,0:4])
            ration_frischmelker = ration_frischmelker.append(ration.iloc[number_rows_alt[0]+r,0:4])
            ration_altmelker = ration_altmelker.append(ration.iloc[number_rows_alt[0]+r,0:4])
            ration_trockensteher = ration_trockensteher.append(ration.iloc[number_rows_alt[0]+r,0:4])
            ration_rinder = ration_rinder.append(ration.iloc[number_rows_alt[0]+r,0:4])
            ration_bullen = ration_bullen.append(ration.iloc[number_rows_alt[0]+r,0:4])
            
            mischung_hochleistend = mischung_hochleistend.append(ration.iloc[number_rows_alt[0]+r,0:2])
            mischung_frischmelker = mischung_frischmelker.append(ration.iloc[number_rows_alt[0]+r,0:2])
            mischung_altmelker = mischung_altmelker.append(ration.iloc[number_rows_alt[0]+r,0:2])
            mischung_trockensteher = mischung_trockensteher.append(ration.iloc[number_rows_alt[0]+r,0:2])
            mischung_rinder = mischung_rinder.append(ration.iloc[number_rows_alt[0]+r,0:2])
            mischung_bullen = mischung_bullen.append(ration.iloc[number_rows_alt[0]+r,0:2])

        ration["Bezeichnung"] = ration["Bezeichnung"].fillna("-")        
        ration_hochleistend["Bezeichnung"] = ration_hochleistend["Bezeichnung"].fillna("-")
        ration_frischmelker["Bezeichnung"] = ration_frischmelker["Bezeichnung"].fillna("-")
        ration_altmelker["Bezeichnung"] = ration_altmelker["Bezeichnung"].fillna("-")
        ration_trockensteher["Bezeichnung"] = ration_trockensteher["Bezeichnung"].fillna("-")
        ration_rinder["Bezeichnung"] = ration_rinder["Bezeichnung"].fillna("-")
        ration_bullen["Bezeichnung"] = ration_bullen["Bezeichnung"].fillna("-")
        
        ration = ration.fillna(0)
        ration_hochleistend = ration_hochleistend.fillna(0)
        ration_frischmelker = ration_frischmelker.fillna(0)
        ration_altmelker = ration_altmelker.fillna(0)
        ration_trockensteher = ration_trockensteher.fillna(0)
        ration_rinder = ration_rinder.fillna(0)
        ration_bullen = ration_bullen.fillna(0)
        
        mischung_hochleistend["Bezeichnung"] = mischung_hochleistend["Bezeichnung"].fillna("-")
        mischung_frischmelker["Bezeichnung"] = mischung_frischmelker["Bezeichnung"].fillna("-")
        mischung_altmelker["Bezeichnung"] = mischung_altmelker["Bezeichnung"].fillna("-")
        mischung_trockensteher["Bezeichnung"] = mischung_trockensteher["Bezeichnung"].fillna("-")
        mischung_rinder["Bezeichnung"] = mischung_rinder["Bezeichnung"].fillna("-")
        mischung_bullen["Bezeichnung"] = mischung_bullen["Bezeichnung"].fillna("-")
        
        mischung_hochleistend = mischung_hochleistend.fillna(0)
        mischung_frischmelker = mischung_frischmelker.fillna(0)
        mischung_altmelker = mischung_altmelker.fillna(0)
        mischung_trockensteher = mischung_trockensteher.fillna(0)
        mischung_rinder = mischung_rinder.fillna(0)
        mischung_bullen = mischung_bullen.fillna(0)
        
    if status=='Komponenten':
        os.chdir('/home/thomas/.config/spyder-py3/Projekt1/queries/')
        filename='latest_query.csv'
        Analysen = pd.read_csv(filename,encoding='latin-1')
        list1 = Analysen['Description 1'].astype(str)
        autocompleteList=list(set(list1))
    
        tkFenster = Tk()
        tkFenster.title('Auswahl der Komponente')
        tkFenster.geometry('520x150')
        
        Labelueberschrift=Label(master=tkFenster, text= "Welche Komponente soll gesucht werden?", font='Arial 12 bold')
        Labelueberschrift.place(x=10, y=20)
        EingabeKomponente = Entry(master=tkFenster,fg='black', bg='white', width = 12,font="Arial 10 bold")
        EingabeKomponente.config(width=20)
        EingabeKomponente.place(x=10, y=50) 
        ButtonAuswahl=Button(master=tkFenster, text='auswählen',bg='#D5E88F',font='Arial 12 bold', command=buttonauswählen_ration)
        ButtonAuswahl.place(x=400, y=100, width=100, height=30)
        ButtonAbbruch=Button(master=tkFenster, text='abbrechen',bg='#FFCFC9',font='Arial 12 bold', command=buttonabbrechen)
        ButtonAbbruch.place(x=10, y=100, width=100, height=30)
        
        tkFenster.mainloop()
        
        
        AnalysenBetrieb=Analysen.head(0)
        i=0
        for x in range(list1.size):
            if str(Analysen.iloc[x]['Description 1']).find(Komponente) != -1:
                AnalysenBetrieb=AnalysenBetrieb.append(Analysen.iloc[x])
                
        #Kennung	Komponente Bezeichnung	Kosten     	kg Frichmasse	 % der Ration in TS	TS in% 	MJ NEL	NDF	G NDF	ADF	Lignin	NSC	Stärke	Zucker	Roh- protein	lösl. Protein	Asche	Ca	P	Mg	K	Na	S	Kationen	Anionen
        AnalysenRation=pd.concat([AnalysenBetrieb["Sampled For"], AnalysenBetrieb["Product Type"],AnalysenBetrieb["Description 1"], AnalysenBetrieb["Date Processed"], emptyDataFrame['Kosten ( € /dt )'],
                             AnalysenBetrieb["Dry Matter"],AnalysenBetrieb["NEL OARDC"]/100*2.2/0.236, AnalysenBetrieb["aNDFom"],emptyDataFrame["Grundfutter NDF"], AnalysenBetrieb["uNDFom30"],AnalysenBetrieb["uNDFom120"],AnalysenBetrieb["uNDFom240"],AnalysenBetrieb["NFC"],
                             AnalysenBetrieb["Starch"],AnalysenBetrieb["IVSD7-o"],AnalysenBetrieb['Adjusted CP'], AnalysenBetrieb["Soluble Protein"],AnalysenBetrieb["Ammonia CP%DM"], AnalysenBetrieb["Ash"],AnalysenBetrieb["Ca"],AnalysenBetrieb["P"],
                             AnalysenBetrieb["Mg"],AnalysenBetrieb["Na"],AnalysenBetrieb["K"],AnalysenBetrieb["S"]], axis=1, ignore_index=False)
    
        AnalysenRation["Grundfutter NDF"]=AnalysenRation["aNDFom"]
        #AnalysenRation, NAlist = reduce_mem_usage(AnalysenRation)
        AnalysenBetriebFenster=pd.concat([AnalysenBetrieb["Field Name"], AnalysenBetrieb["Date Processed"],AnalysenBetrieb["Sampled For"], AnalysenBetrieb["Product Type"],AnalysenBetrieb["Description 1"]], axis=1, ignore_index=False)
        number_rows=AnalysenBetriebFenster.shape
        
        tkFenster = Tk()
        tkFenster.title('Auswahl Analysen')
        table=[]
        number_rows=AnalysenBetriebFenster.shape 
        for x in range(number_rows[0]):
            table.append('var_'+str(x))
            table[x]=IntVar()
        
        header = Label(master=tkFenster, text=' ', fg='gray85', bg='gray85', font='Arial 12 bold',width = 15, height = 2)
        header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
        Labelueberschrift=Label(master=tkFenster, text= "Welche Analysen sollen für die Ration " + str(NameRation) + " verwendet werden?", font='Arial 12 bold')
        Labelueberschrift.place(x=10, y=10)
        
        tkFenster.grid_rowconfigure(0, weight=1)
        tkFenster.columnconfigure(0, weight=1)
        frame_main = Frame(tkFenster,  bg="gray85")
        frame_main.grid(sticky='news')
        
        frame_header = Frame(frame_main)
        frame_header.grid(row=0, column=0, pady=(5, 0), sticky='nw')
        frame_header.grid_rowconfigure(0, weight=1)
        frame_header.grid_columnconfigure(0, weight=1)
        #
        canvas = Canvas(frame_header,width=900, height=20, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
    
        frame_canvas = Frame(frame_main)
        frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        
        # Add a canvas in that frame
        canvas = Canvas(frame_canvas,width=1000, height=800, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
        
        # Link a scrollbar to the canvas
        vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)
        frame_labels = Frame(canvas, bg="gray85")
        canvas.create_window((0, 0), window=frame_labels, anchor='nw')
        
        header = Label(master=frame_labels, text='ausgewählt', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
        header.grid(row=2, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Datum', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
        header.grid(row=2, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Kennung', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
        header.grid(row=2, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Futter', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
        header.grid(row=2, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Bezeichnung', fg='black', bg='white', font='Arial 14 bold',width = 15, height = 2,)
        header.grid(row=2, column=4, padx='1', pady='1', sticky='ew')
        
        
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c == 0:
                    checkbutton = Checkbutton(master=frame_labels, anchor='center',offvalue=0, onvalue=1, variable=table[r],height = 2)
                    checkbutton.grid(row=r+3, column=c, padx='1', pady='1', sticky='ew')
                else:
                    Kasten = Label(master=frame_labels, bg='white', text=AnalysenBetriebFenster.iloc[r,c],font='Arial 12 bold')
                    Kasten.grid(row=r+3, column=c, padx='2', pady='2', sticky='ew')
            
        Buttonauswahlanalysen = Button(master=tkFenster, text='weiter', bg='#D5E88F',font='Arial 14 bold', command=Buttonauswahlanalysen_ration)
        Buttonauswahlanalysen.grid(row=r+4, column=c, padx='5', pady='5', sticky='ew')
            
        tkFenster.mainloop()
                                    
        AnalysenRation = AnalysenRation.rename(columns={'Sampled For': 'Kennung', 'Product Type': 'Komponente','Description 1': 'Bezeichnung','Date Processed': 'Datum','Dry Matter': 'TS in %','NEL OARDC': 'MJ NEL','aNDFom': 'NDF','Starch': 'Staerke','IVSD7-o': 'Staerkeverdaulichkeit 7h','Soluble Protein': 'loesl. Protein', 'Adjusted CP': 'Rohprotein',
                                     'Ammonia CP%DM': 'Ammonium-Protein','Ash': 'Asche','Ca': 'Kalzium','P': 'Phosphor','Mg': 'Magnesium','K':'Kalium','Na':'Natrium','uNDFom30': 'uNDF30','uNDFom120': 'uNDF120','uNDFom240': 'uNDF240', 'S':'Schwefel'})
        ration_append=ration.head(0)
        for r in range(number_rows[0]):
            if table[r].get()==1:
                ration_append=ration_append.append(AnalysenRation.iloc[r], ignore_index = False)
                
        ration_append["Bezeichnung"]=ration_append["Bezeichnung"].fillna("-")
        ration_append=ration_append.fillna(0)
    
        ration_append["Grundfutter NDF"] = ration_append["Grundfutter NDF"]/100
        ration_append["NDF"] = ration_append["Grundfutter NDF"]
        ration_append["uNDF30"] = ration_append["uNDF30"]/100
        ration_append["uNDF120"] = ration_append["uNDF120"]/100
        ration_append["uNDF240"] = ration_append["uNDF240"]/100
        ration_append["NFC"] = ration_append["NFC"]/100
        ration_append["Staerke"] = ration_append["Staerke"]/100
        ration_append["Staerkeverdaulichkeit 7h"] = ration_append["Staerkeverdaulichkeit 7h"]/100
        ration_append["Rohprotein"] = ration_append["Rohprotein"]/100
        ration_append["Asche"] = ration_append["Asche"]/100
        ration_append["Kalzium"] = ration_append["Kalzium"]/100
        ration_append["Phosphor"] = ration_append["Phosphor"]/100
        ration_append["Magnesium"] = ration_append["Magnesium"]/100
        ration_append["Natrium"] = ration_append["Natrium"]/100
        ration_append["Kalium"] = ration_append["Kalium"]/100
        ration_append["Schwefel"] = ration_append["Schwefel"]/100
        ration_append["loesl. Protein"] = ration_append["loesl. Protein"]/100
        ration_append["Ammonium-Protein"] = ration_append["Ammonium-Protein"]/100
        
        rationfenster1=pd.DataFrame()
        rationfenster1=pd.concat([ration_append["Kennung"], ration_append["Komponente"],ration_append["Bezeichnung"],ration_append['Datum'],emptyDataFrame['Kosten ( € /dt )'],ration_append['TS in %']], axis=1, ignore_index=False)
        
        number_rows=rationfenster1.shape
        for r in range(number_rows[0]):
            if rationfenster1.iloc[r,2]=='1':
                rationfenster1.iloc[r,2]='Heu'
            if rationfenster1.iloc[r,2]=='1A':
                rationfenster1.iloc[r,2]='Leguminosen Heu'
            if rationfenster1.iloc[r,2]=='1B':
                rationfenster1.iloc[r,2]='Grassheu'
            if rationfenster1.iloc[r,2]=='1C':
                rationfenster1.iloc[r,2]='gemischte Silage'
            if rationfenster1.iloc[r,2]=='1D':
                rationfenster1.iloc[r,2]='Leguminosen Silage'
            if rationfenster1.iloc[r,2]=='1E':
                rationfenster1.iloc[r,2]='Grasssilage'
            if rationfenster1.iloc[r,2]=='2':
                rationfenster1.iloc[r,2]='Maissilage' 
            if rationfenster1.iloc[r,2]=='3':
                rationfenster1.iloc[r,2]='Körnermais'
            if rationfenster1.iloc[r,2]=='4':
                rationfenster1.iloc[r,2]='Maiskolben'
            if rationfenster1.iloc[r,2]=='5':
                rationfenster1.iloc[r,2]='Getreide'
            if rationfenster1.iloc[r,2]=='6':
                rationfenster1.iloc[r,2]='Nebenprodukte Getreide'
            if rationfenster1.iloc[r,2]=='7':
                rationfenster1.iloc[r,2]='Getreide Silagen'
            if rationfenster1.iloc[r,2]=='8':
                rationfenster1.iloc[r,2]='Oelsamen und Nebenprodukte'
            if rationfenster1.iloc[r,2]=='9':
                rationfenster1.iloc[r,2]='TMR'
            if rationfenster1.iloc[r,2]=='10':
                rationfenster1.iloc[r,2]='sonstiges Futter'
        
        # Kosten und TS eingeben
        
        number_rows=ration_append.shape 
        rationfenster1["Bezeichnung"]=rationfenster1["Bezeichnung"].fillna("-")
        rationfenster1['Kosten ( € /dt )']=rationfenster1['Kosten ( € /dt )'].fillna(0)
        ration_append["Bezeichnung"]=ration_append["Bezeichnung"].fillna("-")
        ration_append=ration_append.fillna(0)
        for r in range(number_rows[0]):
            if ration_append.iloc[r,1]=='1':
                ration_append.iloc[r,1]='Heu'
            if ration_append.iloc[r,1]=='1A':
                ration_append.iloc[r,1]='Leguminosen Heu'
            if ration_append.iloc[r,1]=='1B':
                ration_append.iloc[r,1]='Grassheu'
            if ration_append.iloc[r,1]=='1C':
                ration_append.iloc[r,1]='gemischte Silage'
            if ration_append.iloc[r,1]=='1D':
                ration_append.iloc[r,1]='Leguminosen Silage'
            if ration_append.iloc[r,1]=='1E':
                ration_append.iloc[r,1]='Grasssilage'
            if ration_append.iloc[r,1]=='2':
                ration_append.iloc[r,1]='Maissilage' 
            if ration_append.iloc[r,1]=='3':
                ration_append.iloc[r,1]='Körnermais'
            if ration_append.iloc[r,1]=='4':
                ration_append.iloc[r,1]='Maiskolben'
            if ration_append.iloc[r,1]=='5':
                ration_append.iloc[r,1]='Getreide'
            if ration_append.iloc[r,1]=='6':
                ration_append.iloc[r,1]='Nebenprodukte Getreide'
            if ration_append.iloc[r,1]=='7':
                ration_append.iloc[r,1]='Getreide Silagen'
            if ration_append.iloc[r,1]=='8':
                ration_append.iloc[r,1]='Oelsamen und Nebenprodukte'
            if ration_append.iloc[r,1]=='9':
                ration_append.iloc[r,1]='TMR'
            if ration_append.iloc[r,1]=='10':
                ration_append.iloc[r,1]='sonstiges Futter'
        
        entryKosten=[0] * number_rows[0]
        entryTS=[0] * number_rows[0]

        tkFenster = Tk()
        tkFenster.title("Eintragen der Kosten und aktualisieren der TS")

        c=0
        for col in rationfenster1.columns: 
            Kasten = Label(master=tkFenster, bg='white', text=col, font=('Arial 12 bold'))
            Kasten.grid(row=1, column=c)
            c=c+1
        
        for r in range(number_rows[0]):
            for c in range(6):
                if c<4:
                    Kasten = Label(master=tkFenster, bg='white', text=rationfenster1.iloc[r,c],font='Arial 12 bold')
                    Kasten.grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                if c==4:
                   entryKosten[r] = Entry(master=tkFenster, bg='white')
                   entryKosten[r].config(font='Arial 12 bold',width=20)
                   entryKosten[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                   entryKosten[r].insert(0,rationfenster1.iloc[r,c])
                   
                if c==5:
                    entryTS[r] = Entry(master=tkFenster, bg='white')
                    entryTS[r].config(font='Arial 12 bold',width=10)
                    entryTS[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                    entryTS[r].insert(0,rationfenster1.iloc[r,c])
        
        buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='weiter',font='Arial 12 bold', command=button_Kosten_ration)
        buttonBerechnen.grid(row=r+3, column=c, padx='5', pady='5', sticky='ew')
        
        tkFenster.mainloop()

        ration_append['Kosten ( € /dt )']=Kosten
        ration_append['TS in %']=TS
        
        number_rows_append=ration_append.shape
        number_rows_alt=ration.shape
        for r in range(number_rows_append[0]):
            ration=ration.append(ration_append.iloc[r,0:25])
        
        ration.reset_index(drop=True, inplace=True)
        for r in range(number_rows_append[0]):
            ration_hochleistend = ration_hochleistend.append(ration.iloc[number_rows_alt[0]+r,0:4])
            ration_frischmelker = ration_frischmelker.append(ration.iloc[number_rows_alt[0]+r,0:4])
            ration_altmelker = ration_altmelker.append(ration.iloc[number_rows_alt[0]+r,0:4])
            ration_trockensteher = ration_trockensteher.append(ration.iloc[number_rows_alt[0]+r,0:4])
            ration_rinder = ration_rinder.append(ration.iloc[number_rows_alt[0]+r,0:4])
            ration_bullen = ration_bullen.append(ration.iloc[number_rows_alt[0]+r,0:4])
            
            mischung_hochleistend = mischung_hochleistend.append(ration.iloc[number_rows_alt[0]+r,1:3])
            mischung_frischmelker = mischung_frischmelker.append(ration.iloc[number_rows_alt[0]+r,1:3])
            mischung_altmelker = mischung_altmelker.append(ration.iloc[number_rows_alt[0]+r,1:2])
            mischung_trockensteher = mischung_trockensteher.append(ration.iloc[number_rows_alt[0]+r,1:3])
            mischung_rinder = mischung_rinder.append(ration.iloc[number_rows_alt[0]+r,1:3])
            mischung_bullen = mischung_bullen.append(ration.iloc[number_rows_alt[0]+r,1:3])

        ration["Bezeichnung"] = ration["Bezeichnung"].fillna("-")        
        ration_hochleistend["Bezeichnung"] = ration_hochleistend["Bezeichnung"].fillna("-")
        ration_frischmelker["Bezeichnung"] = ration_frischmelker["Bezeichnung"].fillna("-")
        ration_altmelker["Bezeichnung"] = ration_altmelker["Bezeichnung"].fillna("-")
        ration_trockensteher["Bezeichnung"] = ration_trockensteher["Bezeichnung"].fillna("-")
        ration_rinder["Bezeichnung"] = ration_rinder["Bezeichnung"].fillna("-")
        ration_bullen["Bezeichnung"] = ration_bullen["Bezeichnung"].fillna("-")
        
        ration = ration.fillna(0)
        ration_hochleistend = ration_hochleistend.fillna(0)
        ration_frischmelker = ration_frischmelker.fillna(0)
        ration_altmelker = ration_altmelker.fillna(0)
        ration_trockensteher = ration_trockensteher.fillna(0)
        ration_rinder = ration_rinder.fillna(0)
        ration_bullen = ration_bullen.fillna(0)
        
        mischung_hochleistend["Bezeichnung"] = mischung_hochleistend["Bezeichnung"].fillna("-")
        mischung_frischmelker["Bezeichnung"] = mischung_frischmelker["Bezeichnung"].fillna("-")
        mischung_altmelker["Bezeichnung"] = mischung_altmelker["Bezeichnung"].fillna("-")
        mischung_trockensteher["Bezeichnung"] = mischung_trockensteher["Bezeichnung"].fillna("-")
        mischung_rinder["Bezeichnung"] = mischung_rinder["Bezeichnung"].fillna("-")
        mischung_bullen["Bezeichnung"] = mischung_bullen["Bezeichnung"].fillna("-")
        
        mischung_hochleistend = mischung_hochleistend.fillna(0)
        mischung_frischmelker = mischung_frischmelker.fillna(0)
        mischung_altmelker = mischung_altmelker.fillna(0)
        mischung_trockensteher = mischung_trockensteher.fillna(0)
        mischung_rinder = mischung_rinder.fillna(0)
        mischung_bullen = mischung_bullen.fillna(0)
    else:
        continue
    

ration['index']=ration.index    
ration_bullen['index']=ration_bullen.index
ration_rinder['index']=ration_rinder.index
ration_trockensteher['index']=ration_trockensteher.index
ration_altmelker['index']=ration_altmelker.index
ration_frischmelker['index']=ration_frischmelker.index
ration_hochleistend['index']=ration_hochleistend.index
    
  
os.chdir('/home/thomas/.config/spyder-py3/Projekt1/Gespeicherte Rationen')   
writer=pd.ExcelWriter(str(NameRation)+'.xlsx',engine='xlsxwriter')        
combined_dfs={'Analysen':ration, 'Ration_hochleistend':ration_hochleistend,'Ration_frischmelkend':ration_frischmelker,
              'Ration_altmelkend':ration_altmelker,'Ration_trockenstehend':ration_trockensteher, 'Ration_Rinder':ration_rinder,
              'Ration_Bullen':ration_bullen}
for sheet_name in combined_dfs.keys():
    combined_dfs[sheet_name].to_excel(writer,sheet_name=sheet_name, index=False)
writer.save

mischung_ziel=mischung_hochleistend
    #mischung_ziel=mischung_ziel.rename(columns={'Reihenfolge': 'Lade- \n reihenf.', 'kg Frischmasse': 'kg Frischm.','untere Lademenge': 'untere \n Ladem.','normale Lademenge': 'normale \n Ladem.','obere Lademenge': 'obere \n Ladem.'})
   
    
pdf = FPDF()
for x in range(len(table1)):
    if table1[x].get()==1:
        pdf.add_page()
        pdf.set_font('Arial', 'B', 20)
        if x==0:
            pdf.cell(30, 20, 'Mischtabelle für hochleistende Kühe', ln=1)
            Anzahl=Anzahl_hochleistend
            Varianz=Varianz_hochleistend
            mischung_ziel=mischung_hochleistend
            ration_ziel=ration_hochleistend
            Milchpreis=Milchpreis_hochleistend
            Milchmenge=Milchmenge_hochleistend
            Futterreste=Futterreste_hochleistend
        if x==1:
            pdf.cell(30, 20, 'Mischtabelle für frischmelkende Kühe', ln=1)
            Anzahl=Anzahl_frischmelker
            Varianz=Varianz_frischmelker
            mischung_ziel=mischung_frischmelker
            ration_ziel=ration_frischmelker
            Milchpreis=Milchpreis_frischmelker
            Milchmenge=Milchmenge_frischmelker
            Futterreste=Futterreste_frischmelker
        if x==2:
            pdf.cell(30, 20, 'Mischtabelle für altmelkende Kühe', ln=1)
            Anzahl=Anzahl_altmelker
            Varianz=Varianz_altmelker
            mischung_ziel=mischung_altmelker
            ration_ziel=ration_altmelker
            Milchpreis=Milchpreis_altmelker
            Milchmenge=Milchmenge_altmelker
            Futterreste=Futterreste_altmelker
        if x==3:
            pdf.cell(30, 20, 'Mischtabelle für trockenstehende Kühe', ln=1)
            Anzahl=Anzahl_trockensteher
            Varianz=Varianz_trockensteher
            mischung_ziel=mischung_trockensteher
            ration_ziel=ration_trockensteher
            Milchpreis=Milchpreis_trockensteher
            Milchmenge=Milchmenge_trockensteher
            Futterreste=Futterreste_trockensteher
        if x==4:
            pdf.cell(30, 20, 'Mischtabelle für Rinder', ln=1)
            Anzahl=Anzahl_rinder
            Varianz=Varianz_rinder
            mischung_ziel=mischung_rinder
            ration_ziel=ration_rinder
            Milchpreis=Milchpreis_rinder
            Milchmenge=Milchmenge_rinder
            Futterreste=Futterreste_rinder
        if x==5:
            pdf.cell(30, 20, 'Mischtabelle für Bullen', ln=1)
            Anzahl=Anzahl_bullen
            Varianz=Varianz_bullen
            mischung_ziel=mischung_bullen
            ration_ziel=ration_bullen
            Milchpreis=Milchpreis_bullen
            Milchmenge=Milchertrag_bullen
            Futterreste=Futterreste_bullen
#        if x==0:
#            pdf.cell(30, 20, 'Mischtabelle für hochleistende Kühe', ln=1)
        os.chdir('/home/thomas/.config/spyder-py3/Projekt1/')
        pdf.image('agroprax1.png', 150, 8, 50)
        today = date.today()
        Datum=today.strftime("%d/%m/%Y")
        Ersteller = getpass.getuser()
        
        pdf.set_font('Arial', 'B', 17)
        pdf.cell(15)
        pdf.cell(50, 15, 'Betrieb: ' +str(NameRation))
        pdf.cell(pdf.w/5)
        pdf.cell(20, 15, 'Datum: '+str(Datum))
        pdf.ln(10)
        pdf.cell(15)
        pdf.cell(50, 10, 'Ersteller: '+str(Ersteller))
        pdf.cell(pdf.w/5)
        pdf.cell(0, 10, 'Gruppe: ')
        pdf.set_font('Arial', 'B', 12)
        col_width = pdf.w
        row_height = pdf.font_size
        number_rows=mischung_ziel.shape
        
        pdf.cell(pdf.w/2)
        pdf.cell(col_width/10, row_height*3,txt='Kuhzahl', border=1)
        pdf.cell(col_width/10, row_height*3,txt=str(Anzahl-Varianz), border=1)
        pdf.cell(col_width/10, row_height*3,txt=str(Anzahl), border=1)
        pdf.cell(col_width/10, row_height*3,txt=str(Anzahl+Varianz), border=1)
        pdf.ln(row_height*3)
        pdf.cell(col_width/10, row_height*3,txt='LadeReFo', border=1)
        pdf.cell(col_width/5, row_height*3,txt='Komponente', border=1)
        pdf.cell(col_width/5, row_height*3,txt='Bezeichnung', border=1)
        pdf.cell(col_width/10, row_height*3,txt='kg Frism.', border=1)
        pdf.cell(col_width/10, row_height*3,txt='u. Ladem.', border=1)
        pdf.cell(col_width/10, row_height*3,txt='n. Ladem.', border=1)
        pdf.cell(col_width/10, row_height*3,txt='o. Ladem.', border=1)
        pdf.ln(row_height*3)
        for r in range(number_rows[0]):
            for c in range(7):
                if c==1 or c==2:
                    pdf.cell(col_width/5, row_height*1.5,txt=str(mischung_ziel.iloc[r,c]), border=1)
                else:
                    pdf.cell(col_width/10, row_height*1.5,txt=str(mischung_ziel.iloc[r,c]), border=1)
            pdf.ln(row_height*1.5)
        pdf.cell(col_width/10, row_height*3,txt='Gesamt:', border=1)
        pdf.cell(pdf.w/2.5)
        pdf.cell(col_width/10, row_height*3,txt=str(round(mischung_ziel["kg Frischmasse"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(col_width/10, row_height*3,txt=str(round(mischung_ziel["untere Lademenge"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(col_width/10, row_height*3,txt=str(round(mischung_ziel["normale Lademenge"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(col_width/10, row_height*3,txt=str(round(mischung_ziel["obere Lademenge"].sum(axis = 0, skipna = True),2)), border=1)
        
            
        pdf.ln(row_height*5)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(pdf.w /6, row_height*2, 'Frischmasse(kg):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["kg Frischmasse"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(pdf.w /6, row_height*2, 'GNDF (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["GNDF"].sum(axis = 0, skipna = True),2)), border=1) 
        pdf.cell(pdf.w /6, row_height*2, 'Phosphor (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["Phosphor"].sum(axis = 0, skipna = True),2)), border=1)   
        pdf.ln(row_height*2)
        pdf.cell(pdf.w /6, row_height*2, 'TS (kg):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["TS"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(pdf.w /6, row_height*2, 'NFC (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["NFC"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(pdf.w /6, row_height*2, 'Magnesium (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["Magnesium"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.ln(row_height*2)
        pdf.cell(pdf.w /6, row_height*2, '% TS:', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["TS"].sum(axis = 0, skipna = True)/ration_ziel["kg Frischmasse"].sum(axis = 0, skipna = True)*100,2)), border=1)
        pdf.cell(pdf.w /6, row_height*2, 'Rohprotein (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["Rohprotein"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(pdf.w /6, row_height*2, 'Kalium (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["Kalium"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.ln(row_height*2)
        pdf.cell(pdf.w /6, row_height*2, 'MJNEL:', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["MJ NEL"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(pdf.w /6, row_height*2, 'Staerke:', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["Staerke"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(pdf.w /6, row_height*2, 'Natrium (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["Natrium"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.ln(row_height*2)
        pdf.cell(pdf.w /6, row_height*2, 'MJNEL/kgTS:', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)/ration_ziel["TS"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(pdf.w /6, row_height*2, 'Asche (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["Asche"].sum(axis = 0, skipna = True),2)), border=1) 
        pdf.cell(pdf.w /6, row_height*2, 'Schwefel (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["Schwefel"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.ln(row_height*2)
        pdf.cell(pdf.w /6, row_height*2, 'NDF (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["NDF"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(pdf.w /6, row_height*2, 'Kalzium (%):', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["Kalzium"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.cell(pdf.w /6, row_height*2, 'K/Mg:', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(ration_ziel["Kalium"].sum(axis = 0, skipna = True)/ration_ziel["Magnesium"].sum(axis = 0, skipna = True),2)), border=1)
        pdf.ln(row_height*2)
        pdf.ln(row_height*2)
        
        Kosten=ration_ziel['Kosten'].sum(axis = 0, skipna = True)
        Kostenplus=Kosten*(float(Futterreste)/100+1)
        Umsatz=Milchmenge*Milchpreis/100
        IOFC=Umsatz-Kostenplus
        
        pdf.cell(pdf.w /6, row_height*2, 'Futterreste:', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(Futterreste)), border=1)
        pdf.cell(pdf.w /7, row_height*2,  "%", border=1)
        pdf.cell(pdf.w /6, row_height*2, 'Kosten:', border=1)    
        pdf.cell(pdf.w /9, row_height*2, str(round(Kostenplus,2)), border=1)
        pdf.cell(pdf.w /7, row_height*2,  "Euro/Tag/Kuh", border=1)
        
        pdf.ln(row_height*2)
        pdf.cell(pdf.w /6, row_height*2, 'Milchmenge:', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(Milchmenge)), border=1)
        pdf.cell(pdf.w /7, row_height*2,  "Liter/Tag/Kuh", border=1)    
        pdf.cell(pdf.w /6, row_height*2, 'Umsatz', border=1)    
        pdf.cell(pdf.w /9, row_height*2, str(round(Umsatz,2)), border=1)
        pdf.cell(pdf.w /7, row_height*2,  "Euro/Tag/Kuh", border=1)
        pdf.ln(row_height*2)
        
        pdf.cell(pdf.w /6, row_height*2, 'Milchpreis:', border=1)
        pdf.cell(pdf.w /9, row_height*2, str(round(Milchpreis,2)), border=1)
        pdf.cell(pdf.w /7, row_height*2,  "ct/kg", border=1)
        pdf.cell(pdf.w /6, row_height*2, 'IOFC', border=1)    
        pdf.cell(pdf.w /9, row_height*2, str(round(IOFC,2)), border=1)
        pdf.cell(pdf.w /7, row_height*2,  "Euro/Tag/Kuh", border=1)
      
pdf.output("asd.pdf")


print('fertig')