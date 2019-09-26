from fpdf import FPDF
 
if __name__ == '__main__':
    mischung_ziel=mischung_hochleistend
    #mischung_ziel=mischung_ziel.rename(columns={'Reihenfolge': 'Lade- \n reihenf.', 'kg Frischmasse': 'kg Frischm.','untere Lademenge': 'untere \n Ladem.','normale Lademenge': 'normale \n Ladem.','obere Lademenge': 'obere \n Ladem.'})
   
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(30, 20, 'Mischtabelle für hochleistende Kühe', ln=1)
    pdf.image('agroprax1.png', 150, 8, 50)

    pdf.set_font('Arial', 'B', 17)
    pdf.cell(15)
    pdf.cell(50, 15, 'Betrieb:')
    pdf.cell(pdf.w/5)
    pdf.cell(20, 15, 'Datum:')
    pdf.ln(10)
    pdf.cell(15)
    pdf.cell(50, 10, 'Ersteller:')
    pdf.cell(pdf.w/5)
    pdf.cell(0, 10, 'Gruppe:')
    pdf.set_font('Arial', 'B', 12)
    col_width = pdf.w
    row_height = pdf.font_size
    number_rows=mischung_ziel.shape
    
    pdf.cell(pdf.w/2)
    pdf.cell(col_width/10, row_height*3,txt='Kuhzahl', border=1)
    pdf.cell(col_width/10, row_height*3,txt=str(Anzahl_hochleistend-Varianz_hochleistend), border=1)
    pdf.cell(col_width/10, row_height*3,txt=str(Anzahl_hochleistend), border=1)
    pdf.cell(col_width/10, row_height*3,txt=str(Anzahl_hochleistend+Varianz_hochleistend), border=1)
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
    pdf.cell(col_width/10, row_height*3,txt=str(ration_hochleistend["kg Frischmasse"].sum(axis = 0, skipna = True)), border=1)
    pdf.cell(col_width/10, row_height*3,txt=str(mischung_ziel["untere Lademenge"].sum(axis = 0, skipna = True)), border=1)
    pdf.cell(col_width/10, row_height*3,txt=str(mischung_ziel["normale Lademenge"].sum(axis = 0, skipna = True)), border=1)
    pdf.cell(col_width/10, row_height*3,txt=str(mischung_ziel["obere Lademenge"].sum(axis = 0, skipna = True)), border=1)
    
        
    pdf.ln(row_height*5)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(pdf.w /6, row_height*2, 'Frischmasse(kg):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["kg Frischmasse"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.cell(pdf.w /6, row_height*2, 'GNDF (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["GNDF"].sum(axis = 0, skipna = True),2)), border=1) 
    pdf.cell(pdf.w /6, row_height*2, 'Phosphor (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["Phosphor"].sum(axis = 0, skipna = True),2)), border=1)   
    pdf.ln(row_height*2)
    pdf.cell(pdf.w /6, row_height*2, 'TS (kg):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["TS"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.cell(pdf.w /6, row_height*2, 'NFC (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["NFC"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.cell(pdf.w /6, row_height*2, 'Magnesium (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["Magnesium"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.ln(row_height*2)
    pdf.cell(pdf.w /6, row_height*2, '% TS:', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["TS"].sum(axis = 0, skipna = True)/ration_hochleistend["kg Frischmasse"].sum(axis = 0, skipna = True)*100,2)), border=1)
    pdf.cell(pdf.w /6, row_height*2, 'Rohprotein (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["Rohprotein"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.cell(pdf.w /6, row_height*2, 'Kalium (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["Kalium"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.ln(row_height*2)
    pdf.cell(pdf.w /6, row_height*2, 'MJNEL:', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["MJ NEL"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.cell(pdf.w /6, row_height*2, 'Staerke:', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["Staerke"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.cell(pdf.w /6, row_height*2, 'Natrium (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["Natrium"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.ln(row_height*2)
    pdf.cell(pdf.w /6, row_height*2, 'MJNEL/kgTS:', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["MJ NEL"].sum(axis = 0, skipna = True)/ration_hochleistend["TS"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.cell(pdf.w /6, row_height*2, 'Asche (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["Asche"].sum(axis = 0, skipna = True),2)), border=1) 
    pdf.cell(pdf.w /6, row_height*2, 'Schwefel (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["Schwefel"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.ln(row_height*2)
    pdf.cell(pdf.w /6, row_height*2, 'NDF (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["NDF"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.cell(pdf.w /6, row_height*2, 'Kalzium (%):', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["Kalzium"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.cell(pdf.w /6, row_height*2, 'K/Mg:', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(ration_hochleistend["Kalium"].sum(axis = 0, skipna = True)/ration_hochleistend["Magnesium"].sum(axis = 0, skipna = True),2)), border=1)
    pdf.ln(row_height*2)
    pdf.ln(row_height*2)

    
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
    pdf.cell(pdf.w /9, row_height*2, str(round(0,2)), border=1)
    pdf.cell(pdf.w /7, row_height*2,  "Euro/Tag/Kuh", border=1)
    pdf.ln(row_height*2)
    
    pdf.cell(pdf.w /6, row_height*2, 'Milcherstrag:', border=1)
    pdf.cell(pdf.w /9, row_height*2, str(round(Milchpreis,2)), border=1)
    pdf.cell(pdf.w /7, row_height*2,  "Euro/Tag/Kuh", border=1)
    pdf.cell(pdf.w /6, row_height*2, 'IOFC', border=1)    
    pdf.cell(pdf.w /9, row_height*2, str(round(0,2)), border=1)
    pdf.cell(pdf.w /7, row_height*2,  "Euro/Tag/Kuh", border=1)
    
    

    
    
    
    
    
    
    pdf.output("asd.pdf")