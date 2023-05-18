from Scripts.GPU import GPU
import pystray
import PIL.Image
from Scripts.change_refresh_rate import change_refresh_rate
from Scripts.constants import img_dir
import tkinter as tk
from tkinter import ttk
import os
from Scripts.stop_a_program_selector import Selector


class App:
    def __init__(self):
        # ---------------logo---------------------------------
        img = PIL.Image.open(img_dir)
        # ---------------menuItem------------------------------
        self.stop_programs = pystray.MenuItem('Stop all programs running on NVIDIA GPU', self.stop_all_programs)
        # ---------------menuItem------------------------------
        self.stop_program = pystray.MenuItem('Stop a specific program', self.programs_submenu)
        # ---------------menuItem------------------------------
        set_240 = pystray.MenuItem('240 Hz', self.set_240)
        set_60 = pystray.MenuItem('60 Hz', self.set_60)
        self.refresh_rate = pystray.MenuItem('Change refresh rate', pystray.Menu(set_60, set_240))
        # ---------------menuItem------------------------------
        self.quit_item = pystray.MenuItem('Exit', self.quit)
        # ----------------------------------------------------
        menu = pystray.Menu(self.stop_programs, self.stop_program, self.refresh_rate, self.quit_item)
        self.icon = pystray.Icon('GPU Manager', img, menu=menu)
        self.icon.title = 'GPU Manager'
        self.icon.run()

    def stop_all_programs(self, event):
        gpu = GPU()
        gpu.get_running_applications()
        programs_running = gpu.stop_all()
        if programs_running:
            self.icon.notify('Programs Stopped')
        else:
            self.icon.notify('No programs were running on the NVIDIA GPU')

    def programs_submenu(self, event):
        gpu = GPU()
        gpu.get_running_applications()
        selector = Selector(gpu=gpu)
        selector.start()
        return

    def quit(self, event):
        self.icon.stop()

    def set_240(self, event):
        # self.icon.notify('Refresh Rate set to 240Hz')
        change_refresh_rate(240)

    def set_60(self, event):
        # self.icon.notify('Refresh Rate set to 60Hz')
        change_refresh_rate(60)


if __name__ == '__main__':
    app = App()
