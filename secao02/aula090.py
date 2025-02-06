# Recarregando módulos, importlib e singleton
import importlib

import aula090_m

for i in range(10):
    importlib.reload(aula090_m)
    print(i)

print('Fim')
