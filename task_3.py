#!/usr/bin/env python3

class MyString:
    def __init__(self, value):
        self.value = str(value)

    def __gt__(self, other):
        '''Compares an object of class MyString against another\
         object of the same type according to the operator, based\
          on the length of the value attribute. Returns True or False'''
        if len(self.value) > len(other.value):
            return True
        else:
            return False

    def __ge__(self, other):
        '''Compares an object of class MyString against another\
         object of the same type according to the operator, based\
          on the length of the value attribute. Returns True or False'''
        if len(self.value) >= len(other.value):
            return True
        else:
            return False

    def __lt__(self, other):
        '''Compares an object of class MyString against another\
         object of the same type according to the operator, based\
          on the length of the value attribute. Returns True or False'''
        if len(self.value) < len(other.value):
            return True
        else:
            return False

    def __le__(self, other):
        '''Compares an object of class MyString against another\
         object of the same type according to the operator, based\
          on the length of the value attribute. Returns True or False'''
        if len(self.value) <= len(other.value):
            return True
        else:
            return False

    def __eq__(self, other):
        '''Compares an object of class MyString against another\
         object of the same type according to the operator, based\
          on the length of the value attribute. Returns True or False'''
        if len(self.value) == len(other.value):
            return True
        else:
            return False

# Testcase 1
print("Testcase 1")
string1 = MyString(100)
string2 = MyString("fifteen")
print(f'Values: {string1.value} and {string2.value}\n>: {str(string1 > string2)}\n\
>=: {str(string1 >= string2)}\n<: {str(string1 < string2)}\n\
<=: {str(string1 <= string2)}\n=: {str(string1 == string2)}\n')

# Testcase 2
print("Testcase 2")
string1 = MyString(3.0)
string2 = MyString("two")
print(f'Values: {string1.value} and {string2.value}\n>: {str(string1 > string2)}\n\
>=: {str(string1 >= string2)}\n<: {str(string1 < string2)}\n\
<=: {str(string1 <= string2)}\n=: {str(string1 == string2)}\n')

# Testcase 3
print("Testcase 3")
lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.".split()
string1 = MyString(lorem_ipsum)
string2 = MyString("fifteen")
print(f'Values: {string1.value} and {string2.value}\n>: {str(string1 > string2)}\n\
>=: {str(string1 >= string2)}\n<: {str(string1 < string2)}\n\
<=: {str(string1 <= string2)}\n=: {str(string1 == string2)}\n')
