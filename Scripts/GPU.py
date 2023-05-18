import os
import signal
import sys

from Scripts.get_stats import get_stats


class GPU:
    def __init__(self):
        self.id = None
        self.name = None
        self.usage = None
        self.processes = None
        self.stats = None

    def get_running_applications(self):
        self.stats = get_stats()
        self.id = self.stats['id']
        self.name = self.stats['name']
        self.usage = self.stats['usage']
        self.processes = self.stats['processes']

    def stop_all(self):
        if self.processes == {}:
            return False
        for process in self.processes:
            pid = int(self.processes[process])
            os.kill(pid, signal.SIGTERM)
        return True

    def stop_program(self, process_name):
        for process in self.processes:
            pid = int(self.processes[process])
            if process == process_name:
                os.kill(pid, signal.SIGTERM)
                return

    def get_process_names(self) -> list:
        res = []
        for process_name in self.processes:
            res.append(process_name)
        return res

    def __str__(self):
        return str(self.stats)
