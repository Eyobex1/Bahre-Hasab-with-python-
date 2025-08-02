"""Author Name: Eyob Tekle
   Department: IT engineering
   Id Number: MIT/UR190707/16
   Section: Section 4
   Date: 2017/10/10
                       submited to: Dr. Tuemay"""
   
from tkinter import *
#from PIL import ImageTk, Image
import time
def bahre_hasab():
    main_screen.destroy()
    screen = Tk()
    screen.geometry("700x1700")
    #img = Image.open("pexels-pandaa-20388580.jpg")
#    img=img.resize((720, 1700))
#    bg_img = ImageTk.PhotoImage(img)
#    label = Label(screen, image=bg_img)
#    global x
#    x= label.pack()
    screen.config(bg="white")
    bealat = ["1.ዮሃንስ ==> ", "2.ዓቢይ ፆም ==> ", "3.ደብረ ዘይት ==> ", "4.ሆሳዕና ==> ", "5.ስቅለት ==> ", "6.ትንሳኤ ==> ", "7.ዕርገት ==> ", "8.ጰራቅሊጦስ ==> ", "9.ጾመ ሐዋርያት ==> ","10.ጾመ ድኅነት ==> ",  "11.ጾመ ነነዌ ==> ", "12.ዘመኑ ==> "]
    magist = [0, 14, 41, 62, 67, 69, 108, 118, 119, 121, 0, 0]
    def submit():
        global year
        year = int(entry.get())
        screen2 = 0
        if year > 0:
            screen2=Tk()
            screen2.title("Eyob_bahre_hasab")
            #Calculations
            #1.Amete Alem
            AmeteAlem = 5500 + year
            #2.Century
            century = AmeteAlem%4
            #3.metenerabiet
            metenerabiet = int(AmeteAlem/4)
            #4.eletekemer(bahti)
            eletekemer = (AmeteAlem+metenerabiet)%7
            #5.medeb
            medeb = AmeteAlem%19
            #6.wenber
            wenber = medeb-1
            #7.Abektie
            abektie = (wenber*11)%30
            #8.metkie
            metkie = int((wenber*19)%30)
            day = ["ሰኑይ", "ሰሉስ", "ሮብዕ", "ሓሙስ", "ዓርቢ", "ቀዳም", "ሰንበት"]
               
            month =["መስከረም", "ጥቅምቲ", "ሕዳር", "ትሕሳስ", "ጥሪ", "የካቲት", "መጋቢት", "ሚያዝያ", "ጉንበት", "ሰነ", "ሓምለ", "ነሓሰ"]                
                        
            def century():
                x = str((5500+year)%4)
                if x == "0":
                    return "ዘመነ ዮሃንስ"
                elif x == "1":
                    return "ዘመነ ማቲዎስ"
                elif x== "2":
                    return "ዘመነ ማርቖስ"
                elif x == "3":
                    return "ዘመነ ሉቃስ"
            i = 1
            x = 0
            if eletekemer == 0:
                bahti = day[0]
                tinteon = 7-1
                j = 0
                if metkie >=15:        
                    while i <=metkie:            
                        x = j%7
                        j = j+1
                        i = i+1
                else:
                    while i <=metkie+30:            
                        x = j%7
                        j = j+1
                        i = i+1        
                                 
            elif eletekemer == 1:
                bahti = day[1]
                tinteon=1-1
                j = 1
                if metkie >=15:        
                    while i <=metkie:            
                        x = j%7
                        j = j+1
                        i = i+1
                else:
                    while i <=metkie+30:            
                        x = j%7
                        j = j+1
                        i = i+1        
                                  
            elif eletekemer == 2:
                bahti = day[2]
                tinteon=2-1
                j = 2
                if metkie >=15:        
                    while i <=metkie:            
                        x = j%7
                        j = j+1
                        i = i+1
                else:
                    while i <=metkie+30:            
                        x = j%7
                        j = j+1
                        i = i+1        
                
            elif eletekemer == 3:
                bahti = day[3]
                tinteon=3-1
                j = 3
                if metkie >=15:        
                    while i <=metkie:            
                        x = j%7
                        j = j+1
                        i = i+1
                else:
                    while i <=metkie+30:            
                        x = j%7
                        j = j+1
                        i = i+1        
                                            
            elif eletekemer == 4:
                bahti = day[4]
                tinteon=4-1
                j = 4
                if metkie >=15:        
                    while i <=metkie:            
                        x = j%7
                        j = j+1
                        i = i+1
                else:
                    while i <=metkie+30:            
                        x = j%7
                        j = j+1
                        i = i+1        
                                          
            elif eletekemer == 5:
                bahti = day[5]
                tinteon=5-1
                j = 5
                if metkie >=15:        
                    while i <=metkie:            
                        x = j%7
                        j = j+1
                        i = i+1
                else:
                    while i <=metkie+30:            
                        x = j%7
                        j = j+1
                        i = i+1        
                                 
            elif eletekemer == 6:
                bahti = day[6]
                tinteon=6-1
                j = 6
                if metkie >=15:                
                    while i <=metkie:            
                        x = j%7
                        j = j+1
                        i = i+1        
                else:
                    while i <=metkie+30:            
                        x = j%7
                        j = j+1
                        i = i+1        
            #Day        
            day = day[x]       
            #tewsak
            tewsak = 0
            if day == "ሰኑይ":
                tewsak = 6
            elif day == "ሰሉስ":
                tewsak = 5
            elif day == "ሮብዕ":
                tewsak = 4
            elif day == "ሓሙስ":
                tewsak = 3
            elif day == "ዓርቢ":
                tewsak = 2
            elif day == "ቀዳም":
                tewsak = 8
            elif day == "ሰንበት":
                tewsak = 7
                  
            #9.mebeja hamer      
            mebejahamer = metkie + tewsak
            if mebejahamer==30:
                mebejahamer = 30
            elif mebejahamer >30:
                mebejahamer = mebejahamer%30
            x = 0
            y = 0
            
            tewsakebealat = [0, 14, 11, 2, 7, 9, 18, 28, 29, 1, 0, 0]
            for i in range(0, len(bealat)):
                #Date 
                date = mebejahamer + tewsakebealat[x]
                if date>30:
                    date= date-30
                #nenewe
                nenewei = mebejahamer+0
                month =["መስከረም", "ጥቅምቲ", "ሕዳር", "ትሕሳስ", "ጥሪ", "የካቲት", "መጋቢት", "ሚያዝያ", "ጉንበት", "ሰነ", "ሓምለ", "ነሓሰ"]  
                if metkie>=15:
                    nenewe=month[4]
                else:
                    nenewe=month[5]
                sum = nenewei + magist[x]
                
                sum = nenewei + magist[x]
                if metkie>=15 and mebejahamer<=17:
                    nenewe=month[5]
                    monthnum=6 
                if sum<=30:
                    if nenewe == month[4]:
                        month = month[4]
                        monthnum = 5
                    else:
                        month = month[4+1]
                        monthnum = 6
                elif sum>30 and sum<=60:
                    if nenewe == month[4]:
                        month = month[5]
                        monthnum = 6
                    else:
                         month = month[5+1]
                         monthnum = 7
                elif sum>60 and sum<=90:
                    if nenewe == month[4]:
                        month = month[6]
                        monthnum = 7    
                    else:
                         month = month[6+1]
                         monthnum = 8
                elif sum>90 and sum<=120:
                    if nenewe == month[4]:
                        month = month[7]
                        monthnum = 8
                    else:
                         month = month[7+1]
                         monthnum = 9
                elif sum>120 and sum<=150:
                    if nenewe ==month[4]:
                        month = month[8]
                        monthnum = 9
                    else:
                         month = month[8+1]
                         monthnum = 10
                elif sum>150 and sum<=180:
                    if nenewe == month[4]:
                        month = month[9]
                        monthnum = 10
                    else:
                         month[9+1]
                         monthnum = 11
                
                dayofmon = ["ሰኑይ", "ሰሉስ", "ሮብዕ", "ሓሙስ", "ዓርቢ", "ቀዳም", "ሰንበት"]
            
                datenum=int(date)         
                daymon = str((datenum + 2*(monthnum-1)+tinteon+2)%7)
                      
                if daymon =="1":
                    daymon = dayofmon[6]
                elif daymon =="2":
                    daymon = dayofmon[0]
                elif daymon =="3":
                    daymon = dayofmon[1]
                elif daymon =="4":
                    daymon = dayofmon[2]
                elif daymon =="5":
                    daymon = dayofmon[3]
                elif daymon =="6":
                    daymon = dayofmon[4]        
                elif daymon =="0":
                    daymon = dayofmon[5]   
                if y == 0:
                    date=1
                    month="መስከረም"
                    daymon= bahti
                if y == 11:
                    month = ""
                    date = century()
                    daymon = ""
                buttons = Button(screen2,
                                #font=("bold", 10),
                                fg = "blue",
                                bg = "white",
                                padx = 50,
                                width = 28,
                                height= 2,
                                #state = DISABLED,
                                borderwidth = 10,
                                text = bealat[y]+str(month)+" "+ str(date)+" "+ daymon)
                buttons.pack()
                i += 1
                x = x+1
                y +=1
        else:
            entry.insert(0, "Invalid")
            entry.delete(7, END)      
                    
    entry = Entry(screen,
                        font = ("Arial", 20),
                        width = 10,
                        fg = "green",
                        placeholder="Enter a year",
                        bg = "white",
                        borderwidth = 5)
    ##entry.insert(0, "2024")
    entry.place(x=0, y=1)
    
    submit_button = Button(screen,
                        text = "submit",
                        padx = 58,
                        width = 5,
                        height= 2,
                        borderwidth = 5,
                        fg = "white",
                        bg = "red",
                        activebackground = "orangered",
                        command = submit)
    submit_button.place(x=490, y=0) 
    screen.mainloop()
#bahre_hasab()

def specific_day():
    main_screen.destroy()
    day_screen = Tk()
    day_screen.geometry("700x1700")
    day_screen.title("Eyob_Specific_Day")
    daymon = 0
    def printday():    
        year = int(entered_year.get())
        datenum = int(entered_Date.get())
        monthnum = int(entered_month.get())
        if year>0 and datenum>0 and datenum<=30 and monthnum>0 and monthnum <=12:
            #1.Amete Alem
            AmeteAlem = 5500 + year
            #3.metenerabiet
            metenerabiet = int(AmeteAlem/4)
            #4.eletekemer(bahti)
            eletekemer = (AmeteAlem+metenerabiet)%7
            #tinteon
            tinteon  = eletekemer-1
            if tinteon == -1:
                tinteon = 6
            global daymon
            daymon = str((datenum + 2*(monthnum-1)+tinteon+2)%7)
            dayofmon = ["monday", "tuesday", "wendsday", "thursday", "friday","saturday", "sunday"]
            if daymon =="1":
                daymon = dayofmon[6]
            elif daymon =="2":
                daymon = dayofmon[0]
            elif daymon =="3":
                daymon = dayofmon[1]
            elif daymon =="4":
                daymon = dayofmon[2]
            elif daymon =="5":
                daymon = dayofmon[3]
            elif daymon =="6":
                daymon = dayofmon[4]        
            elif daymon =="0":
                daymon = dayofmon[5]  
            Day_button= Button(day_screen,
                        text = daymon,
                        padx = 50,
                        width = 20,
                        height= 2,
                        borderwidth = 10,
                        fg = "black",
                        bg = "white",
                        state = DISABLED) 
        Day_button.place(x=240, y=320)  
            
    Day_info = Button(day_screen,
                        text = "Day",
                        padx = 50,
                        width = 7,
                        height= 2,
                        borderwidth = 10,
                        fg = "black",
                        bg = "white",
                        state = DISABLED)
    Day_info.place(x=0, y=320)   
    
    year_info = Button(day_screen,
                        text = "Enter Year",
                        padx = 50,
                        width = 7,
                        height= 2,
                        borderwidth = 10,
                        fg = "black",
                        bg = "white",
                        state = DISABLED)
    year_info.place(x=0, y=0)   
    entered_year = Entry(day_screen,
                            font = ("Arial", 20),
                            width = 10,
                            fg = "green",
                            bg = "white",
                            placeholder="2024",
                            borderwidth = 10,)
    entered_year.place(x=240, y=1)
    
    month_info = Button(day_screen,
                        text = "Enter Month",
                        padx = 50,
                        width = 7,
                        height= 2,
                        borderwidth = 10,
                        fg = "black",
                        bg = "white",
                        state = DISABLED)
    month_info.place(x=0, y=100)   
    entered_month = Entry(day_screen,
                            font = ("Arial", 20),
                            width = 10,
                            fg = "green",
                            bg = "white",
                            placeholder="12",
                            borderwidth = 10,)
    entered_month.place(x=240, y=100)
    
    Date_info = Button(day_screen,
                        text = "Enter Date",
                        padx = 50,
                        width = 7,
                        height= 2,
                        borderwidth = 10,
                        fg = "black",
                        bg = "white",
                        state = DISABLED)
    Date_info.place(x=0, y=200)   
    entered_Date = Entry(day_screen,
                            font = ("Arial", 20),
                            width = 10,
                            fg = "green",
                            bg = "white",
                            placeholder="16",
                            borderwidth = 10)
    entered_Date.place(x=240, y=200) 
    
    Exit_button = Button(day_screen,
                        text = "Exit",
                        padx = 50,
                        width = 14,
                        height= 3,
                        borderwidth = 10,
                        fg = "white",
                        bg = "red",
                        activebackground = "red",
                        command = exit)
    Exit_button.place(x=0, y=450)   
    submit_button = Button(day_screen,
                        text = "Submit",
                        padx = 50,
                        width = 14,
                        height= 3,
                        borderwidth = 10,
                        fg = "white",
                        bg = "red",
                        activebackground = "red",
                        command = printday)
    submit_button.place(x=350, y=450)   
    day_screen.mainloop()
#specific_day()
def main():
    global main_screen
    main_screen = Tk()  
    msg = Label(main_screen,
                    text = "welcom \nto \n Ethiopian \ncalander",
                    font = ("Arial", 40, "bold"),
                    fg = "yellow",
                   # bg = "black",
                    relief = RAISED,
                    bd = 0,
                    padx = 20,
                    pady = 40)                
    msg.pack()
    
    bahrehasab_button = Button(main_screen,
                        text = "1.የኣመቱን በኣላት ለማወቅ",
                        padx = 50,
                        width = 50,
                        height= 5,
                        borderwidth = 5,
                        fg = "white",
                        activeforeground = "green",
                        bg = "red",
                        activebackground = "pink",
                        command = bahre_hasab)
    bahrehasab_button.pack()   
    
    spe_day_button = Button(main_screen,
                        text = "2.የተወለዱበትን ዕለት ለማወቅ",
                        padx = 50,
                        width = 50,
                        height= 5,
                        borderwidth = 5,
                        fg = "black",
                        activeforeground = "green",
                        bg = "yellow",
                        activebackground = "pink",
                        command = specific_day
                        )
    spe_day_button.pack() 
    
    Exit_button = Button(main_screen,
                        text = "3.ለመውጣት",
                        padx = 50,
                        width = 50,
                        height= 5,
                        borderwidth = 5,
                        fg = "white",
                        activeforeground = "green",
                        bg = "green",
                        activebackground = "pink",
                        command = exit)
    Exit_button.pack()                  
    main_screen.mainloop()
main()