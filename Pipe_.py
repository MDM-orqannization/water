from tkinter.tix import *


#wait = input("Press Enter to continue.")

# ------------------------------------------------------FORM 1 ÜÇÜN PARAMETRLƏR

root = Tk()
root.geometry("1920x1080")
root.wm_attributes("-topmost", 1)                                            # Həmişə bütün pəncərələrdən üstdə olur
root.title("Расчет и конструирование водопропускных труб")


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
editmenu.add_command(label="Карта количества осадок Азербайджана")
editmenu.add_command(label="Карта количества осадок России")
menubar.add_cascade(label="Редактирование", menu=editmenu)

toolsmenu = Menu(menubar, tearoff=0)
toolsmenu.add_command(label="Исползуемый язык")
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


##----------------------------------------------------------------------------------------------------
ToolTp = Balloon()
But1 = Button(width=2, height=1, relief='raised', borderwidth=1)
ToolTp.bind_widget(But1, balloonmsg="Создат проект")
But1.place(x=1, y=0)

But2 = Button(width=2, height=1, relief='raised', borderwidth=1)
ToolTp.bind_widget(But2, balloonmsg="Сохранить проект")
But2.place(x=26, y=0)

But3 = Button(width=2, height=1, relief='raised', borderwidth=1)
ToolTp.bind_widget(But3, balloonmsg="Карта России")
But3.place(x=80, y=0)

But4 = Button(width=2, height=1, relief='raised', borderwidth=1)
ToolTp.bind_widget(But4, balloonmsg="Карта Aзербайджана")
But4.place(x=105, y=0)

But5 = Button(width=2, height=1, relief='raised', borderwidth=1)
ToolTp.bind_widget(But5, balloonmsg="Расчет пропускной способности трубы")
But5.place(x=140, y=0)




root.mainloop()
