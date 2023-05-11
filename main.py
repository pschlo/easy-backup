import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import csv
import os
from backup_type import BackupType, DayWeek, IntervalSetter
# import backup_type

appdata = os.getenv('appdata')
assert isinstance(appdata, str)
app_folder = os.path.join(appdata, 'EasyBackup')
app_config = os.path.join(app_folder, 'config.txt')
app_paths = os.path.join(app_folder, 'paths.csv')
if not os.path.exists(app_folder):
    os.mkdir(app_folder)

def add_file():
    choice = filedialog.askopenfiles()
    
    with open(app_paths) as f:
        for row in f:
            print(row.replace('\n', '').split(' -> '))
    return

def add_folder():
    choice = filedialog.askdirectory()
    return choice


options_type = [
    BackupType.FULL,
    BackupType.DIFFERENTIAL,
    BackupType.INCREMENTAL
]


def dummy():
    return


root = tk.Tk()
root.title('EasyBackup')
# root.geometry('800x500')
bg = root['bg']
# font = ('Verdana', 20)
root.iconbitmap('favicon.ico')

title = tk.Label(root, text="EasyBackup", font="TkDefaultFont 25 bold italic", anchor="w")
title.grid(row=0, column=0)


frame_backups = tk.LabelFrame(root, text='Backups', bg='green', width=100, height=200)
frame_backups.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)
# frame_backups.grid_rowconfigure(1, weight=1)
# frame_backups.grid_columnconfigure(1, weight=1)

listbox_backups = tk.Listbox(frame_backups, activestyle="none", selectmode="extended", width=30, height=10)
listbox_backups.grid(row=1, column=0, columnspan=2, sticky='news', padx=10, pady=10)

# tk.Button(frame_backups, text='X', command=None).grid(row=1, column=0, sticky='n')

button_add_folder = tk.Button(frame_backups, text='+ Add Backup Definition', command=add_file, width=20, height=1, pady=5)
button_add_folder.grid(row=2, column=0)

button_rem = tk.Button(frame_backups, text='- Remove Backup Definition', command=dummy, width=22, height=1, pady=5)
button_rem.grid(row=2, column=1)

### frame_details
frame_details = tk.LabelFrame(root, text='Details', bg='red', width=100, height=200)
frame_details.grid(row=1, column=1, sticky='nesw', padx=10, pady=10)
# frame_details.grid_rowconfigure(0, weight=1)
# frame_details.grid_columnconfigure(0, weight=1)


##### frame_details_name
tk.Label(frame_details, text='Name').grid(row=0, column=0)

frame_details_name = tk.Frame(frame_details)
frame_details_name.grid(row=0, column=1)

tk.Entry(frame_details_name).grid(row=0, column=0)


##### frame_details_source
tk.Label(frame_details, text='Sources').grid(row=1, column=0)

frame_details_source = tk.Frame(frame_details)
frame_details_source.grid(row=1, column=1)

listbox_from = tk.Listbox(frame_details_source, activestyle="none", selectmode="extended", width=80, height=10)
listbox_from.grid(row=0, column=0, columnspan=2, sticky='news', padx=10, pady=10)

button_add_folder = tk.Button(frame_details_source, text='+ Add Folder', command=add_file, width=15, height=1, pady=5)
button_add_folder.grid(row=1, column=0)

button_rem = tk.Button(frame_details_source, text='- Remove Folder/File', command=dummy, width=18, height=1, pady=5)
button_rem.grid(row=1, column=1)


##### frame_details_destination
tk.Label(frame_details, text='Destination').grid(row=2, column=0)

frame_details_destination = tk.Frame(frame_details)
frame_details_destination.grid(row=2, column=1)


tk.Button(frame_details_destination, text='Change', command=dummy).grid(row=0, column=1)
tk.Button(frame_details_destination, text='Open', command=dummy).grid(row=0, column=2)




##### frame_details_type
tk.Label(frame_details, text='Type').grid(row=3, column=0)

frame_details_type = tk.Frame(frame_details)
frame_details_type.grid(row=3, column=1)

var_type = tk.StringVar(name='var_type')
var_type.set(options_type[2])

tk.OptionMenu(frame_details_type, var_type, *options_type).grid(row=0, column=0)


##### frame_details_interval
tk.Label(frame_details, text='Interval').grid(row=4, column=0)

interval_setter = IntervalSetter(frame_details, var_type)
var_type.trace("w", interval_setter.update)
interval_setter.grid(row=4, column=1)


root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
