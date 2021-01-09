try:
	from tkinter import *
	import tkinter.messagebox as tmsg
	from tkinter.filedialog import *
	import pygame
	import os
	os.system('cls')

	root = Tk()
	root.title('Music Player By Aaditya Kandel')
	root.minsize(700,180)
	root.maxsize(700,180)

	pygame.init()

	def turnoff():
		b2.config(text = "Auto Load [ Turned Off ]",bg = 'red',fg = "white",font = "comicsansms 12",command=turnon)
		os.system('del dta1.dta')
		os.system('cls')

	def turnon():
		b2.config(text="Auto Load [ Turned On ]",bg="green",fg="white",command=turnoff)
		f = open('dta1.dta','w+')
		f.write('turned on')
		f.close()

	def killmusic():
		pygame.mixer.music.stop()
		b3.config(text="",borderwidth=0,state=DISABLED)
		b4.config(text="Play Music",borderwidth=1,command=playmusic)
		b5.config(text="",borderwidth=0,state=DISABLED)
		b6.config(text="",borderwidth=0,state=DISABLED)
		b7.config(text="",borderwidth=0,state=DISABLED)
		b8.config(text="",borderwidth=0,state=DISABLED)
		b1.config(state=NORMAL)
		root.minsize(700,180)
		root.maxsize(700,180)

	def restartmusic():
		pygame.mixer.music.rewind()

	def resumemusic():
		pygame.mixer.music.unpause()
		b4.config(text="Pause Music",command=pausemusic,borderwidth=1)

	def pausemusic():
		pygame.mixer.music.pause()
		b4.config(text="Resume Music",command=resumemusic)

	def volincrease():
		vola = pygame.mixer.music.get_volume()
		pygame.mixer.music.set_volume(vola+0.2)
		volaa = pygame.mixer.music.get_volume()
		b6.config(text=f"Volume {'%.1f'%volaa}")

	def voldecrease():
		vola = pygame.mixer.music.get_volume()
		pygame.mixer.music.set_volume(vola-0.1)
		volaa = pygame.mixer.music.get_volume()
		b6.config(text=f"Volume {'%.1f'%volaa}")

	def playmusic():
		if (en1.get()) == "" or (en1.get()) == "None":
			tmsg.showinfo('Warning','Music Not Found, Please Browse The Location Of Your Music')
		else:
			pygame.mixer.music.load((en1.get()))
			pygame.mixer.music.play(loops=0)
			b3.config(text="Kill Music",borderwidth=1,state=NORMAL)
			b5.config(text="Restart Music",borderwidth=1,state=NORMAL)
			b4.config(text="Pause Music",command=pausemusic,borderwidth=1)
			vola = pygame.mixer.music.get_volume()
			b6.config(text=f"Volume: {'%.1f'%vola}",state=NORMAL)
			b7.config(text="+",borderwidth=1,command=volincrease,state=NORMAL)
			b8.config(text="- ",borderwidth=1,command=voldecrease,state=NORMAL)
			root.minsize(700,210)
			root.maxsize(700,210)
			b1.config(state=DISABLED)

	def brwse():
		a = askopenfile()
		en1.set(a)
		b = (en1.get())[25:-29]
		en1.set(b)
		f = open('brs.dta','w+')
		f.write((en1.get()))
		f.close()

	en1 = StringVar()

	try:
		f = open('brs.dta','r+')
		for words in f:
			pass
		en1.set(words)
		f.close()
	except:
		pass

	def loadunload():
		try:
			f = open('dta1.dta','r+')
			f.close()
			playmusic()
			turnon()
		except:
			pass

	f1 = Frame(borderwidth = 10,bg = 'black')
	f2 = Frame(borderwidth = 10,bg = 'black')
	f3 = Frame(borderwidth = 10,bg = 'black')
	f4 = Frame(borderwidth = 10,bg = 'black')

	l1 = Label(f1,text = "File Location: ",bg = 'black',fg = "white",font = "comicsansms 12 italic")
	entry1 = Entry(f1,textvariable = en1,bg = "white",fg = "black",font = "comicsansms 12 bold",width = 55,state=DISABLED)
	b1 = Button(f1,text = "Browse",bg = 'black',fg = "white",font = "comicsansms 12 italic",command=brwse)

	l1.pack(side=LEFT)
	entry1.pack(side=LEFT)
	Label(f1,text = "",bg="black").pack(side=LEFT)
	b1.pack(side=LEFT)

	b2 = Button(f2,text = "Auto Load [ Turned Off ]",bg = 'red',fg = "white",font = "comicsansms 12",command=turnon)
	b2.pack()

	b3 = Button(f3,text = "",bg = 'black',fg = "white",font = "comicsansms 12",command=killmusic,state=DISABLED,borderwidth=0,pady=4,padx=4,relief=SUNKEN)
	b4 = Button(f3,text = "Play Music",bg = 'black',fg = "white",font = "comicsansms 12",command=playmusic,pady=4,padx=4,relief=SUNKEN)
	b5 = Button(f3,text = "",bg = 'black',fg = "white",font = "comicsansms 12",command=restartmusic,state=DISABLED,borderwidth=0,pady=4,padx=4,relief=SUNKEN)


	b3.pack(side=LEFT)
	b4.pack(side=LEFT)
	b5.pack(side=LEFT)

	b6 = Label(f4,text = "",bg = 'black',fg = "white",font = "comicsansms 12",state=DISABLED,borderwidth=0,pady=4,padx=4,relief=SUNKEN)
	b7 = Button(f4,text = "",bg = 'black',fg = "white",font = "comicsansms 12",pady=4,padx=4,relief=SUNKEN,state=DISABLED,borderwidth=0)
	b8 = Button(f4,text = "",bg = 'black',fg = "white",font = "comicsansms 12",state=DISABLED,borderwidth=0,pady=4,padx=4,relief=SUNKEN)


	b6.pack(side=LEFT)
	b7.pack(side=LEFT)
	Label(f4,text="",bg="black").pack(side=LEFT)
	b8.pack(side=LEFT)

	f1.pack(anchor="w")
	f2.pack(anchor="w")
	f3.pack(anchor="w")
	f4.pack(anchor="w")

	root.config(bg = 'black')

	loadunload()

	root.mainloop()
except:
	quit()