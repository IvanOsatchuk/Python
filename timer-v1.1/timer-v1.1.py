#pyinstaller --onefile --windowed  --icon=icon.ico timer-v1.1.py


from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time
import sys
import os


def theme():
   global theme_v
   theme_var.get()
   themes = {'Dark': 'darkly',
             'Light': 'minty',
             'Normal': 'flatly'}
   theme_v = themes.get(theme_var.get())
   s.theme_use(theme_v)

def restart():
   if len(sys.argv) > 1:
      sys.argv[1] = str(root.winfo_rootx())
      sys.argv[2] = str(root.winfo_rooty())
   else:
      sys.argv.append(str(root.winfo_rootx()))
      sys.argv.append(str(root.winfo_rooty()))
   python = sys.executable
   os.execl(python, python, * sys.argv)

def on_stop():
   global times, f_stop
   times = -1
   input_var.set(f'{00:02}:{00:02}:{00:02}')
   b_pause.config(state="disabled")
   b_continue.config(state="disabled")
   

def on_pause():
   global times 
   global aux
   global b_pause, flag_pause, f_stop

   aux = times
   times = -1
   flag_pause = True
   print(times)
   root.title('Timer - Pausado')
   b_pause.config(bootstyle="SECONDARY")
   b_continue.config(bootstyle="SUCCESS")


def on_continue():
   global times 
   global aux, flag_pause
   
   times = aux 
   flag_pause = False
   print(times)
   root.title('Timer')
   countdowntimer(times)


def layout_timer_run():
   global b_continue, b_pause, label_saida

   frame_timer = Frame(root)
   frame_timer.pack()

   label_saida = ttk.Label(frame_timer, textvariable=input_var, bootstyle="INVERSE-PRIMARY", font=("", 40))
   label_saida.pack(side=LEFT, padx=2)

   frame_bt_timer = Frame(frame_timer)
   frame_bt_timer.pack(side=RIGHT, fill=BOTH, padx=2, pady=2)


   frame_pause_continue = Frame(frame_bt_timer)
   frame_pause_continue.pack(side=TOP)

   b_pause = ttk.Button(frame_pause_continue, text='⏸', bootstyle="WARNING", command=on_pause, width=3)
   b_pause.pack(side=LEFT, padx=1)

   b_continue = ttk.Button(frame_pause_continue, text='▶', bootstyle="SECONDARY", command=on_continue, width=3)
   b_continue.pack(side=LEFT, padx=1)


   frame_restart_stop = Frame(frame_bt_timer)
   frame_restart_stop.pack(side=BOTTOM)

   b_stop = ttk.Button(frame_restart_stop, text='■', bootstyle="DARK", command=on_stop, width=3)
   b_stop.pack(side=LEFT, padx=1)


   b_restart = ttk.Button(frame_restart_stop, text='⟳', bootstyle="DANGER", command=restart, width=3)
   b_restart.pack(side=LEFT, padx=1)


def countdowntimer(input_t=None):
   global times
   global b_pause_stop, label_saida, flag_pause

   if not input_t:
      hrs = int(entry_hrs.get())
      mins = int(entry_mins.get())
      sec = int(entry_sec.get())
      times = hrs*3600 + mins*60 + sec
   
   else:
      times = input_t

   for i in root.winfo_children():
         i.destroy()

   layout_timer_run()

   while times > -1:

      minute,second = (times // 60 , times % 60)
      hour = 0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec = second
      mins = minute
      hrs = hour
      input_var.set(f'{hrs:02}:{mins:02}:{sec:02}')
      label_saida.update()
      time.sleep(1)
      if(times == 0):
         sec = '00' 
         mins = '00'
         hrs = '00'
         starttime = time.time()
         cont = True
         i = 0
         while cont:
            if i % 2 == 0:
               label_saida.config(bootstyle="INVERSE-DANGER")
            else:
               label_saida.config(bootstyle="DANGER")
            label_saida.update()
            time.sleep(0.5)
            i += 1
      times -= 1

   

root = ttk.Window()

root.title('Timer')
root.attributes('-toolwindow', True)
root.attributes("-topmost", True)
root.resizable(0,0)

s = ttk.Style()

if len(sys.argv) > 1:
   root.geometry(f'+{sys.argv[1]}+{sys.argv[2]}')
else:
   root.geometry('+300+300')

input_var = StringVar()

sec = StringVar()
mins = StringVar()
hrs = StringVar()

theme_var = StringVar()

width_entry = 4

frame_inicio = ttk.Frame(root, bootstyle="light")
frame_inicio.pack(fill=BOTH)

frame_theme = ttk.Frame(root, bootstyle="default")
frame_theme.pack(side=BOTTOM)

# ================================== entradas =================================

label = ttk.Label(frame_inicio, text='Tempo (hh mm ss):', bootstyle="inverse-light")
label.pack(side=LEFT, padx=5, pady=5)

entry_hrs = ttk.Entry(frame_inicio, textvariable=hrs, width=width_entry, justify='center')

entry_hrs.pack(side=LEFT, padx=5, pady=5)
entry_hrs.insert(0, "00")

entry_mins = ttk.Entry(frame_inicio, textvariable=mins, width=width_entry, justify='center')
entry_mins.pack(side=LEFT, padx=5, pady=5)
entry_mins.insert(0, "00")

entry_sec = ttk.Entry(frame_inicio, textvariable=sec, width=width_entry, justify='center')
entry_sec.pack(side=LEFT, padx=5, pady=5)
entry_sec.insert(0, "00")

b_start = ttk.Button(frame_inicio, text='Start', bootstyle="PRIMARY",  command = countdowntimer)
b_start.pack(padx=5, pady=5)


# ================================== temas =================================
theme_check_dark = ttk.Radiobutton(frame_theme, bootstyle="success-round-toggle", text = "Dark", variable=theme_var, value='Dark', command=theme)
theme_check_dark.pack(side=LEFT, padx=5, pady=5)

theme_check_light = ttk.Radiobutton(frame_theme, bootstyle="success-round-toggle", text = "Ligth", variable=theme_var, value='Light',command=theme)
theme_check_light.pack(side=LEFT, padx=5, pady=5)

theme_check_normal = ttk.Radiobutton(frame_theme, bootstyle="success-round-toggle", text = "Normal", variable=theme_var, value='Normal', command=theme)
theme_check_normal.pack(side=LEFT, padx=5, pady=5)

root.mainloop()

