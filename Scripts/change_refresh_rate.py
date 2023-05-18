import os
from .constants import qres_dir


def change_refresh_rate(target_refresh_rate: int):
    if target_refresh_rate not in (240, 60):
        return
    os.chdir(qres_dir)
    set_60fps = f'qres f={target_refresh_rate}'
    os.system(set_60fps)


if __name__ == '__main__':
    change_refresh_rate(240)
