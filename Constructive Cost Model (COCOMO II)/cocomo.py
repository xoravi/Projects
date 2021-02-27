import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

def raise_frame(frame):
    frame.tkraise()

root=tk.Tk()

window = tk.Frame(root, width=1024, height=650)
window.configure(bg="white")
page1 = tk.Frame(root, width=1024, height=650)
pagesloc = tk.Frame(root, width=1024, height=650)
pagefp = tk.Frame(root, width=1024, height=650)
pagefpcd = tk.Frame(root, width=1024, height=650)
#res = tk.Frame(root, width=1024, height=650)
window.tkraise()
for frame in (window, page1,pagesloc,pagefp,pagefpcd):
    frame.place(x=0,y=0)

def exitm():
    if messagebox.askokcancel("Warning!", "Are you sure you want to exit?"):
        root.destroy()

def knowmore():
   messagebox.showinfo("About Developer", "Developed by:\n\nRAVI SAHNI\nFaculty No.: 17 COB 085\nEnrollment No.: GJ7718\n\nas the part of project work (assignment) for course:\nSOFTWARE ENGINEERING (COC2090).")

#SLOC RESULT
def locclick():
    sloc=int(loc.get())
    sal=int(cost.get())
    eaf=1

    if cd1.current() == 0:
    	eaf=eaf*0.75
    if cd1.current() == 1:
    	eaf=eaf*0.88
    if cd1.current() == 2:
    	eaf=eaf*1.00
    if cd1.current() == 3:
    	eaf=eaf*1.15
    if cd1.current() == 4:
    	eaf=eaf*1.40

    if cd2.current() == 0:
    	eaf=eaf*0.94
    if cd2.current() == 1:
    	eaf=eaf*0.94
    if cd2.current() == 2:
    	eaf=eaf*1.00
    if cd2.current() == 3:
    	eaf=eaf*1.08
    if cd2.current() == 4:
    	eaf=eaf*1.16

    if cd3.current() == 0:
    	eaf=eaf*0.70
    if cd3.current() == 1:
    	eaf=eaf*0.85
    if cd3.current() == 2:
    	eaf=eaf*1.00
    if cd3.current() == 3:
    	eaf=eaf*1.15
    if cd3.current() == 4:
    	eaf=eaf*1.30

    if cd4.current() == 0:
    	eaf=eaf*1.00
    if cd4.current() == 1:
    	eaf=eaf*1.00
    if cd4.current() == 2:
    	eaf=eaf*1.00
    if cd4.current() == 3:
    	eaf=eaf*1.11
    if cd4.current() == 4:
    	eaf=eaf*1.30

    if cd5.current() == 0:
    	eaf=eaf*1.00
    if cd5.current() == 1:
    	eaf=eaf*1.00
    if cd5.current() == 2:
    	eaf=eaf*1.00
    if cd5.current() == 3:
    	eaf=eaf*1.06
    if cd5.current() == 4:
    	eaf=eaf*1.21

    if cd6.current() == 0:
    	eaf=eaf*0.87
    if cd6.current() == 1:
    	eaf=eaf*0.87
    if cd6.current() == 2:
    	eaf=eaf*1.00
    if cd6.current() == 3:
    	eaf=eaf*1.15
    if cd6.current() == 4:
    	eaf=eaf*1.30

    if cd7.current() == 0:
    	eaf=eaf*0.94
    if cd7.current() == 1:
    	eaf=eaf*0.94
    if cd7.current() == 2:
    	eaf=eaf*1.00
    if cd7.current() == 3:
    	eaf=eaf*1.07
    if cd7.current() == 4:
    	eaf=eaf*1.15

    if cd8.current() == 0:
    	eaf=eaf*1.46
    if cd8.current() == 1:
    	eaf=eaf*1.19
    if cd8.current() == 2:
    	eaf=eaf*1.00
    if cd8.current() == 3:
    	eaf=eaf*0.86
    if cd8.current() == 4:
    	eaf=eaf*0.71

    if cd9.current() == 0:
    	eaf=eaf*1.29
    if cd9.current() == 1:
    	eaf=eaf*1.13
    if cd9.current() == 2:
    	eaf=eaf*1.00
    if cd9.current() == 3:
    	eaf=eaf*0.91
    if cd9.current() == 4:
    	eaf=eaf*0.82

    if cd10.current() == 0:
    	eaf=eaf*1.42
    if cd10.current() == 1:
    	eaf=eaf*1.17
    if cd10.current() == 2:
    	eaf=eaf*1.00
    if cd10.current() == 3:
    	eaf=eaf*0.86
    if cd10.current() == 4:
    	eaf=eaf*0.70

    if cd11.current() == 0:
    	eaf=eaf*1.21
    if cd11.current() == 1:
    	eaf=eaf*1.10
    if cd11.current() == 2:
    	eaf=eaf*1.00
    if cd11.current() == 3:
    	eaf=eaf*0.90
    if cd11.current() == 4:
    	eaf=eaf*0.90

    if cd12.current() == 0:
    	eaf=eaf*1.14
    if cd12.current() == 1:
    	eaf=eaf*1.07
    if cd12.current() == 2:
    	eaf=eaf*1.00
    if cd12.current() == 3:
    	eaf=eaf*0.95
    if cd12.current() == 4:
    	eaf=eaf*0.95

    if cd13.current() == 0:
    	eaf=eaf*1.24
    if cd13.current() == 1:
    	eaf=eaf*1.10
    if cd13.current() == 2:
    	eaf=eaf*1.00
    if cd13.current() == 3:
    	eaf=eaf*0.91
    if cd13.current() == 4:
    	eaf=eaf*0.82

    if cd14.current() == 0:
    	eaf=eaf*1.24
    if cd14.current() == 1:
    	eaf=eaf*1.10
    if cd14.current() == 2:
    	eaf=eaf*1.00
    if cd14.current() == 3:
    	eaf=eaf*0.91
    if cd14.current() == 4:
    	eaf=eaf*0.83

    if cd15.current() == 0:
    	eaf=eaf*1.23
    if cd15.current() == 1:
    	eaf=eaf*1.08
    if cd15.current() == 2:
    	eaf=eaf*1.00
    if cd15.current() == 3:
    	eaf=eaf*1.04
    if cd15.current() == 4:
    	eaf=eaf*1.10


    if dm.current() == 0:
        effort = 2.4*((sloc/1000)**1.05)*eaf
        tdev = 2.5*(effort**0.38)
    if dm.current() == 1:
        effort = 3.0*((sloc/1000)**1.12)*eaf
        tdev = 2.5*(effort**0.35)
    if dm.current() == 2:
        effort = 3.6*((sloc/1000)**1.20)*eaf
        tdev = 2.5*(effort**0.32)
    procost=sal*tdev

    res = tk.Frame(root, width=1024, height=650)
    res.place(x=0,y=0)
    lbl2=tk.Label(res, text="Result:",font = ("Verdana 10 bold",16))
    lbl2.place(x=20, y=10)

    tk.Label(res, text="Effort = " +str(round(effort,3))+" Person-Months", font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=150)
    tk.Label(res, text="Development Time = " +str(round(tdev,3))+" Months", font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=200)
    tk.Label(res, text="Development Cost = Rs " +str(round(procost,3)), font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=250)

    btn4=tk.Button(res, text="Home",command=lambda:raise_frame(window))
    btn4.place(x=900, y=550)

    btn5=tk.Button(res, text="Back", command=lambda:raise_frame(pagesloc))
    btn5.place(x=820, y=550)

def fpclick():
	lfval=int(lf.get())
	costval=int(costfp.get())
	eaffp=1

	if fpd1.current() == 0:
		eaffp=eaffp*0.75
	if fpd1.current() == 1:
		eaffp=eaffp*0.88
	if fpd1.current() == 2:
		eaffp=eaffp*1.00
	if fpd1.current() == 3:
		eaffp=eaffp*1.15
	if fpd1.current() == 4:
		eaffp=eaffp*1.40

	if fpd2.current() == 0:
		eaffp=eaffp*0.94
	if fpd2.current() == 1:
		eaffp=eaffp*0.94
	if fpd2.current() == 2:
		eaffp=eaffp*1.00
	if fpd2.current() == 3:
		eaffp=eaffp*1.08
	if fpd2.current() == 4:
		eaffp=eaffp*1.16

	if fpd3.current() == 0:
		eaffp=eaffp*0.70
	if fpd3.current() == 1:
		eaffp=eaffp*0.85
	if fpd3.current() == 2:
		eaffp=eaffp*1.00
	if fpd3.current() == 3:
		eaffp=eaffp*1.15
	if fpd3.current() == 4:
		eaffp=eaffp*1.30

	if fpd4.current() == 0:
		eaffp=eaffp*1.00
	if fpd4.current() == 1:
		eaffp=eaffp*1.00
	if fpd4.current() == 2:
		eaffp=eaffp*1.00
	if fpd4.current() == 3:
		eaffp=eaffp*1.11
	if fpd4.current() == 4:
		eaffp=eaffp*1.30

	if fpd5.current() == 0:
		eaffp=eaffp*1.00
	if fpd5.current() == 1:
		eaffp=eaffp*1.00
	if fpd5.current() == 2:
		eaffp=eaffp*1.00
	if fpd5.current() == 3:
		eaffp=eaffp*1.06
	if fpd5.current() == 4:
		eaffp=eaffp*1.21

	if fpd6.current() == 0:
		eaffp=eaffp*0.87
	if fpd6.current() == 1:
		eaffp=eaffp*0.87
	if fpd6.current() == 2:
		eaffp=eaffp*1.00
	if fpd6.current() == 3:
		eaffp=eaffp*1.15
	if fpd6.current() == 4:
		eaffp=eaffp*1.30

	if fpd7.current() == 0:
		eaffp=eaffp*0.94
	if fpd7.current() == 1:
		eaffp=eaffp*0.94
	if fpd7.current() == 2:
		eaffp=eaffp*1.00
	if fpd7.current() == 3:
		eaffp=eaffp*1.07
	if fpd7.current() == 4:
		eaffp=eaffp*1.15

	if fpd8.current() == 0:
		eaffp=eaffp*1.46
	if fpd8.current() == 1:
		eaffp=eaffp*1.19
	if fpd8.current() == 2:
		eaffp=eaffp*1.00
	if fpd8.current() == 3:
		eaffp=eaffp*0.86
	if fpd8.current() == 4:
		eaffp=eaffp*0.71

	if fpd9.current() == 0:
		eaffp=eaffp*1.29
	if fpd9.current() == 1:
		eaffp=eaffp*1.13
	if fpd9.current() == 2:
		eaffp=eaffp*1.00
	if fpd9.current() == 3:
		eaffp=eaffp*0.91
	if fpd9.current() == 4:
		eaffp=eaffp*0.82

	if fpd10.current() == 0:
		eaffp=eaffp*1.42
	if fpd10.current() == 1:
		eaffp=eaffp*1.17
	if fpd10.current() == 2:
		eaffp=eaffp*1.00
	if fpd10.current() == 3:
		eaffp=eaffp*0.86
	if fpd10.current() == 4:
		eaffp=eaffp*0.70

	if fpd11.current() == 0:
		eaffp=eaffp*1.21
	if fpd11.current() == 1:
		eaffp=eaffp*1.10
	if fpd11.current() == 2:
		eaffp=eaffp*1.00
	if fpd11.current() == 3:
		eaffp=eaffp*0.90
	if fpd11.current() == 4:
		eaffp=eaffp*0.90

	if fpd12.current() == 0:
		eaffp=eaffp*1.14
	if fpd12.current() == 1:
		eaffp=eaffp*1.07
	if fpd12.current() == 2:
		eaffp=eaffp*1.00
	if fpd12.current() == 3:
		eaffp=eaffp*0.95
	if fpd12.current() == 4:
		eaffp=eaffp*0.95

	if fpd13.current() == 0:
		eaffp=eaffp*1.24
	if fpd13.current() == 1:
		eaffp=eaffp*1.10
	if fpd13.current() == 2:
		eaffp=eaffp*1.00
	if fpd13.current() == 3:
		eaffp=eaffp*0.91
	if fpd13.current() == 4:
		eaffp=eaffp*0.82

	if fpd14.current() == 0:
		eaffp=eaffp*1.24
	if fpd14.current() == 1:
		eaffp=eaffp*1.10
	if fpd14.current() == 2:
		eaffp=eaffp*1.00
	if fpd14.current() == 3:
		eaffp=eaffp*0.91
	if fpd14.current() == 4:
		eaffp=eaffp*0.83

	if fpd15.current() == 0:
		eaffp=eaffp*1.23
	if fpd15.current() == 1:
		eaffp=eaffp*1.08
	if fpd15.current() == 2:
		eaffp=eaffp*1.00
	if fpd15.current() == 3:
		eaffp=eaffp*1.04
	if fpd15.current() == 4:
		eaffp=eaffp*1.10

	eival=int(ei.get())
	eoval=int(eo.get())
	eqval=int(eq.get())
	ilfval=int(ilf.get())
	eifval=int(eif.get())

	if wffp.current() == 0:
		eival=eival*3
		eoval=eoval*4
		eqval=eqval*3
		ilfval=ilfval*7
		eifval=eifval*5
	if wffp.current() == 1:
		eival=eival*4
		eoval=eoval*5
		eqval=eqval*4
		ilfval=ilfval*10
		eifval=eifval*7
	if wffp.current() == 2:
		eival=eival*6
		eoval=eoval*7
		eqval=eqval*6
		ilfval=ilfval*15
		eifval=eifval*10

	ufp = (eival+eoval+eqval+ilfval+eifval)
	di=0

	if rate2.current() == 0:
		di=di+0
	if rate2.current() == 1:
		di=di+1
	if rate2.current() == 2:
		di=di+2
	if rate2.current() == 3:
		di=di+3
	if rate2.current() == 4:
		di=di+4
	if rate2.current() == 5:
		di=di+5

	if rate3.current() == 0:
		di=di+0
	if rate3.current() == 1:
		di=di+1
	if rate3.current() == 2:
		di=di+2
	if rate3.current() == 3:
		di=di+3
	if rate3.current() == 4:
		di=di+4
	if rate3.current() == 5:
		di=di+5

	if rate4.current() == 0:
		di=di+0
	if rate4.current() == 1:
		di=di+1
	if rate4.current() == 2:
		di=di+2
	if rate4.current() == 3:
		di=di+3
	if rate4.current() == 4:
		di=di+4
	if rate4.current() == 5:
		di=di+5

	if rate5.current() == 0:
		di=di+0
	if rate5.current() == 1:
		di=di+1
	if rate5.current() == 2:
		di=di+2
	if rate5.current() == 3:
		di=di+3
	if rate5.current() == 4:
		di=di+4
	if rate5.current() == 5:
		di=di+5

	if rate6.current() == 0:
		di=di+0
	if rate6.current() == 1:
		di=di+1
	if rate6.current() == 2:
		di=di+2
	if rate6.current() == 3:
		di=di+3
	if rate6.current() == 4:
		di=di+4
	if rate6.current() == 5:
		di=di+5

	if rate7.current() == 0:
		di=di+0
	if rate7.current() == 1:
		di=di+1
	if rate7.current() == 2:
		di=di+2
	if rate7.current() == 3:
		di=di+3
	if rate7.current() == 4:
		di=di+4
	if rate7.current() == 5:
		di=di+5

	if rate8.current() == 0:
		di=di+0
	if rate8.current() == 1:
		di=di+1
	if rate8.current() == 2:
		di=di+2
	if rate8.current() == 3:
		di=di+3
	if rate8.current() == 4:
		di=di+4
	if rate8.current() == 5:
		di=di+5

	if rate9.current() == 0:
		di=di+0
	if rate9.current() == 1:
		di=di+1
	if rate9.current() == 2:
		di=di+2
	if rate9.current() == 3:
		di=di+3
	if rate9.current() == 4:
		di=di+4
	if rate9.current() == 5:
		di=di+5

	if rate10.current() == 0:
		di=di+0
	if rate10.current() == 1:
		di=di+1
	if rate10.current() == 2:
		di=di+2
	if rate10.current() == 3:
		di=di+3
	if rate10.current() == 4:
		di=di+4
	if rate10.current() == 5:
		di=di+5

	if rate11.current() == 0:
		di=di+0
	if rate11.current() == 1:
		di=di+1
	if rate11.current() == 2:
		di=di+2
	if rate11.current() == 3:
		di=di+3
	if rate11.current() == 4:
		di=di+4
	if rate11.current() == 5:
		di=di+5

	if rate12.current() == 0:
		di=di+0
	if rate12.current() == 1:
		di=di+1
	if rate12.current() == 2:
		di=di+2
	if rate12.current() == 3:
		di=di+3
	if rate12.current() == 4:
		di=di+4
	if rate12.current() == 5:
		di=di+5

	if rate13.current() == 0:
		di=di+0
	if rate13.current() == 1:
		di=di+1
	if rate13.current() == 2:
		di=di+2
	if rate13.current() == 3:
		di=di+3
	if rate13.current() == 4:
		di=di+4
	if rate13.current() == 5:
		di=di+5

	if rate14.current() == 0:
		di=di+0
	if rate14.current() == 1:
		di=di+1
	if rate14.current() == 2:
		di=di+2
	if rate14.current() == 3:
		di=di+3
	if rate14.current() == 4:
		di=di+4
	if rate14.current() == 5:
		di=di+5

	if rate15.current() == 0:
		di=di+0
	if rate15.current() == 1:
		di=di+1
	if rate15.current() == 2:
		di=di+2
	if rate15.current() == 3:
		di=di+3
	if rate15.current() == 4:
		di=di+4
	if rate15.current() == 5:
		di=di+5

	caf=0.65+(0.01*di)
	fuctionpoint=ufp*caf
	slocf=fuctionpoint*lfval

	if dmfp.current() == 0:
		effortfp = 2.4*((slocf/1000)**1.05)*eaffp
		tdevfp = 2.5*(effortfp**0.38)
	if dmfp.current() == 1:
		effortfp = 3.0*((slocf/1000)**1.12)*eaffp
		tdevfp = 2.5*(effortfp**0.35)
	if dmfp.current() == 2:
		effortfp = 3.6*((slocf/1000)**1.20)*eaffp
		tdevfp = 2.5*(effortfp**0.32)

	try:
		procostfp=costval*tdevfp
		Productivity=fuctionpoint/effortfp
		resfp = tk.Frame(root, width=1024, height=650)
		resfp.place(x=0,y=0)
		lbl2=tk.Label(resfp, text="Result:",font = ("Verdana 10 bold",16))
		lbl2.place(x=20, y=10)

		
		tk.Label(resfp, text="Effort = " +str(round(effortfp,3))+" Person-Months",font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=150)
		tk.Label(resfp, text="Development Time = " +str(round(tdevfp,3))+" Months",font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=200)
		tk.Label(resfp, text="Development Cost = Rs " +str(round(procostfp,3)),font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=250)
		
		def moreinf():
			btnmoreinfo.destroy()
			tk.Label(resfp, text="More Info:").place(x=50, y=300)
			tk.Label(resfp, text="Function Point(s) = " +str(round(fuctionpoint,3))+" ",font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=350)
			tk.Label(resfp, text="Lines of Code = " +str(round(slocf))+" Lines",font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=400)
			tk.Label(resfp, text="Productivity = " +str(round(Productivity,3)),font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=450)
			tk.Label(resfp, text="UFP = " +str(round(ufp,3)),font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=500)
			tk.Label(resfp, text="CAF = " +str(round(caf,3)),font = ("Verdana 10 bold",16), bg='yellow', fg='blue').place(x=50, y=550)


		btnmoreinfo=tk.Button(resfp, text="More Info",command=moreinf)
		btnmoreinfo.place(x=50, y=360)
	
	except ZeroDivisionError:
		messagebox.showinfo("ERROR","Error! Input cannot be Zero.")
		raise_frame(pagefp)
        			


	btn4=tk.Button(resfp, text="Home",command=lambda:raise_frame(window))
	btn4.place(x=900, y=550)

	btn5=tk.Button(resfp, text="Back", command=lambda:raise_frame(pagefp))
	btn5.place(x=820, y=550)

menu = tk.Menu(root) 
root.config(menu=menu) 
filemenu = tk.Menu(menu) 
menu.add_cascade(label='Menu', menu=filemenu) 
filemenu.add_command(label='Home', command=lambda:raise_frame(window))  
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=exitm) 
helpmenu = tk.Menu(menu) 
menu.add_cascade(label='About', menu=helpmenu) 
helpmenu.add_command(label='Developer', command=knowmore) 

#Window

load = Image.open("logo.jpg")
render = ImageTk.PhotoImage(load)
lbl=tk.Label(window,image=render,highlightthickness=0,borderwidth=0)
lbl.image = render
lbl.place(x=240, y=70)
lbl2=tk.Label(window, text="COnstructive COst MOdel II",bg="white",font = ("Verdana 10 bold",16))
lbl2.place(x=360, y=160)

btn1=tk.Button(window, text="Enter", bg="lightgreen", command=lambda:raise_frame(page1))
btn1.place(x=350, y=350)

btn2=tk.Button(window, text="About", bg="lightblue", command=knowmore)
btn2.place(x=470, y=350)

btn3=tk.Button(window, text="Exit", bg="pink", command=exitm)
btn3.place(x=590, y=350)

window.pack()

#PAGE 1
lbl2=tk.Label(page1, text="1. Select the unit for Estimated Software Size:",font = ("Verdana 10 bold",16))
lbl2.place(x=20, y=10)

#var = tk.StringVar()
#var.set("Source Lines Of Code (sLOC)")
insize=("Source Lines Of Code (sLOC)","Function Point (FP)")
tk.Label(page1, text="Select ").place(x=50, y=150)
cb=Combobox(page1, values=insize, width=30)
cb.place(x=100, y=150)
cb.current(0)
def pagesel():
	if cb.current() == 0:
	   	return pagesloc
	if cb.current() == 1:
		return pagefp
btn4=tk.Button(page1, text="Next",command=lambda:raise_frame(pagesel()))
btn4.place(x=900, y=550)

btn5=tk.Button(page1, text="Back", command=lambda:raise_frame(window))
btn5.place(x=820, y=550)



#PAGE SLOC
lbl2=tk.Label(pagesloc, text="2. Source Lines Of Code (sLOC):",font = ("Verdana 10 bold",16))
lbl2.place(x=20, y=10)

de = tk.IntVar(root, value=0)
tk.Label(pagesloc, text="Enter no. of LOC: ").place(x=50, y=60)
loc=tk.Entry(pagesloc, textvariable=de)
loc.place(x=220, y=60)

dec = tk.IntVar(root, value=0)
tk.Label(pagesloc, text="Enter Salary/Cost (in Rs): ").place(x=50, y=90)
cost=tk.Entry(pagesloc, textvariable=dec)
cost.place(x=220, y=90)

tk.Label(pagesloc, text="Development Mode: ").place(x=50, y=120)
devmode=("Organic", "Semi Detached", "Embedded")
dm=Combobox(pagesloc, values=devmode)
dm.place(x=220, y=120)
dm.current(0)
tk.Label(pagesloc, text="Cost Drivers:	a) Required Software Reliability").place(x=50, y=150)
tk.Label(pagesloc, text="		b) Size of Application Database").place(x=50, y=180)
tk.Label(pagesloc, text="		c) Complexity of The Product").place(x=50, y=210)
tk.Label(pagesloc, text="		d) Runtime Performance Constraints").place(x=50, y=240)
tk.Label(pagesloc, text="		e) Memory Constraints").place(x=50, y=270)
tk.Label(pagesloc, text="		f) Volatility of the VM environment").place(x=50, y=300)
tk.Label(pagesloc, text="		g) Required turnabout time").place(x=50, y=330)
tk.Label(pagesloc, text="		h) Analyst capability").place(x=50, y=360)
tk.Label(pagesloc, text="		i) Software engineering capability").place(x=50, y=390)
tk.Label(pagesloc, text="		j) Applications experience").place(x=50, y=420)
tk.Label(pagesloc, text="		k) Virtual machine experience").place(x=50, y=450)
tk.Label(pagesloc, text="		l) Programming language experience").place(x=50, y=480)
tk.Label(pagesloc, text="		m) Use of software tools").place(x=50, y=510)
tk.Label(pagesloc, text="		n) Application of SW engg. methods").place(x=50, y=540)
tk.Label(pagesloc, text="		o) Required development schedule").place(x=50, y=570)


cdriver=("Very Low", "Low", "Nominal", "High", "Very High")
cd1=Combobox(pagesloc, values=cdriver)
cd1.place(x=430, y=150)
cd1.current(2)
cd2=Combobox(pagesloc, values=cdriver)
cd2.place(x=430, y=180)
cd2.current(2)
cd3=Combobox(pagesloc, values=cdriver)
cd3.place(x=430, y=210)
cd3.current(2)
cd4=Combobox(pagesloc, values=cdriver)
cd4.place(x=430, y=240)
cd4.current(2)
cd5=Combobox(pagesloc, values=cdriver)
cd5.place(x=430, y=270)
cd5.current(2)
cd6=Combobox(pagesloc, values=cdriver)
cd6.place(x=430, y=300)
cd6.current(2)
cd7=Combobox(pagesloc, values=cdriver)
cd7.place(x=430, y=330)
cd7.current(2)
cd8=Combobox(pagesloc, values=cdriver)
cd8.place(x=430, y=360)
cd8.current(2)
cd9=Combobox(pagesloc, values=cdriver)
cd9.place(x=430, y=390)
cd9.current(2)
cd10=Combobox(pagesloc, values=cdriver)
cd10.place(x=430, y=420)
cd10.current(2)
cd11=Combobox(pagesloc, values=cdriver)
cd11.place(x=430, y=450)
cd11.current(2)
cd12=Combobox(pagesloc, values=cdriver)
cd12.place(x=430, y=480)
cd12.current(2)
cd13=Combobox(pagesloc, values=cdriver)
cd13.place(x=430, y=510)
cd13.current(2)
cd14=Combobox(pagesloc, values=cdriver)
cd14.place(x=430, y=540)
cd14.current(2)
cd15=Combobox(pagesloc, values=cdriver)
cd15.place(x=430, y=570)
cd15.current(2)

btn4=tk.Button(pagesloc, text="Next",command=locclick)
btn4.place(x=900, y=550)

btn5=tk.Button(pagesloc, text="Back", command=lambda:raise_frame(page1))
btn5.place(x=820, y=550)

#PAGE FP

lbl2=tk.Label(pagefp, text="2. Function Point (FP):",font = ("Verdana 10 bold",16))
lbl2.place(x=20, y=10)

delf = tk.IntVar(root, value=0)
tk.Label(pagefp, text="Language Factor: ").place(x=50, y=60)
lf=tk.Entry(pagefp, textvariable=delf)
lf.place(x=220, y=60)

dec = tk.IntVar(root, value=0)
tk.Label(pagefp, text="Enter Salary/Cost (in Rs): ").place(x=50, y=90)
costfp=tk.Entry(pagefp, textvariable=dec)
costfp.place(x=220, y=90)

tk.Label(pagefp, text="Development Mode: ").place(x=50, y=120)
devmode=("Organic", "Semi Detached", "Embedded")
dmfp=Combobox(pagefp, values=devmode)
dmfp.place(x=220, y=120)
dmfp.current(0)
tk.Label(pagefp, text="Weighting Factor: ").place(x=50, y=150)
wf=("Simple", "Average", "Complex")
wffp=Combobox(pagefp, values=wf)
wffp.place(x=220, y=150)
wffp.current(0)

tk.Label(pagefp, text="14 GSCs Rating:	a) Data communications").place(x=50, y=180)
tk.Label(pagefp, text="		b) Distributed data processing").place(x=50, y=210)
tk.Label(pagefp, text="		c) Performance").place(x=50, y=240)
tk.Label(pagefp, text="		d) Heavily used configuration ").place(x=50, y=270)
tk.Label(pagefp, text="		e) Transaction rate").place(x=50, y=300)
tk.Label(pagefp, text="		f) On-Line data entry").place(x=50, y=330)
tk.Label(pagefp, text="		g) End-user efficiency").place(x=50, y=360)
tk.Label(pagefp, text="		h) On-Line update").place(x=50, y=390)
tk.Label(pagefp, text="		i) Complex processing").place(x=50, y=420)
tk.Label(pagefp, text="		j) Reusability").place(x=50, y=450)
tk.Label(pagefp, text="		k) Installation ease").place(x=50, y=480)
tk.Label(pagefp, text="		l) Operational ease").place(x=50, y=510)
tk.Label(pagefp, text="		m) Multiple sites").place(x=50, y=540)
tk.Label(pagefp, text="		n) Facilitate change").place(x=50, y=570)

rate=("No influence (0)", "Incidental influence (1)", "Moderate influence (2)", "Average influence (3)", "Significant influence (4)","Strong influence (5)")
rate2=Combobox(pagefp, values=rate)
rate2.place(x=430, y=180)
rate2.current(3)
rate3=Combobox(pagefp, values=rate)
rate3.place(x=430, y=210)
rate3.current(3)
rate4=Combobox(pagefp, values=rate)
rate4.place(x=430, y=240)
rate4.current(3)
rate5=Combobox(pagefp, values=rate)
rate5.place(x=430, y=270)
rate5.current(3)
rate6=Combobox(pagefp, values=rate)
rate6.place(x=430, y=300)
rate6.current(3)
rate7=Combobox(pagefp, values=rate)
rate7.place(x=430, y=330)
rate7.current(3)
rate8=Combobox(pagefp, values=rate)
rate8.place(x=430, y=360)
rate8.current(3)
rate9=Combobox(pagefp, values=rate)
rate9.place(x=430, y=390)
rate9.current(3)
rate10=Combobox(pagefp, values=rate)
rate10.place(x=430, y=420)
rate10.current(3)
rate11=Combobox(pagefp, values=rate)
rate11.place(x=430, y=450)
rate11.current(3)
rate12=Combobox(pagefp, values=rate)
rate12.place(x=430, y=480)
rate12.current(3)
rate13=Combobox(pagefp, values=rate)
rate13.place(x=430, y=510)
rate13.current(3)
rate14=Combobox(pagefp, values=rate)
rate14.place(x=430, y=540)
rate14.current(3)
rate15=Combobox(pagefp, values=rate)
rate15.place(x=430, y=570)
rate15.current(3)


btn4=tk.Button(pagefp, text="Next",command=lambda:raise_frame(pagefpcd))
btn4.place(x=900, y=550)

btn5=tk.Button(pagefp, text="Back", command=lambda:raise_frame(page1))
btn5.place(x=820, y=550)

#PAGE FP COSTDRIVERS
lbl2=tk.Label(pagefpcd, text="2. Function Point (FP):",font = ("Verdana 10 bold",16))
lbl2.place(x=20, y=10)

tk.Label(pagefpcd, text="Cost Drivers:	a) Required Software Reliability").place(x=50, y=60)
tk.Label(pagefpcd, text="		b) Size of Application Database").place(x=50, y=90)
tk.Label(pagefpcd, text="		c) Complexity of The Product").place(x=50, y=120)
tk.Label(pagefpcd, text="		d) Runtime Performance Constraints").place(x=50, y=150)
tk.Label(pagefpcd, text="		e) Memory Constraints").place(x=50, y=180)
tk.Label(pagefpcd, text="		f) Volatility of the VM environment").place(x=50, y=210)
tk.Label(pagefpcd, text="		g) Required turnabout time").place(x=50, y=240)
tk.Label(pagefpcd, text="		h) Analyst capability").place(x=50, y=270)
tk.Label(pagefpcd, text="		i) Software engineering capability").place(x=50, y=300)
tk.Label(pagefpcd, text="		j) Applications experience").place(x=50, y=330)
tk.Label(pagefpcd, text="		k) Virtual machine experience").place(x=50, y=360)
tk.Label(pagefpcd, text="		l) Programming language experience").place(x=50, y=390)
tk.Label(pagefpcd, text="		m) Use of software tools").place(x=50, y=420)
tk.Label(pagefpcd, text="		n) Application of SW engg. methods").place(x=50, y=450)
tk.Label(pagefpcd, text="		o) Required development schedule").place(x=50, y=480)


fpdriver=("Very Low", "Low", "Nominal", "High", "Very High")
fpd1=Combobox(pagefpcd, values=fpdriver)
fpd1.place(x=430, y=60)
fpd1.current(2)
fpd2=Combobox(pagefpcd, values=fpdriver)
fpd2.place(x=430, y=90)
fpd2.current(2)
fpd3=Combobox(pagefpcd, values=fpdriver)
fpd3.place(x=430, y=120)
fpd3.current(2)
fpd4=Combobox(pagefpcd, values=fpdriver)
fpd4.place(x=430, y=150)
fpd4.current(2)
fpd5=Combobox(pagefpcd, values=fpdriver)
fpd5.place(x=430, y=180)
fpd5.current(2)
fpd6=Combobox(pagefpcd, values=fpdriver)
fpd6.place(x=430, y=210)
fpd6.current(2)
fpd7=Combobox(pagefpcd, values=fpdriver)
fpd7.place(x=430, y=240)
fpd7.current(2)
fpd8=Combobox(pagefpcd, values=fpdriver)
fpd8.place(x=430, y=270)
fpd8.current(2)
fpd9=Combobox(pagefpcd, values=fpdriver)
fpd9.place(x=430, y=300)
fpd9.current(2)
fpd10=Combobox(pagefpcd, values=fpdriver)
fpd10.place(x=430, y=330)
fpd10.current(2)
fpd11=Combobox(pagefpcd, values=fpdriver)
fpd11.place(x=430, y=360)
fpd11.current(2)
fpd12=Combobox(pagefpcd, values=fpdriver)
fpd12.place(x=430, y=390)
fpd12.current(2)
fpd13=Combobox(pagefpcd, values=fpdriver)
fpd13.place(x=430, y=420)
fpd13.current(2)
fpd14=Combobox(pagefpcd, values=fpdriver)
fpd14.place(x=430, y=450)
fpd14.current(2)
fpd15=Combobox(pagefpcd, values=fpdriver)
fpd15.place(x=430, y=480)
fpd15.current(2)

tk.Label(pagefpcd, text="Count for:       a) External Inputs (EIs)").place(x=650, y=60)
tk.Label(pagefpcd, text="	b) External Outputs (EOs)").place(x=680, y=90)
tk.Label(pagefpcd, text="	c) External Inquiries (EQs)").place(x=680, y=120)
tk.Label(pagefpcd, text="	d) Internal Logic Files (ILFs)").place(x=680, y=150)
tk.Label(pagefpcd, text="	e) External Interface Files (EIFs)").place(x=680, y=180)

deei = tk.IntVar(root, value=0)
ei=tk.Entry(pagefpcd, textvariable=deei, width=5)
ei.place(x=970, y=60)
deeo = tk.IntVar(root, value=0)
eo=tk.Entry(pagefpcd, textvariable=deeo, width=5)
eo.place(x=970, y=90)
deeq = tk.IntVar(root, value=0)
eq=tk.Entry(pagefpcd, textvariable=deeq, width=5)
eq.place(x=970, y=120)
deilf = tk.IntVar(root, value=0)
ilf=tk.Entry(pagefpcd, textvariable=deilf, width=5)
ilf.place(x=970, y=150)
deeif = tk.IntVar(root, value=0)
eif=tk.Entry(pagefpcd, textvariable=deeif, width=5)
eif.place(x=970, y=180)


btn4=tk.Button(pagefpcd, text="Next",command=fpclick)
btn4.place(x=900, y=550)

btn5=tk.Button(pagefpcd, text="Back", command=lambda:raise_frame(pagefp))
btn5.place(x=820, y=550)

root.title('COCOMO II Simulator')
root.geometry("1024x650+10+20")
root.mainloop()