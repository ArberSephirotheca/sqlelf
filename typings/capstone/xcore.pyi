"""
This type stub file was generated by pyright.
"""

import ctypes
from .xcore_const import *

class XcoreOpMem(ctypes.Structure):
    _fields_ = ...


class XcoreOpValue(ctypes.Union):
    _fields_ = ...


class XcoreOp(ctypes.Structure):
    _fields_ = ...
    @property
    def imm(self): # -> Any:
        ...
    
    @property
    def reg(self): # -> Any:
        ...
    
    @property
    def mem(self): # -> Any:
        ...
    


class CsXcore(ctypes.Structure):
    _fields_ = ...


def get_arch_info(a): # -> list[Any]:
    ...

