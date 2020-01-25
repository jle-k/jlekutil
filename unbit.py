#!/usr/bin/python3
from ctypes import c_uint8, c_uint16, c_uint32, c_uint64
#wrapper around ctypes for easier unsigned bitwise operations

def bxor(x, y, type):
    if type == 'byte': 
        return c_uint8(x ^ y).value
    if type == 'word':
        return c_uint16(x ^ y).value
    if type == 'dword':
        return c_uint32(x ^ y).value
    if type == 'qword':
        return c_uint64(x ^ y).value
    print('"Type" not matched. Returning None.')
    return None

def band(x, y, type):
    if type == 'byte':
        return c_uint8(x & y).value
    if type == 'word':
        return c_uint16(x & y).value
    if type == 'dword':
        return c_uint32(x & y).value
    if type == 'qword':
        return c_uint64(x & y).value
    print('"Type" not matched. Returning None.')
    return None

def bor(x, y, type):
    if type == 'byte':
        return c_uint8(x | y).value
    if type == 'word':
        return c_uint16(x | y).value 
    if type == 'dword':
        return c_uint32(x | y).value
    if type == 'qword':
        return c_uint64(x | y).value
    print('"Type" not matched. Returning None.')
    return None

def bshl(x, y, type):
    if type == 'byte':
        return c_uint8(x << y).value
    if type == 'word':
        return c_uint16(x << y).value
    if type == 'dword':
        return c_uint32(x << y).value
    if type == 'qword':
        return c_uint64(x << y).value
    print('"Type" not matched. Returning None.')
    return None

def bshr(x, y, type):
    if type == 'byte':
        return c_uint8(x >> y).value
    if type == 'word':
        return c_uint16(x >> y).value
    if type == 'dword':
        return c_uint32(x >> y).value
    if type == 'qword':
        return c_uint64(x >> y).value
    print('"Type" not matched. Returning None.')
    return None

def badd(x, y, type):
    if type == 'byte':
        return c_uint8(x + y).value
    if type == 'word':
        return c_uint16(x + y).value
    if type == 'dword':
        return c_uint32(x + y).value
    if type == 'qword':
        return c_uint64(x + y).value
    print('"Type" not matched. Returning None.')
    return None
    
def bsub(x, y, type):
    if type == 'byte':
        return c_uint8(x - y).value
    if type == 'word':
        return c_uint16(x - y).value
    if type == 'dword':
        return c_uint32(x - y).value
    if type == 'qword':
        return c_uint64(x - y).value
    print('"Type" not matched. Returning None.')
    return None
    
def binc(x, type):
    if type == 'byte':
        return c_uint8(x + 1).value
    if type == 'word':
        return c_uint16(x + 1).value
    if type == 'dword':
        return c_uint32(x + 1).value
    if type == 'qword':
        return c_uint64(x + 1).value
    print('"Type" not matched. Returning None.')
    return None

def bdec(x, type):
    if type == 'byte':
        return c_uint8(x - 1).value
    if type == 'word':
        return c_uint16(x - 1).value
    if type == 'dword':
        return c_uint32(x - 1).value
    if type == 'qword':
        return c_uint64(x - 1).value

class unbit:

    def __init__(self, initVal, dataType):
       self.value = initVal 
       self.dataType = dataType 

    def bxor(self, operand):
        self.value = bxor(self.value, operand, self.dataType)
    
    def band(self, operand):
        self.value = band(self.value, operand, self.dataType)

    def bor(self, operand):
        self.value = bor(self.value, operand, self.dataType)

    def bshl(self, operand):
        self.value = bshl(self.value, operand, self.dataType)

    def bshr(self, operand):
        self.value = bshr(self.value, operand, self.dataType)

    def badd(self, operand):
        self.value = badd(self.value, operand, self.dataType)

    def bsub(self, operand):
        self.value = bsub(self.value, operand, self.dataType)

    def binc(self):
        self.value = binc(self.value, self.dataType)

    def bdec(self): 
        self.value = bdec(self.value, self.dataType)
    