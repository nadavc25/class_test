from .numbers.simp import *
from .numbers.comp import *

simp_called = False  # Flag to check if a function in simp module has been called

def check_simp_called():
    if not simp_called:
        raise Exception("Cannot call functions in comp module before calling at least one function in simp module")
