#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:55:14 2019

@author: thomas
"""
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
    global status1
    status1='fertig'
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
    
def ButtonweitereBetriebe():
    global status1
    status1 ='weitere Betriebe'
    root.destroy()
    return 

def buttonKosten():
    global Kosten, TS
    Kosten= [0] * asd
    TS= [0] * asd
    for x in range(asd):
        Kosten[x] = entryKosten[x].get()
        TS[x] = entryTS[x].get()
    Tk.destroy(tkFenster)
    return


            

pd.read_csv = functools.partial(pd.read_csv, low_memory=False)    

#öffnen Startbildschirm
tkFenster = Tk()
tkFenster.title('Fütterungsprogramm')
tkFenster.geometry('600x450')    

os.chdir('/home/thomas/.config/spyder-py3/Projekt1/')
img = PhotoImage(file="agroprax.png")
canvas = Canvas(master=tkFenster, width=600, height=360)
canvas.pack()
#canvas.place(x=0, y=0, width=500, height=350)
canvas.create_image(12, 60, image=img, anchor='nw')
header = Label(master=tkFenster, text='Herzlich Willkommen beim Fütterungsprogramm der ', fg='black', bg='white', font='Arial 14 bold')
header.place(x=12, y=5, width=575, height=60)
header = Label(master=tkFenster, text='Soll eine neue Ration erschaffen\n oder eine alte aktualisiert werden?', fg='black', bg='white', font='Arial 14 bold')
header.place(x=12, y=360, width=575, height=60)

# Button
buttonaktualisieren = Button(master=tkFenster, text='neu', bg='#FFCFC9', command=buttonneu)
buttonaktualisieren.place(x=5, y=420, width=100, height=30)
buttonneu = Button(master=tkFenster, text='aktualisieren', bg='#D5E88F', command=buttonaktualisieren)
buttonneu.place(x=490, y=420, width=100, height=30)

tkFenster.mainloop()


if status == "neu":
    #Auswahl Query
    list_of_files = glob.glob('/home/thomas/.config/spyder-py3/Projekt1/queries/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    if  latest_file.endswith('.csv'):
        os.rename(latest_file, '/home/thomas/.config/spyder-py3/Projekt1/queries/latest_query.csv')
    else: 
        print("Keine aktuelle .csv Query-Datei in Downloads in vorhanden")
  
    os.chdir('/home/thomas/.config/spyder-py3/Projekt1/queries/')
    filename='latest_query.csv'
    Analysen = pd.read_csv(filename,encoding='latin-1')


    
list1 = Analysen['Sampled For'].astype(str)
autocompleteList=list(set(list1))

status1='unfertig'
if status1 !='fertig':
    tkFenster = Tk()
    tkFenster.title('Auswahl des Betriebes')
    tkFenster.geometry('425x250')
    #tkFenster.bind('<Return>', buttonauswählen)
    #tkFenster.bind("<Button-1>", buttonauswählen)
    Labelueberschrift=Label(master=tkFenster, text= "Die Analysen welcher Betriebe soll genutzt werden?", font='Arial 10 bold')
    Labelueberschrift.place(x=30, y=20)
    EingabeBetrieb = AutocompleteEntry(autocompleteList, tkFenster, listboxLength=12, width=56, x=10,  matchesFunction=matches)
    EingabeBetrieb.place(x=10, y=40)
    EingabeBetrieb1 = AutocompleteEntry(autocompleteList, tkFenster, listboxLength=12, width=56, x=10,  matchesFunction=matches)
    EingabeBetrieb1.place(x=10, y=80)
    EingabeBetrieb2 = AutocompleteEntry(autocompleteList, tkFenster, listboxLength=12, width=56, x=10,  matchesFunction=matches)
    EingabeBetrieb2.place(x=10, y=120)
     
    ButtonAuswahl=Button(master=tkFenster, text='auswählen',bg='#D5E88F', command=buttonauswählen)
    ButtonAuswahl.place(x=307, y=150, width=100, height=50)
    ButtonAbbruch=Button(master=tkFenster, text='abbrechen',bg='#FFCFC9', command=buttonabbrechen)
    ButtonAbbruch.place(x=10, y=150, width=100, height=50)
    
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
            
    emptyDataFrame = pd.DataFrame(columns=['Maske','Kosten ( € /dt )', 'kg Frischmasse', '% der Ration TS','Kationen','Anionen','Rohprotein','Grundfutter NDF','Reihenfolge'])        
    #Kennung	Komponente Bezeichnung	Kosten     	kg Frichmasse	 % der Ration in TS	TS in% 	MJ NEL	NDF	G NDF	ADF	Lignin	NSC	Stärke	Zucker	Roh- protein	lösl. Protein	Asche	Ca	P	Mg	K	Na	S	Kationen	Anionen
    AnalysenRation=pd.concat([emptyDataFrame['Maske'],AnalysenBetrieb["Sampled For"], AnalysenBetrieb["Product Type"],AnalysenBetrieb["Description 1"],emptyDataFrame['Kosten ( € /dt )'],
                             AnalysenBetrieb["Dry Matter"],AnalysenBetrieb["NEL OARDC"]/100*2.2/0.236, AnalysenBetrieb["aNDFom"],emptyDataFrame["Grundfutter NDF"], AnalysenBetrieb["ADF"],AnalysenBetrieb["Lignin"],AnalysenBetrieb["NFC"],
                             AnalysenBetrieb["Starch"],AnalysenBetrieb["WSC (Sugar)"],AnalysenBetrieb['Adjusted CP'], AnalysenBetrieb["Soluble Protein"], AnalysenBetrieb["Ash"],AnalysenBetrieb["Ca"],AnalysenBetrieb["P"],
                             AnalysenBetrieb["Mg"],AnalysenBetrieb["Na"],AnalysenBetrieb["K"],AnalysenBetrieb["S"],emptyDataFrame['Kationen'],emptyDataFrame['Anionen']], axis=1, ignore_index=False)
#        AnalysenRation=AnalysenRation.reindex(columns = header_list)
#        header_list = ["Sampled For","Product Type","Description 1", "Kosten ( € /dt )","kg Frichmasse","% der Ration                         TS","Dry Matter","NEL OARDC","aNDFom","ADF","Lignin","NFC","Starch","WSC (Sugar)","Soluble Protein","Ash","Ca", "P","Mg","S"]
    AnalysenRation["Grundfutter NDF"]=AnalysenRation["aNDFom"]
    AnalysenRation, NAlist = reduce_mem_usage(AnalysenRation)
    AnalysenBetriebFenster=pd.concat([AnalysenBetrieb["Field Name"], AnalysenBetrieb["Date Processed"],AnalysenBetrieb["Sampled For"], AnalysenBetrieb["Product Type"],AnalysenBetrieb["Description 1"]], axis=1, ignore_index=False)
    tkFenster = Tk()
    tkFenster.title('Auswahl Analysen')
    table=[]
    number_rows=AnalysenBetriebFenster.shape 
    for x in range(number_rows[0]):
        table.append('var_'+str(x))
        table[x]=IntVar()
        
    header = Label(master=tkFenster, text='ausgewählt', fg='black', bg='white', font='Arial 12 bold',width = 15, height = 2,)
    header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
    header = Label(master=tkFenster, text='Datum', fg='black', bg='white', font='Arial 12 bold',width = 15, height = 2,)
    header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
    header = Label(master=tkFenster, text='Kennung', fg='black', bg='white', font='Arial 12 bold',width = 15, height = 2,)
    header.grid(row=0, column=2, padx='1', pady='1', sticky='ew')
    header = Label(master=tkFenster, text='Futter', fg='black', bg='white', font='Arial 12 bold',width = 15, height = 2,)
    header.grid(row=0, column=3, padx='1', pady='1', sticky='ew')
    header = Label(master=tkFenster, text='Bezeichnung', fg='black', bg='white', font='Arial 12 bold',width = 15, height = 2,)
    header.grid(row=0, column=4, padx='1', pady='1', sticky='ew')
    
    
    for r in range(number_rows[0]):
        for c in range(number_rows[1]):
            if c == 0:
                checkbutton = Checkbutton(master=tkFenster, anchor='w',offvalue=0, onvalue=1, variable=table[r])
                checkbutton.grid(row=r+1, column=c, padx='5', pady='5', sticky='ew')
            else:
                Kasten = Label(master=tkFenster, bg='white', text=AnalysenBetriebFenster.iloc[r,c])
                Kasten.grid(row=r+1, column=c, padx='5', pady='5', sticky='ew')
        

    Buttonauswahlanalysen = Button(master=tkFenster, text='weiter', bg='#D5E88F', command=Buttonauswahlanalysen)
    Buttonauswahlanalysen.grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
    ButtonweitereBetriebe = Button(master=tkFenster, text='weitere Betriebe', bg='#D5E88F', command=ButtonweitereBetriebe)
    ButtonweitereBetriebe.grid(row=r+2, column=0, padx='5', pady='5', sticky='ew')
    
    tkFenster.mainloop()    
    ration=AnalysenRation.head(0)
    for r in range(number_rows[0]):
        if table[r].get()==1:
            ration=ration.append(AnalysenRation.iloc[r], ignore_index = True)
                
    ration = ration.rename(columns={'Sampled For': 'Kennung', 'Product Type': 'Komponente','Description 1': 'Bezeichnung','Dry Matter': 'TS in %','NEL OARDC': 'MJ NEL','aNDFom': 'NDF','Starch': 'Staerke','WSC (Sugar)': 'Zucker','Soluble Protein': 'loesl. Protein', 'Adjusted CP': 'Rohprotein',
                                    'Ash': 'Asche','Ca': 'Kalzium','P': 'Phosphor','Mg': 'Magnesium','K':'Kalium','Na':'Natrium', 'S':'Schwefel'})
    
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
    canvas = Canvas(frame_header,width=700, height=20, bg="gray85")
    canvas.grid(row=0, column=0, sticky="news")

    frame_canvas = Frame(frame_main)
    frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    
    # Add a canvas in that frame
    canvas = Canvas(frame_canvas,width=700, height=800, bg="gray85")
    canvas.grid(row=0, column=0, sticky="news")
    
    # Link a scrollbar to the canvas
    vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)
    
#    hsbar = Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
#    hsbar.grid(row=1, column=0, sticky="EW")
#    canvas.configure(xscrollcommand=hsbar.set)
    
    # Create a frame to contain the labels
    frame_labels = Frame(canvas, bg="gray85")
    canvas.create_window((0, 0), window=frame_labels, anchor='nw')
    header = Label(master=frame_labels, text='ausgewählt', fg='black', bg='white', font=('Arial 12 bold'))
    header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
    header = Label(master=frame_labels, text='Kennung', fg='black', bg='white', font=('Arial 12 bold'))
    header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
    header = Label(master=frame_labels, text='Futter', fg='black', bg='white', font=('Arial 12 bold'))
    header.grid(row=0, column=2, padx='1', pady='1', sticky='ew')
    header = Label(master=frame_labels, text='Bezeichnung', fg='black', bg='white', font=('Arial 12 bold'))
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
                checkbutton[r] = Checkbutton(master=frame_labels, anchor='w',offvalue=0, onvalue=1, variable=table[r])
                checkbutton[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
            else:
                Kasten[r][c] = Label(master=frame_labels, bg='white', text=KomponentenFenster.iloc[r,c])
                Kasten[r][c].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
    
    # Update buttons frames idle tasks to let tkinter calculate buttons sizes
    frame_labels.update_idletasks()
    
    # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
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
        Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F', command=Buttonauswahlmineral)
    if y==1:
        Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F', command=Buttonauswahlfeucht)    
    if y==2:
        Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F', command=Buttonauswahltrocken) 
                                       
    Buttonauswahlanalysen.grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
#    ButtonweitereBetriebe = Button(master=tkFenster, text='weitere Betriebe', bg='#D5E88F', command=ButtonweitereBetriebe)
#    ButtonweitereBetriebe.grid(row=r+2, column=0, padx='5', pady='5', sticky='ew')

    root.mainloop()     
            
    for r in range(number_rows[0]):
        if table[r].get()==1:
            ration=ration.append(Komponenten.iloc[r])    

rationfenster=pd.concat([ration["Kennung"], ration["Komponente"],ration["Bezeichnung"],ration['Kosten ( € /dt )'],ration['TS in %']], axis=1, ignore_index=False)

# Kosten und TS eingeben

number_rows=rationfenster.shape 

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
           entryKosten[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
            
        if c==4:
            entryTS[r] = Entry(master=tkFenster, bg='white')
            entryTS[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
            entryTS[r].insert(0,rationfenster.iloc[r,c])
global asd
asd=number_rows[0]
buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='weiter', command=buttonKosten)
buttonBerechnen.grid(row=r+3, column=c, padx='5', pady='5', sticky='ew')

tkFenster.mainloop()



for x in range(number_rows[0]):
    if Kosten[x]=='':
        Kosten[x]=0
    else:
        Kosten[x]=float(Kosten[x])
  
    
    if TS[x]!='':
        ration.iloc[x,7]=float(TS[x])
    else:
        ration.iloc[x,7]=rationfenster.iloc[x,4]

ration['Kosten ( € /dt )']=Kosten
ration=ration.drop(["Maske"],axis=1)
ration, NAlist = reduce_mem_usage(ration)

def Gruppenweiter():
    tkFenster.destroy()
    return 

Gruppen=[]
Gruppen=['Hochleistende Kuehe', 'Frischmelker','Altmelker','Trockensteher', 'Rinder','Bullen', 'x',] 

table1=[]
tkFenster = Tk()
tkFenster.title("Auswahl der Gruppen")
for x in range(len(Gruppen)):
        table1.append('var_'+str(x))
        table1[x]=IntVar()
        

header = Label(master=tkFenster, text='ausgewählt', fg='black', bg='white', font=('Arial 12 bold'))
header.grid(row=1, column=0, padx='1', pady='1', sticky='ew')
header = Label(master=tkFenster, text='Gruppenname', fg='black', bg='white', font=('Arial 12 bold'))
header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')

        
checkbutton=[Checkbutton() for r in range(len(Gruppen))]  
Kasten=[Label() for r in range(len(Gruppen))] 
for r in range(len(Gruppen)):
        checkbutton[r] = Checkbutton(master=tkFenster, anchor='w',offvalue=0, onvalue=1, variable=table1[r])
        checkbutton[r].grid(row=r+2, column=0, padx='5', pady='5', sticky='ew')
        Kasten[r] = Label(master=tkFenster, bg='white', text=Gruppen[r])
        Kasten[r].grid(row=r+2, column=1, padx='5', pady='5', sticky='ew')
        
Buttonauswahlanalysen = Button(master=tkFenster, text='weiter', bg='#D5E88F', command=Gruppenweiter)                 
Buttonauswahlanalysen.grid(row=r+3, column=1, padx='5', pady='5', sticky='ew')
        
tkFenster.mainloop()
status=''    
while status!='weiter': 
    L=[]
    L=['Kosten', 'kg Frischmasse','% der Ration TS','TS', 'MJ NEL', 'NDF', 'GNDF', 'NFC', 'Staerke','Zucker', 'Rohprotein', 'loesl. Protein', 'Asche' , 'Ca', 'P', 'Mg', 'K', 'Na', 'S', 'Kationen', 'Anionen']        
    ration_ziel=pd.concat([emptyDataFrame['Reihenfolge'],ration['Kennung'],ration['Komponente'],ration['Bezeichnung']], axis=1, ignore_index=False)
    for col in L:
        ration_ziel[col] = 0
    
    ration_hochleistend=ration_frischmelker=ration_altmelker=ration_trockensteher=ration_rinder=ration_bullen=ration_ziel

    def buttonMineral():
        parent.destroy()
        global status
        status='mineral'
        return
    
    def buttonFeucht():
        parent.destroy()
        global status
        status='feucht'
        return
    
    def buttonTrocken():
        parent.destroy()
        global status
        status='trocken'
        return
   
    def buttonBerechnen():
        global FM
        FM= [0] * asd
        for x in range(asd):
            FM[x] = entryFM[x].get()
        
        for x in range(number_rows[0]):
            FM[x]=float(FM[x])
        ration['kg Frischmasse']=ration_ziel['kg Frischmasse']=FM
        #    ration_ziel=ration_ziel.sort_values(by=['kg Frischmasse'], ascending=False)
        #    ration=ration.sort_values(by=['kg Frischmasse'], ascending=False)
        ration_ziel['TS']=ration_ziel['kg Frischmasse'].mul(ration['TS in %'])/100
        ration_ziel['Kosten']= ration_ziel['kg Frischmasse'].mul(ration['Kosten ( € /dt )'])/100
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        ration_ziel['% der Ration TS']= ration_ziel['TS']/TS 
        ration_ziel['MJ NEL']=ration_ziel['TS'].mul(ration['MJ NEL'])
        ration_ziel['NDF']=ration_ziel['TS'].mul(ration['NDF']) 
        ration_ziel['GNDF']=ration_ziel['TS'].mul(ration['Grundfutter NDF'])
        ration_ziel['NFC']=ration_ziel['TS'].mul(ration['NFC'])
        ration_ziel['Staerke']=ration_ziel['TS'].mul(ration['Staerke'])
        ration_ziel['NDF']=ration_ziel['TS'].mul(ration['NDF'])
        ration_ziel['Rohprotein']=ration_ziel['TS'].mul(ration['Rohprotein'])
        ration_ziel['loesl. Protein']=ration_ziel['TS'].mul(ration['loesl. Protein'])
        ration_ziel['Asche']=ration_ziel['TS'].mul(ration['Asche'])
        ration_ziel['Ca']=ration_ziel['TS'].mul(ration['Kalzium'])
        ration_ziel['P']=ration_ziel['TS'].mul(ration['Phosphor'])
        ration_ziel['Mg']=ration_ziel['TS'].mul(ration['Magnesium'])
        ration_ziel['K']=ration_ziel['TS'].mul(ration['Kalium'])
        ration_ziel['Na']=ration_ziel['TS'].mul(ration['Natrium'])
        ration_ziel['S']=ration_ziel['TS'].mul(ration['Schwefel'])
        ration_ziel['Kationen']=ration_ziel['TS'].mul(ration['Kationen'])
        ration_ziel['Anionen']=ration_ziel['TS'].mul(ration['Anionen'])
        
        Frischmasse=ration_ziel["kg Frischmasse"].sum(axis = 0, skipna = True)
        TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        PTS=Frischmasse/TS
        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
        MJNELkg=MJNEL/TS
    
        NDF=ration_ziel["NDF"].sum(axis = 0, skipna = True)/TS
        GNDF=ration_ziel["GNDF"].sum(axis = 0, skipna = True)/TS
        NFC=ration_ziel["NFC"].sum(axis = 0, skipna = True)/TS
        RP=ration_ziel["Rohprotein"].sum(axis = 0, skipna = True)/TS
        Staerke=ration_ziel["Staerke"].sum(axis = 0, skipna = True)/TS
        
        Asche=ration_ziel["Asche"].sum(axis = 0, skipna = True)/TS*100
        Ca=ration_ziel["Ca"].sum(axis = 0, skipna = True)/TS*100
        P=ration_ziel["P"].sum(axis = 0, skipna = True)/TS*100
        Mg=ration_ziel["Mg"].sum(axis = 0, skipna = True)/TS*100
        K=ration_ziel["K"].sum(axis = 0, skipna = True)/TS*100
         
        Na=ration_ziel["Na"].sum(axis = 0, skipna = True)/TS*100
        S=ration_ziel["S"].sum(axis = 0, skipna = True)/TS*100
        Kosten=ration_ziel['Kosten'].sum(axis = 0, skipna = True)/TS
        
        Futterreste = float(Futterresteentry.get())
        Milchmenge = float(Milchertragentry.get())
        Milchpreis = float(Milchpreisentry.get())
        Faktor = float(Faktorentry.get())
        
        Kostenplus=Kosten*(float(Futterreste)/100+1)
        Umsatz=Milchmenge*Milchpreis/100
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
        header = Label(master=tkFenster, text=round(K/Mg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=10, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text=round(Kosten,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(Kostenplus,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(IOFC,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(Umsatz,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=3, column=16, padx='1', pady='1', sticky='ew')
       
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c==4:
                    entryFM[r] = Entry(master=tkFenster, bg='white')
                    entryFM[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM[r].insert(0,ration_ziel.iloc[r,c])
                elif c>3:
                    Kasten = Label(master=tkFenster, bg='white', text=round(ration_ziel.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c) 
                else:
                    Kasten = Label(master=tkFenster, bg='white', text=ration_ziel.iloc[r,c])
                    Kasten.grid(row=r+6, column=c)
        return
    
    
    def buttonWeiter():
        global status
        status='weiter'
        Tk.destroy(parent)
        return
    
    def buttonAktualisierenMischung():
        
        
        header = Label(master=f3, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
        EntryAnzahl = Entry(master=f3, bg='white')
        EntryAnzahl.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=f3, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
        EntryVar = Entry(master=f3, bg='white')
        EntryVar.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
        
#        header = Label(master=f3, text='Komponeten:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
#        header.grid(row=3, column=0, padx='1', pady='1', sticky='ew')
#        header = Label(master=f3, text='Bezeichnung:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
#        header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
#        header = Label(master=f3, text='Frischmasse pro Kuh:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
#        header.grid(row=3, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=f3, text=Anzahl-Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=f3, text=Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=f3, text=Anzahl +Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=5, padx='1', pady='1', sticky='ew')
        
        for r in range(number_rows[0]):
            Kasten = Label(master=f3, bg='white', text=ration_ziel.iloc[r,1])
            Kasten.grid(row=r+4, column=0)
            Kasten = Label(master=f3, bg='white', text=ration_ziel.iloc[r,2])
            Kasten.grid(row=r+4, column=1)
            Kasten = Label(master=f3, bg='white', text=ration_ziel.iloc[r,4])
            Kasten.grid(row=r+4, column=2) 
            Kasten = Label(master=f3, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl-Varianz))
            Kasten.grid(row=r+4, column=3)
            Kasten = Label(master=f3, bg='white', text=ration_ziel.iloc[r,4]*Anzahl)
            Kasten.grid(row=r+4, column=4)
            Kasten = Label(master=f3, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl+Varianz))
            Kasten.grid(row=r+4, column=5)
            
        header = Label(master=f3, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=f3, text=Frischmasse*(Anzahl-Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=f3, text=Frischmasse*Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
        header = Label(master=f3, text=Frischmasse*(Anzahl+Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
        
        return
    
    Varianz=Anzahl=Milchpreis=Futterreste=Faktor=Milchertrag=Milchmenge=0    
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
    if table1[6].get()==1:
        Ration_x  = ttk.Frame(n)   # second page
        Mischung_x =ttk.Frame(n)#
        n.add(Ration_x, text='Ration_x')
        n.add(Mischung_x, text='Mischung_x')
    
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
    canvas = Canvas(frame_canvas,width=800, height=400, bg="gray85")
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
                Kasten = Label(master=frame_labels, bg='white', text=ration.iloc[r,c+1])
                Kasten.grid(row=r+1, column=c, padx='5', pady='5', sticky='ew')
    c=0
    for col in ration.columns: 
        Kasten = Label(master=frame_labels, bg='white', text=col)
        Kasten.grid(row=0, column=c)
        c=c+1
    
    buttonmineral = Button(master=frame_labels, bg='#FBD975', text='Mineralfutter\n hinzufügen', command=buttonMineral)
    buttonmineral.grid(row=number_rows[0]+1, column=0, padx='5', pady='5', sticky='ew')
    buttonFeucht = Button(master=frame_labels, bg='#FBD975', text='Trockene Komponente\n hinzufügen', command=buttonFeucht)
    buttonFeucht.grid(row=number_rows[0]+1,column=1, padx='5', pady='5', sticky='ew')
    buttonTrocken = Button(master=frame_labels, bg='#FBD975', text='Feuchte Komponente\n hinzufügen', command=buttonTrocken)
    buttonTrocken.grid(row=number_rows[0]+1,column=2, padx='5', pady='5', sticky='ew')
    
    
    
    table=[]
    number_rows=ration_ziel.shape 
#    Frischmasse=ration_ziel["kg Frischmasse"].sum(axis = 0, skipna = True)
#    TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
#    MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
#    if TS==0:
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
#    else:
#        PTS=Frischmasse/TS
#        MJNEL=ration_ziel["MJ NEL"].sum(axis = 0, skipna = True)
#        MJNELkg=MJNEL/TS
#        
#        NDF=ration_ziel["NDF"].sum(axis = 0, skipna = True)/TS
#        GNDF=ration_ziel["GNDF"].sum(axis = 0, skipna = True)/TS
#        NFC=ration_ziel["NFC"].sum(axis = 0, skipna = True)/TS
#        RP=ration_ziel["Rohprotein"].sum(axis = 0, skipna = True)/TS
#        Staerke=ration_ziel["Staerke"].sum(axis = 0, skipna = True)/TS
#        
#        Asche=ration_ziel["Asche"].sum(axis = 0, skipna = True)/TS*100
#        Ca=ration_ziel["Ca"].sum(axis = 0, skipna = True)/TS*100
#        P=ration_ziel["P"].sum(axis = 0, skipna = True)/TS*100
#        Mg=ration_ziel["Mg"].sum(axis = 0, skipna = True)/TS*100
#        K=ration_ziel["K"].sum(axis = 0, skipna = True)/TS*100
#         
#        Na=ration_ziel["Na"].sum(axis = 0, skipna = True)/TS*100
#        S=ration_ziel["S"].sum(axis = 0, skipna = True)/TS*100
#        Kosten=ration_ziel['Kosten'].sum(axis = 0, skipna = True)/TS
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
        
        if x==0 and table1[x].get()!=1:
            continue
        
        if x==1 and table1[x].get()==1:
            Ration_Frischmelker.grid_rowconfigure(0, weight=1)
            Ration_Frischmelker.columnconfigure(0, weight=1)
            frame_main = Frame(Ration_Frischmelker,  bg="gray85")
            
        if x==1 and table1[x].get()!=1:
            continue
            
        if x==2 and table1[x].get()==1:
            Ration_Altmelker.grid_rowconfigure(0, weight=1)
            Ration_Altmelker.columnconfigure(0, weight=1)
            frame_main = Frame(Ration_Altmelker,  bg="gray85")
        
        if x==2 and table1[x].get()!=1:
            continue
            
        if x==3 and table1[x].get()==1:
            Ration_Trockensteher.grid_rowconfigure(0, weight=1)
            Ration_Trockensteher.columnconfigure(0, weight=1)
            frame_main = Frame(Ration_Trockensteher,  bg="gray85")
            
        if x==3 and table1[x].get()!=1:
            continue
            
        if x==4 and table1[x].get()==1:
            Ration_Rinder.grid_rowconfigure(0, weight=1)
            Ration_Rinder.columnconfigure(0, weight=1)
            frame_main = Frame(Ration_Rinder,  bg="gray85")
            
        if x==4 and table1[x].get()!=1:
            continue
            
        if x==5 and table1[x].get()==1:
            Ration_Bullen.grid_rowconfigure(0, weight=1)
            Ration_Bullen.columnconfigure(0, weight=1)
            frame_main = Frame(Ration_Bullen,  bg="gray85")
            
        if x==5 and table1[x].get()!=1:
            continue

        frame_main.grid(sticky='news')
        frame_canvas = Frame(frame_main)
        frame_canvas.grid(row=0, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        canvas = Canvas(frame_canvas,width=800, height=400, bg="gray85")
        canvas.grid(row=1, column=0, sticky="news")
        
        hsbar = Scrollbar(frame_canvas, orient='horizontal', command=canvas.xview)
        hsbar.grid(row=2, column=0, sticky='ew')
        canvas.configure(xscrollcommand=hsbar.set)
        
        vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=1, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)
        
        tkFenster = Frame(canvas, bg="gray85")
        canvas.create_window((0, 0), window=tkFenster, anchor='nw')
    
        header = Label(master=tkFenster, text='Frischmasse:\n (realer Wert!)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='TS (kg)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='% TS', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='MJ NEL', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='MJ NEL/kg TS', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=0, padx='1', pady='1', sticky='ew')
        
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
        
        header = Label(master=tkFenster, text=24, fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=0, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=0, fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=0, fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=2, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=0, fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=3, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=0, fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=4, column=2, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text='NDF (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='GNDF (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='NFC', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=3, padx='1', pady='1', sticky='ew') 
        header = Label(master=tkFenster, text='RP (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=3, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Stärke', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=3, padx='1', pady='1', sticky='ew')   
        
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
        
        header = Label(master=tkFenster, text="30.0", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=0, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="21-24", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=1, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=40, fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=2, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="17-17,5", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=3, column=5, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="24-28", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=4, column=5, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text='Asche (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=6, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Ca (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=6, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='P', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=6, padx='1', pady='1', sticky='ew') 
        header = Label(master=tkFenster, text='Mg (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=6, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='K (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=6, padx='1', pady='1', sticky='ew')   
        
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
        
        header = Label(master=tkFenster, text=" ", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=0, column=8, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="0,7", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=1, column=8, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="0,45", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=2, column=8, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="0,35", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=3, column=8, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=">1", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=4, column=8, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text='Na (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=9, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='S (%)', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=9, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='K/Mg', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=9, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text=round(Na,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=0, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(S,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=1, column=10, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(KMg,2), fg='black', bg='white',width = 12, height = 2,)
        header.grid(row=2, column=10, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text=24, fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=0, column=11, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=0, fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=1, column=11, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=0, fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=2, column=11, padx='1', pady='1', sticky='ew')
        
        #header = Label(master=tkFenster, text='Annahmen', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        #header.grid(row=0, column=12-14, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Futterreste', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=12, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Milchertrag', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=12, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Milchpreis', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=12, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Faktor', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=12, padx='1', pady='1', sticky='ew')
        
        #Kosten = Entry(master=tkFenster, fg='black', bg='white',width = 12)
        #Kosten.grid(row=0, column=13, padx='1', pady='1', sticky='ew')
        Futterresteentry = Entry(master=tkFenster, fg='black', bg='white',width = 12)
        Futterresteentry.grid(row=1, column=13, padx='1', pady='1', sticky='ew')
        Futterresteentry.insert(0,Futterreste)
        Milchertragentry = Entry(master=tkFenster, fg='black', bg='white',width = 12)
        Milchertragentry.grid(row=2, column=13, padx='1', pady='1', sticky='ew')
        Milchertragentry.insert(0,Milchertrag)
        Milchpreisentry = Entry(master=tkFenster, fg='black', bg='white',width = 12)
        Milchpreisentry.grid(row=3, column=13, padx='1', pady='1', sticky='ew')
        Milchpreisentry.insert(0,Milchpreis)
        Faktorentry = Entry(master=tkFenster, fg='black', bg='white',width = 12)
        Faktorentry.grid(row=4, column=13, padx='1', pady='1', sticky='ew')
        Faktorentry.insert(0,Faktor)
        
        #header = Label(master=tkFenster, text="€/Kuh/Tag", fg='black', bg='yellow',width = 12, height = 2,)
        #header.grid(row=0, column=14, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="%", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=1, column=14, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="kg Milch/\nKuh/Tag", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=2, column=14, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="ct/kg Milch", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=3, column=14, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=" ", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=4, column=14, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text='Kosten', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=0, column=15, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Kosten +\n Futterreste', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=15, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='IOFC', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=15, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text='Umsatz', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=15, padx='1', pady='1', sticky='ew')
        #header = Label(master=tkFenster, text='Faktor', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        #header.grid(row=4, column=15, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text=round(Kosten,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=1, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(Kostenplus,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=2, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(IOFC,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=3, column=16, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text=round(Umsatz,2), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
        header.grid(row=4, column=16, padx='1', pady='1', sticky='ew')
        
        header = Label(master=tkFenster, text="€/Kuh/Tag", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=0, column=17, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="€/Kuh/Tag", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=1, column=17, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="€/Kuh/Tag", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=2, column=17, padx='1', pady='1', sticky='ew')
        header = Label(master=tkFenster, text="€/Kuh/Tag", fg='black', bg='yellow',width = 12, height = 2,)
        header.grid(row=3, column=17, padx='1', pady='1', sticky='ew')
        #header = Label(master=tkFenster, text=" ", fg='black', bg='yellow',width = 12, height = 2,)
        #header.grid(row=4, column=14, padx='1', pady='1', sticky='ew')
        
        #s = ttk.Separator(header, orient=HORIZONTAL)
        number_rows=ration_ziel.shape 
        
        
        entryFM=[0] * number_rows[0]
        entryRf=[0] * number_rows[0]
        FM=[0] * number_rows[0]
        c=0
        for col in ration_ziel.columns: 
            Kasten = Label(master=tkFenster, bg='white', text=col)
            Kasten.grid(row=5, column=c)
            c=c+1
        
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):        
                if c==0:
                    entryRf[r] = Entry(master=tkFenster, bg='white')
                    entryRf[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryRf[r].insert(0,ration_ziel.iloc[r,c])
                elif c==5:
                    entryFM[r] = Entry(master=tkFenster, bg='white')
                    entryFM[r].grid(row=r+6, column=c, padx='5', pady='5', sticky='ew')
                    entryFM[r].insert(0,ration_ziel.iloc[r,c])
                elif c>4:
                    Kasten = Label(master=tkFenster, bg='white', text=round(ration_ziel.iloc[r,c],2))
                    Kasten.grid(row=r+6, column=c)
                else:
                    Kasten = Label(master=tkFenster, bg='white', text=ration_ziel.iloc[r,c])
                    Kasten.grid(row=r+6, column=c)
                
        buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='berechnen', command=buttonBerechnen)
        buttonBerechnen.grid(row=number_rows[0]+7, column=0, padx='5', pady='5', sticky='ew')
        buttonWeiter = Button(master=tkFenster, bg='#FBD975', text='weiter', command=buttonWeiter)
        buttonWeiter.grid(row=number_rows[0]+7, column=9, padx='5', pady='5', sticky='ew')
          
    for x in range(len(table1)):
        if x==0 and table1[x].get()==1:
            header = Label(master=Mischung, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl = Entry(master=Mischung, bg='white')
            EntryAnzahl.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar = Entry(master=Mischung, bg='white')
            EntryVar.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
            
            header = Label(master=Mischung, text='Komponeten:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text='Bezeichnung:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text='Frischmasse pro Kuh:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text=Anzahl-Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung, text=Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text=Anzahl +Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=5, padx='1', pady='1', sticky='ew')
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung, bg='white', text=ration_ziel.iloc[r,1])
                Kasten.grid(row=r+4, column=0)
                Kasten = Label(master=Mischung, bg='white', text=ration_ziel.iloc[r,2])
                Kasten.grid(row=r+4, column=1)
                Kasten = Label(master=Mischung, bg='white', text=ration_ziel.iloc[r,4])
                Kasten.grid(row=r+4, column=2) 
                Kasten = Label(master=Mischung, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl-Varianz))
                Kasten.grid(row=r+4, column=3)
                Kasten = Label(master=Mischung, bg='white', text=ration_ziel.iloc[r,4]*Anzahl)
                Kasten.grid(row=r+4, column=4)
                Kasten = Label(master=Mischung, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl+Varianz))
                Kasten.grid(row=r+4, column=5)
                
            header = Label(master=Mischung, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text=Frischmasse*(Anzahl-Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text=Frischmasse*Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung, text=Frischmasse*(Anzahl+Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung, bg='#FBD975', text='aktualisieren', command=buttonAktualisierenMischung)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')

        
        if x==1 and table1[x].get()==1:
            header = Label(master=Mischung_Frischmelker, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl = Entry(master=Mischung_Frischmelker, bg='white')
            EntryAnzahl.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar = Entry(master=Mischung_Frischmelker, bg='white')
            EntryVar.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
            
            header = Label(master=Mischung_Frischmelker, text='Komponeten:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text='Bezeichnung:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text='Frischmasse pro Kuh:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text=Anzahl-Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung_Frischmelker, text=Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text=Anzahl +Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=5, padx='1', pady='1', sticky='ew')
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=ration_ziel.iloc[r,1])
                Kasten.grid(row=r+4, column=0)
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=ration_ziel.iloc[r,2])
                Kasten.grid(row=r+4, column=1)
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=ration_ziel.iloc[r,4])
                Kasten.grid(row=r+4, column=2) 
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl-Varianz))
                Kasten.grid(row=r+4, column=3)
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=ration_ziel.iloc[r,4]*Anzahl)
                Kasten.grid(row=r+4, column=4)
                Kasten = Label(master=Mischung_Frischmelker, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl+Varianz))
                Kasten.grid(row=r+4, column=5)
                
            header = Label(master=Mischung_Frischmelker, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text=Frischmasse*(Anzahl-Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text=Frischmasse*Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Frischmelker, text=Frischmasse*(Anzahl+Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung_Frischmelker, bg='#FBD975', text='aktualisieren', command=buttonAktualisierenMischung)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
            
        if x==2 and table1[x].get()==1:
            header = Label(master=Mischung_Altmelker, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl = Entry(master=Mischung_Altmelker, bg='white')
            EntryAnzahl.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar = Entry(master=Mischung_Altmelker, bg='white')
            EntryVar.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
            
            header = Label(master=Mischung_Altmelker, text='Komponeten:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text='Bezeichnung:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text='Frischmasse pro Kuh:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text=Anzahl-Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung_Altmelker, text=Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text=Anzahl +Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=5, padx='1', pady='1', sticky='ew')
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=ration_ziel.iloc[r,1])
                Kasten.grid(row=r+4, column=0)
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=ration_ziel.iloc[r,2])
                Kasten.grid(row=r+4, column=1)
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=ration_ziel.iloc[r,4])
                Kasten.grid(row=r+4, column=2) 
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl-Varianz))
                Kasten.grid(row=r+4, column=3)
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=ration_ziel.iloc[r,4]*Anzahl)
                Kasten.grid(row=r+4, column=4)
                Kasten = Label(master=Mischung_Altmelker, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl+Varianz))
                Kasten.grid(row=r+4, column=5)
                
            header = Label(master=Mischung_Altmelker, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text=Frischmasse*(Anzahl-Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text=Frischmasse*Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Altmelker, text=Frischmasse*(Anzahl+Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung_Altmelker, bg='#FBD975', text='aktualisieren', command=buttonAktualisierenMischung)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
            
        if x==3 and table1[x].get()==1:
            header = Label(master=Mischung_Trockensteher, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl = Entry(master=Mischung_Trockensteher, bg='white')
            EntryAnzahl.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar = Entry(master=Mischung_Trockensteher, bg='white')
            EntryVar.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
            
            header = Label(master=Mischung_Trockensteher, text='Komponeten:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text='Bezeichnung:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text='Frischmasse pro Kuh:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text=Anzahl-Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung_Trockensteher, text=Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text=Anzahl +Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=5, padx='1', pady='1', sticky='ew')
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=ration_ziel.iloc[r,1])
                Kasten.grid(row=r+4, column=0)
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=ration_ziel.iloc[r,2])
                Kasten.grid(row=r+4, column=1)
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=ration_ziel.iloc[r,4])
                Kasten.grid(row=r+4, column=2) 
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl-Varianz))
                Kasten.grid(row=r+4, column=3)
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=ration_ziel.iloc[r,4]*Anzahl)
                Kasten.grid(row=r+4, column=4)
                Kasten = Label(master=Mischung_Trockensteher, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl+Varianz))
                Kasten.grid(row=r+4, column=5)
                
            header = Label(master=Mischung_Trockensteher, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text=Frischmasse*(Anzahl-Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text=Frischmasse*Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Trockensteher, text=Frischmasse*(Anzahl+Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung_Trockensteher, bg='#FBD975', text='aktualisieren', command=buttonAktualisierenMischung)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
            
        if x==4 and table1[x].get()==1:
            header = Label(master=Mischung_Rinder, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl = Entry(master=Mischung_Rinder, bg='white')
            EntryAnzahl.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar = Entry(master=Mischung_Rinder, bg='white')
            EntryVar.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
            
            header = Label(master=Mischung_Rinder, text='Komponeten:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text='Bezeichnung:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text='Frischmasse pro Kuh:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text=Anzahl-Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung_Rinder, text=Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text=Anzahl +Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=5, padx='1', pady='1', sticky='ew')
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung_Rinder, bg='white', text=ration_ziel.iloc[r,1])
                Kasten.grid(row=r+4, column=0)
                Kasten = Label(master=Mischung_Rinder, bg='white', text=ration_ziel.iloc[r,2])
                Kasten.grid(row=r+4, column=1)
                Kasten = Label(master=Mischung_Rinder, bg='white', text=ration_ziel.iloc[r,4])
                Kasten.grid(row=r+4, column=2) 
                Kasten = Label(master=Mischung_Rinder, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl-Varianz))
                Kasten.grid(row=r+4, column=3)
                Kasten = Label(master=Mischung_Rinder, bg='white', text=ration_ziel.iloc[r,4]*Anzahl)
                Kasten.grid(row=r+4, column=4)
                Kasten = Label(master=Mischung_Rinder, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl+Varianz))
                Kasten.grid(row=r+4, column=5)
                
            header = Label(master=Mischung_Rinder, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text=Frischmasse*(Anzahl-Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text=Frischmasse*Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Rinder, text=Frischmasse*(Anzahl+Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung_Rinder, bg='#FBD975', text='aktualisieren', command=buttonAktualisierenMischung)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
            
        if x==5 and table1[x].get()==1:
            header = Label(master=Mischung_Bullen, text='Mischtabelle', fg='black', bg='white',width = 12, height = 2,font="Arial 14 bold")
            header.grid(row=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text='Anzahl Kühe:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=1, padx='1', pady='1', sticky='ew')
            EntryAnzahl = Entry(master=Mischung_Bullen, bg='white')
            EntryAnzahl.grid(row=1, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text='Varianz:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=1, column=3, padx='1', pady='1', sticky='ew')
            EntryVar = Entry(master=Mischung_Bullen, bg='white')
            EntryVar.grid(row=1, column=4, padx='1', pady='1', sticky='ew')
            
            header = Label(master=Mischung_Bullen, text='Komponeten:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text='Bezeichnung:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=1, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text='Frischmasse pro Kuh:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=2, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text=Anzahl-Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=3, padx='1', pady='1', sticky='ew') 
            header = Label(master=Mischung_Bullen, text=Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text=Anzahl +Varianz, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=3, column=5, padx='1', pady='1', sticky='ew')
            
            for r in range(number_rows[0]):
                Kasten = Label(master=Mischung_Bullen, bg='white', text=ration_ziel.iloc[r,1])
                Kasten.grid(row=r+4, column=0)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=ration_ziel.iloc[r,2])
                Kasten.grid(row=r+4, column=1)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=ration_ziel.iloc[r,4])
                Kasten.grid(row=r+4, column=2) 
                Kasten = Label(master=Mischung_Bullen, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl-Varianz))
                Kasten.grid(row=r+4, column=3)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=ration_ziel.iloc[r,4]*Anzahl)
                Kasten.grid(row=r+4, column=4)
                Kasten = Label(master=Mischung_Bullen, bg='white', text=ration_ziel.iloc[r,4]*(Anzahl+Varianz))
                Kasten.grid(row=r+4, column=5)
                
            header = Label(master=Mischung_Bullen, text='Gesamt:', fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=0, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text=Frischmasse*(Anzahl-Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=3, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text=Frischmasse*Anzahl, fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=4, padx='1', pady='1', sticky='ew')
            header = Label(master=Mischung_Bullen, text=Frischmasse*(Anzahl+Varianz), fg='black', bg='white',width = 12, height = 2,font="Arial 10 bold")
            header.grid(row=number_rows[0]+5, column=5, padx='1', pady='1', sticky='ew')
            
            buttonaktualisieren = Button(master=Mischung_Bullen, bg='#FBD975', text='aktualisieren', command=buttonAktualisierenMischung)
            buttonaktualisieren.grid(row=number_rows[0]+6, column=0, padx='1', pady='1', sticky='ew')
            
        else:
            continue
            
            
#    for x in range(number_rows[0]):
#        FM[x]=float(FM[x])
#    ration['kg Frischmasse']=ration_ziel['kg Frischmasse']=FM
#    #    ration_ziel=ration_ziel.sort_values(by=['kg Frischmasse'], ascending=False)
#    #    ration=ration.sort_values(by=['kg Frischmasse'], ascending=False)
#    ration_ziel['TS']=ration_ziel['kg Frischmasse'].mul(ration['TS in %'])/100
#    ration_ziel['Kosten']= ration_ziel['kg Frischmasse'].mul(ration['Kosten ( € /dt )'])/100
#    TS=ration_ziel["TS"].sum(axis = 0, skipna = True)
#    ration_ziel['% der Ration TS']= ration_ziel['TS']/TS 
#    ration_ziel['MJ NEL']=ration_ziel['TS'].mul(ration['MJ NEL'])
#    ration_ziel['NDF']=ration_ziel['TS'].mul(ration['NDF']) 
#    ration_ziel['GNDF']=ration_ziel['TS'].mul(ration['Grundfutter NDF'])
#    ration_ziel['NFC']=ration_ziel['TS'].mul(ration['NFC'])
#    ration_ziel['Staerke']=ration_ziel['TS'].mul(ration['Staerke'])
#    ration_ziel['NDF']=ration_ziel['TS'].mul(ration['NDF'])
#    ration_ziel['Rohprotein']=ration_ziel['TS'].mul(ration['Rohprotein'])
#    ration_ziel['loesl. Protein']=ration_ziel['TS'].mul(ration['loesl. Protein'])
#    ration_ziel['Asche']=ration_ziel['TS'].mul(ration['Asche'])
#    ration_ziel['Ca']=ration_ziel['TS'].mul(ration['Kalzium'])
#    ration_ziel['P']=ration_ziel['TS'].mul(ration['Phosphor'])
#    ration_ziel['Mg']=ration_ziel['TS'].mul(ration['Magnesium'])
#    ration_ziel['K']=ration_ziel['TS'].mul(ration['Kalium'])
#    ration_ziel['Na']=ration_ziel['TS'].mul(ration['Natrium'])
#    ration_ziel['S']=ration_ziel['TS'].mul(ration['Schwefel'])
#    ration_ziel['Kationen']=ration_ziel['TS'].mul(ration['Kationen'])
#    ration_ziel['Anionen']=ration_ziel['TS'].mul(ration['Anionen'])

    parent.mainloop()
    
    if status=='mineral' or status=='feucht' or status=='trocken' :        
        os.chdir('/home/thomas/.config/spyder-py3/Projekt1/Komponenten/')
        if status=='mineral':
            filename='Mineralfutter.csv'
        if status=='feucht':
            filename='feuchte Komponenten.csv'    
        if status=='trocken':
            filename='trockene Komponenten.csv'    
        Komponenten = pd.read_csv(filename,encoding='latin-1')
        
        KomponentenFenster=pd.concat([Komponenten["Maske"], Komponenten["Kennung"], Komponenten["Komponente"],Komponenten["Bezeichnung"]], axis=1, ignore_index=False)
        root = Tk()
        if status=='mineral':
            root.title("Auswahl Mineralfutter")
        if status=='feucht':
            root.title("Auswahl feuchte Komponenten")    
        if status=='trocken':
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
        canvas = Canvas(frame_header,width=600, height=20, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
        
        header = Label(master=frame_main, text='Wähle die Analyse der gewünschten Komponente aus', fg='black', bg='white', font=('Arial'),width = 12, height = 2,)
        header.grid(row=0, column=0, sticky="news")
    
        frame_canvas = Frame(frame_main)
        frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        
        # Add a canvas in that frame
        canvas = Canvas(frame_canvas,width=600, height=800, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
        
        # Link a scrollbar to the canvas
        vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)
        
    #    hsbar = Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
    #    hsbar.grid(row=1, column=0, sticky="EW")
    #    canvas.configure(xscrollcommand=hsbar.set)
        
        # Create a frame to contain the labels
        frame_labels = Frame(canvas, bg="gray85")
        canvas.create_window((0, 0), window=frame_labels, anchor='nw')
        header = Label(master=frame_labels, text='ausgewählt', fg='black', bg='white', font=('Arial'),width = 12, height = 2,)
        header.grid(row=0, column=0, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Kennung', fg='black', bg='white', font=('Arial'),width = 12, height = 2,)
        header.grid(row=0, column=1, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Komponente', fg='black', bg='white', font=('Arial'),width = 12, height = 2,)
        header.grid(row=0, column=2, padx='1', pady='1', sticky='ew')
        header = Label(master=frame_labels, text='Bezeichnung', fg='black', bg='white', font=('Arial'),width = 12, height = 2,)
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
                    checkbutton[r] = Checkbutton(master=frame_labels, anchor='w',offvalue=0, onvalue=1, variable=table[r])
                    checkbutton[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                else:
                    Kasten[r][c] = Label(master=frame_labels, bg='white', text=KomponentenFenster.iloc[r,c])
                    Kasten[r][c].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
        
        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        frame_labels.update_idletasks()
        
        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
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
        canvas = Canvas(frame_button,width=550, height=20, bg="gray85")
        canvas.grid(row=0, column=0, sticky="news")
        if status=='mineral':
            Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F', command=Buttonauswahlmineral)
        if status=='feucht':
            Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F', command=Buttonauswahlfeucht)    
        if status=='trocken':
            Buttonauswahlanalysen = Button(master=root, text='weiter', bg='#D5E88F', command=Buttonauswahltrocken) 
                                           
        Buttonauswahlanalysen.grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
    #    ButtonweitereBetriebe = Button(master=tkFenster, text='weitere Betriebe', bg='#D5E88F', command=ButtonweitereBetriebe)
    #    ButtonweitereBetriebe.grid(row=r+2, column=0, padx='5', pady='5', sticky='ew')
    
        root.mainloop()     
                
        for r in range(number_rows[0]):
            if table[r].get()==1:
                ration=ration.append(Komponenten.iloc[r])    
    
        rationfenster=pd.concat([ration["Kennung"], ration["Komponente"],ration["Bezeichnung"],ration['Kosten ( € /dt )'],ration['TS in %']], axis=1, ignore_index=False)
        
        # Kosten und TS eingeben
        
        number_rows=rationfenster.shape 
        
        entryKosten=[0] * number_rows[0]
        entryTS=[0] * number_rows[0]
        
        tkFenster = Tk()
        tkFenster.title("Kosten und TS")
#        header = Label(master=tkFenster, text='Gib den Preis ein und aktualisiere gegebenenfalls die TS-Werte', fg='black', bg='white', font=('Arial'),width = 12, height = 2,)
#        header.grid(row=0, sticky="news")
        c=0
        for col in rationfenster.columns: 
            Kasten = Label(master=tkFenster, bg='white', text=col)
            Kasten.grid(row=1, column=c)
            c=c+1
        
        for r in range(number_rows[0]):
            for c in range(number_rows[1]):
                if c<3:
                    Kasten = Label(master=tkFenster, bg='white', text=rationfenster.iloc[r,c])
                    Kasten.grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                if c==3:
                   entryKosten[r] = Entry(master=tkFenster, bg='white')
                   entryKosten[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                    
                if c==4:
                    entryTS[r] = Entry(master=tkFenster, bg='white')
                    entryTS[r].grid(row=r+2, column=c, padx='5', pady='5', sticky='ew')
                    entryTS[r].insert(0,rationfenster.iloc[r,c])
        asd=number_rows[0]
        buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='weiter', command=buttonKosten)
        buttonBerechnen.grid(row=r+3, column=c, padx='5', pady='5', sticky='ew')
        
        tkFenster.mainloop()
        
        
        
        for x in range(number_rows[0]):
            if Kosten[x]=='':
                Kosten[x]=0
            else:
                Kosten[x]=float(Kosten[x])
          
            
            if TS[x]!='':
                ration.iloc[x,7]=float(TS[x])
            else:
                ration.iloc[x,7]=rationfenster.iloc[x,4]
        
        ration['Kosten ( € /dt )']=Kosten