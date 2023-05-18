import time
import tkinter
from tkinter import ttk
import tkinter as tk
from Scripts.GPU import GPU
import win32api
from Scripts.constants import root_dir
import os


class Selector:
    def __init__(self, gpu: GPU):
        self.gpu = gpu
        self.root = tk.Tk()
        self.app_running = True
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.iconbitmap(os.path.join(root_dir, 'logo.ico'))
        self.root.title('GPU Manager')
        # --------------DRAW GUI----------------------------
        self.frame = ttk.Frame(self.root)
        self.frame.grid(row=0, column=0, padx=10, pady=10)
        text = f'Running Applications on {gpu.name}:'
        text = text + '\n' + (len(text) + 10) * '-'
        header = ttk.Label(self.frame, text=text)
        header.grid(row=0, column=0, columnspan=2)
        self.draw_programs()
        self.set_position()

    def set_position(self):
        monitors = win32api.EnumDisplayMonitors()
        display1 = win32api.GetMonitorInfo(monitors[0][0])
        # from the Work key, select the first and second values
        y_adj = (display1['Work'][1])
        self.root.resizable(False, False)
        self.root.update_idletasks()
        width = self.root.winfo_width()
        screen_width = self.root.winfo_screenwidth()
        x_pos = screen_width - width
        self.root.geometry(f"+{x_pos}+{y_adj}")

    def draw_programs(self):
        self.gpu.get_running_applications()
        self.programs = self.gpu.get_process_names()
        self.rows = []
        starting_row = 1
        for program_name in self.programs:
            p = ttk.Label(self.frame, text=program_name)
            p.grid(row=starting_row, column=0, sticky='w')
            button = ttk.Button(self.frame, text='Stop',
                                command=lambda name=program_name: [self.stop_app(name)])
            button.grid(row=starting_row, column=1, sticky='we', pady=3)
            starting_row += 1
            self.rows.append([p, button])

        if self.rows == []:
            ttk.Label(self.frame, text='No programs running').grid(row=1, column=0, columnspan=2)

    def start(self):
        try:
            while self.app_running:
                self.update()
        except tkinter.TclError:
            pass

    def update(self):
        self.root.update()
        self.root.update_idletasks()

    def stop_app(self, program_name):
        self.gpu.stop_program(program_name)
        program_name = program_name
        for r in self.rows:
            if r[0]['text'] == program_name:
                r[0].destroy()
                r[1].destroy()
                self.rows.remove(r)
        if self.rows == []:
            ttk.Label(self.frame, text='No programs running').grid(row=1, column=0, columnspan=2)

    def close(self):
        self.app_running = False
        self.root.destroy()


if __name__ == '__main__':
    gpu = GPU()
    gpu.get_running_applications()
    selector = Selector(gpu)
    selector.start()
