import tkinter as tk #imports
from tkinter import * #imports
from PIL import ImageTk,Image #imports
import pandas as pd

spreadsheet = pd.read_csv('C:/Users/maticl/Downloads/NapoleonicWars2.csv')

print(spreadsheet.to_string())

a = (spreadsheet['Commander F1'].apply(pd.Series).stack().drop_duplicates().tolist())
b = (spreadsheet['Commander F2'].apply(pd.Series).stack().drop_duplicates().tolist())
c = (spreadsheet['Commander F3'].apply(pd.Series).stack().drop_duplicates().tolist())
d = (spreadsheet['Commander C1'].apply(pd.Series).stack().drop_duplicates().tolist())
e = (spreadsheet['Commander C2'].apply(pd.Series).stack().drop_duplicates().tolist())
f = (spreadsheet['Commander C3'].apply(pd.Series).stack().drop_duplicates().tolist())

a1 = spreadsheet['Commander F1']
b1 = spreadsheet['Commander F2']
c1 = spreadsheet['Commander F3']
d1 = spreadsheet['Commander C1']
e1 = spreadsheet['Commander C2']
f1 = spreadsheet['Commander C3']

generalscolumnsF = a1+b1+c1
generalscolumnsC = d1+e1+f1

generalscombinedF = a+b+c
generalscombinedC = d+e+f

generalscombinedF = list(dict.fromkeys(generalscombinedF))
generalscombinedC = list(dict.fromkeys(generalscombinedC))
generalscombinedF.remove('~')
generalscombinedC.remove('~')
print(generalscombinedF)
print(generalscombinedC)

print('this is the rows every general features in:')

general_rows = []

for i in range(len(generalscombinedF)):
    result = generalscolumnsF.str.contains(generalscombinedF[i])
    print(result)
    for l in range(spreadsheet.index.stop):
        if result[l] == True:
            general_rows.append(l)
            print(general_rows)




total = 0
for l in range(spreadsheet.index.stop):
    total += (int(spreadsheet['Army Size F'].iloc[l]) + int(spreadsheet['Army Size C'].iloc[l]))

SizeAvg = total/((spreadsheet.index.stop)*2)

print('Army size average',SizeAvg)

print('Army size total',total)

total2 = 0
for d in range(spreadsheet.index.stop):
    total2 += (int(spreadsheet['Casualties F'].iloc[d]) + int(spreadsheet['Casualties C'].iloc[d]))

CasultyAvg = total2/((spreadsheet.index.stop)*2)

print('Casualty average', CasultyAvg)

print('Casualty total', total2)

SizeCasultyratio = SizeAvg/CasultyAvg

print(SizeCasultyratio)

ll = (SizeAvg)/1500

print('ll',ll)

def equation(n):
    ratio_F = (int(spreadsheet['Army Size F'].iloc[n]) / int(spreadsheet['Army Size C'].iloc[n])) * 100 + 1500
    ratio_C = (int(spreadsheet['Army Size C'].iloc[n]) / int(spreadsheet['Army Size F'].iloc[n])) * 100 + 1500

    elof = 10**(ratio_F/400)
    eloc = 10**(ratio_C/400)

    #print('ratios',ratio_F, ratio_C)

    #print('Q',elof, eloc)

    expectedresultf = (elof/(elof+eloc))
    expectedresultc = (eloc/(elof+eloc))

    #print('Ef',expectedresultf)
    #print('Ec',expectedresultc)

    if (spreadsheet['Result'].iloc[n]) == 'F':
        resultbattlef = 1
    elif (spreadsheet['Result'].iloc[n]) == 'C':
        resultbattlef = 0
    else:
        resultbattlef = 0.5

    if (spreadsheet['Result'].iloc[n]) == 'C':
        resultbattlec = 1
    elif (spreadsheet['Result'].iloc[n]) == 'F':
        resultbattlec = 0
    else:
        resultbattlec = 0.5

    Casultyf = (int(spreadsheet['Casualties F'].iloc[n]) / int(spreadsheet['Army Size F'].iloc[n]))/SizeCasultyratio
    Casultyc = (int(spreadsheet['Casualties C'].iloc[n]) / int(spreadsheet['Army Size C'].iloc[n]))/SizeCasultyratio

    #print('Casultyf',Casultyf)
    #print('Casultyc',Casultyc)

    Casultyscorevariable=1

    Casultyscoref = Casultyf/Casultyscorevariable
    Casultyscorec = Casultyc/Casultyscorevariable

    startingscoref = 0
    startingscorec = 0

    newscoref = startingscoref + 32 * (resultbattlef - expectedresultf - Casultyscoref)
    newscorec = startingscorec + 32 * (resultbattlec - expectedresultc - Casultyscorec)

    #print(newscoref)
    #print(newscorec)

    return (newscoref, newscorec)

def loop():
    totalf = 0
    totalc = 0
    for i in range(len(generalscombinedF)):
        result = generalscolumnsF.str.contains(generalscombinedF[i])
        for l in range(spreadsheet.index.stop):
            if result[l] == True:
                general_rows.append(l)
                print(i,generalscombinedF[i],l)
                for n in range(l):
                    result2 = equation(n)
                    totalf += result2[0]
                    totalc += result2[1]
    print(totalf)
    print(totalc)

    # print(Commandertotals)



app = tk.Tk() #title
app.title('Generals Code')
app.geometry('800x800') #this changes how big the screen is

my_img = ImageTk.PhotoImage(Image.open('C:/Users/maticl/Downloads/Apotheosis_Of_Napoleon_Bonaparte.jpg'))# this is the image file
mylabel = Label(image=my_img)
mylabel.grid(column=0, row=0)# this is image placement

mylabel1 = tk.Label(app, text= "Insert spreadsheet URL")#text
mylabel1.grid(column=0, row=1,)

mylabel2 = tk.Entry(app)#text
mylabel2.grid(column=0, row=2)

def show(event):#this funtion is for showing result when button is pressed
    data = mylabel2.get()
    mylabel3 = tk.Label(app, text=data)#text
    mylabel3.grid(column=0, row=4)
button = Button(text='Go', command=lambda:show('d'))
button.grid(column=0, row=3)

app.bind('<Return>', show)

def quit():
    app.destroy()
button3 = Button( text='Exit', command=quit)
button3.grid( column=0, row=8)

mylabel4 = tk.Label(app, text= "Made by Luka Matic with the help of Ben and Harry")#text
mylabel4.grid(column=0, row=5,)

def help():#this funtion is for loading a tutorial page
    tutorial = tk.Tk() #title
    tutorial.title('guide')
    tutorial.geometry('200x200') #this changes how big the screen is
    def quit():
        tutorial.destroy()
    button3 = Button(tutorial, text='Exit', command=quit)
    button3.grid( column=0, row=0)
    mylabel5 = tk.Label(tutorial, text= "Step 1: save spreadsheet in Users/maticl/Downloads")#text
    mylabel5.grid(column=0, row=1,)
button2 = Button(text='Help', command=help)
button2.grid(column=0, row=7)

button4 = Button(text='Use', command=loop)
button4.grid(column=1, row=2)

app.mainloop()
