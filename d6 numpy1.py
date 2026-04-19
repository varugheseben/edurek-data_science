import numpy as np
import time

size = 1_000_000

# ── Python List ──────────────────────────
py_list = list(range(size))

start = time.perf_counter()
result = [x * 2 for x in py_list]
end = time.perf_counter()
print(f"Python List : {end - start:.4f} seconds")

# ── NumPy Array ──────────────────────────
np_array = np.arange(size)          # ✅ arange, not arrange

start = time.perf_counter()
result = np_array * 2
end = time.perf_counter()
print(f"NumPy Array : {end - start:.4f} seconds")