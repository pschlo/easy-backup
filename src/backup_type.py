import tkinter as tk


class BackupType():
    FULL = 'full'
    INCREMENTAL = 'incremental'
    DIFFERENTIAL = 'differential'


options_type = [
    BackupType.FULL,
    BackupType.DIFFERENTIAL,
    BackupType.INCREMENTAL
]



class DayWeek():
    DAY = 'day',
    WEEK = 'week',
    MONTH = 'month',
    YEAR = 'year'


class IntervalSetter(tk.Frame):
    def __init__(self, master=None, var_type=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        assert var_type is not None
        self.var_type = var_type
        for type_ in options_type:              # full, incremental, differential
            self.build_subframe(type_)
        self.update()

    def update(self, *args):
        for name, widget in self.children.items():
            widget.grid_remove()
            if name == BackupType.FULL or name == self.var_type.get():
                widget.grid()
            
            # print(*[val.get() for val in widget.children.values() if type(val) is tk.Entry])
            print(self.getvar(BackupType.INCREMENTAL))
    
    def build_subframe(self, name):
        frame = tk.Frame(self, name=name)
        tk.Label(frame, text='Perform %s backup' % name).grid(row=0, column=0)

        entry = tk.Entry(frame, name='num', width=3)
        entry.grid(row=0, column=1)

        tk.Label(frame, text='time(s) per').grid(row=0, column=2)
        options_interval = [
            DayWeek.DAY,
            DayWeek.WEEK,
            DayWeek.MONTH,
            DayWeek.YEAR
        ]
        var = tk.StringVar(name=name)
        var.set(options_interval[1])
        tk.OptionMenu(frame, var, *options_interval).grid(row=0, column=3)