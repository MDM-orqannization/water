from tkinter import Tk
from tkinter.tix import Menu
from tkinter import Button
from tkinter import PhotoImage
from tkinter import filedialog


from PIL import ImageTk, Image

# ------------------------------------------------------FORM 1 ÜÇÜN PARAMETRLƏR
root = Tk()
root.geometry("1920x1080")
root.wm_attributes("-topmost", 1)                                            # Həmişə bütün pəncərələrdən üstdə olur
root.title("Расчет и конструирование водопропускных труб")
root.iconname("c:\clone\icon\App.ico")

#--------------------------------------------------------- kartalari ekrandan silmek ve berpa etmek
photo = PhotoImage(file=r"c:\clone\icon\Az.gif")
Az = photo.subsample(1, 1)
photo = PhotoImage(file=r"c:\clone\icon\Rus.gif")
Rus = photo.subsample(1, 1)
def Click_Menu_Edit_Az():
    def click_button_Az():
        But7.destroy()
    But7 = Button(root, width=890, height=550, image=Az, relief='raised', borderwidth=1, command=click_button_Az)
    But7.place(x=470, y=100)
def Click_Menu_Edit_Rus():
    def click_button_Rus():
        But8.destroy()
    But8 = Button(root, width=890, height=550, image=Rus, relief='raised', borderwidth=1, command=click_button_Rus)
    But8.place(x=470, y=100)

#------------------------------------------------------- Meny Bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Создать")

filemenu.add_command(label="Oткрыть")
filemenu.add_command(label="Сохранить")
filemenu.add_command(label="Сохранить как ...")
filemenu.add_command(label="Расчет конвертировать в <Word>")
filemenu.add_command(label="Close")
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Файл", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Карта количества осадок Азербайджана", command=Click_Menu_Edit_Az)
editmenu.add_command(label="Карта количества осадок России", command=Click_Menu_Edit_Rus)
menubar.add_cascade(label="Редактирование", menu=editmenu)

toolsmenu = Menu(menubar, tearoff=0)
toolsmenu.add_command(label="Переключение языков")
toolsmenu.add_command(label="Проект Трубы на <Autocad>")
menubar.add_cascade(label="Инструменты", menu=toolsmenu)

tipmenu = Menu(menubar, tearoff=0)
tipmenu.add_command(label="Трапецадальный или трехугольный кювет")
tipmenu.add_command(label="Полуеруглый кювет")
tipmenu.add_command(label="Круглая труба")
tipmenu.add_command(label="Четырехугольная труба")
menubar.add_cascade(label="Тип сооружения", menu=tipmenu)

rascetmenu = Menu(menubar, tearoff=0)
rascetmenu.add_command(label="Расчет расхода .....")
menubar.add_cascade(label="Расчет", menu=rascetmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
#-------------------------------------------------------------------------------Button 7 ve 8
photo = PhotoImage(file = r"c:\clone\icon\Sozdat_file.png")
photoimage1 = photo.subsample(1, 1)
But1 = Button(root, width=20, height=20, image=photoimage1, relief='raised', borderwidth=1)
But1.place(x=1, y=0)

photo = PhotoImage(file=r"c:\clone\icon\Soxranit_file.png")
photoimage2 = photo.subsample(1, 1)
But2 = Button(root, width=20, height=20, image=photoimage2, relief='raised', borderwidth=1)
But2.place(x=26, y=0)

photo = PhotoImage(file=r"c:\clone\icon\Azerb_flaq.png")
photoimage3 = photo.subsample(2, 2)
But3 = Button(root, width=20, height=20, image=photoimage3, relief='raised', borderwidth=1, command=Click_Menu_Edit_Az)
But3.place(x=70, y=0)

photo = PhotoImage(file=r"c:\clone\icon\Russia_flag.png")
photoimage4 = photo.subsample(1, 1)
But4 = Button(root, width=20, height=20, image=photoimage4, relief='raised', borderwidth=1, command=Click_Menu_Edit_Rus)
But4.place(x=95, y=0)

photo = PhotoImage(file=r"c:\clone\icon\Run_rasxod.png")
photoimage5 = photo.subsample(1, 1)
But5 = Button(root, width=20, height=20, image=photoimage5, relief='raised', borderwidth=1)
But5.place(x=140, y=0)
#------------------------------------------------------------------------------------------------------------


root.mainloop()