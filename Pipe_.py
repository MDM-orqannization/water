from tkinter.tix import *



# ------------------------------------------------------FORM 1 ÜÇÜN PARAMETRLƏR
root = Tk()
root.geometry("1920x1080")
#root.resizable(0, 0)                                                         # formanın razmerini deyişmeye qadağa qoyur
root.wm_attributes("-topmost", 1)                                            # Həmişə bütün pəncərələrdən üstdə olur
root.title("Расчет и конструирование водопропускных труб")


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Создать", command=donothing)
filemenu.add_command(label="Oткрыть", command=donothing)
filemenu.add_command(label="Сохранить", command=donothing)
filemenu.add_command(label="Сохранить как ...", command=donothing)
filemenu.add_command(label="Расчет конвертировать в <Word>", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Файл", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Карта количества осадок Азербайджана", command=donothing)
editmenu.add_command(label="Карта количества осадок России", command=donothing)
menubar.add_cascade(label="Редактирование", menu=editmenu)

toolsmenu = Menu(menubar, tearoff=0)
toolsmenu.add_command(label="Исползуемый язык", command=donothing)
toolsmenu.add_command(label="Проект Трубы на <Autocad>", command=donothing)
menubar.add_cascade(label="Инструменты", menu=toolsmenu)

tipmenu = Menu(menubar, tearoff=0)
tipmenu.add_command(label="Трапецадальный или трехугольный кювет", command=donothing)
tipmenu.add_command(label="Полуеруглый кювет", command=donothing)
tipmenu.add_command(label="Круглая труба", command=donothing)
tipmenu.add_command(label="Четырехугольная труба", command=donothing)
menubar.add_cascade(label="Тип сооружения", menu=tipmenu)

rascetmenu = Menu(menubar, tearoff=0)
rascetmenu.add_command(label="Расчет расхода .....", command=donothing)
menubar.add_cascade(label="Расчет", menu=rascetmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
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
ToolTp.bind_widget(But4, balloonmsg="Карта Aяербайджана")
But4.place(x=105, y=0)

But5 = Button(width=2, height=1, relief='raised', borderwidth=1)
ToolTp.bind_widget(But5, balloonmsg="Расчет пропускной способности трубы")
But5.place(x=140, y=0)




root.mainloop()
