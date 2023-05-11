import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        if 'child' in kw:
            child = kw['child']
            kw.pop('child')
            child.set_master(self)

class Label(tk.Label):
    def __init__(self, master=None, cnf={}, **kw):
        self.cnf = cnf
        self.kw = kw

    def set_master(self, master):
        super().__init__(master=master, cnf=self.cnf, **self.kw)
        self.pack()


root = tk.Tk()

obj = Frame(root, bg="green", width=100, height=50, child=
    Label(text='test')
    )
obj.pack()

root.mainloop()
