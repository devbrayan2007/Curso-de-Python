# Módulos - import, from, as e *

# Inteiro
import sys

print(sys.platform)


# Partes
from sys import exit, platform

print(platform)

# alias 1
import sys as s
print(s.platform)

# alias 2
from sys import platform as pt, exit as ex

print(pt)
