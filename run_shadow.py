#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["my_ris", "cow", "ccc", "king", "cube", "box"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        Polyedr(f"data/{name}.geom").draw(tk)
        delta_time = time() - start_time
        pl = Polyedr(f"data/{name}.geom")
        print(f"Изображение полиэдра '{name}' заняло {delta_time}"
              f"сек, сумма проекций площадей {pl.area_ob}.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
