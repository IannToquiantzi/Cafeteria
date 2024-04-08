import pytest
from bebidas import validate_input

#(longArticleName)
def test_(self):
  # Enter code here
  assert validate_input("Coffee,12,16,20") == True

#(articleName)
def test_(self):
  # Enter code here
  assert validate_input("C0ffee,12,16,20") == False

#(shortArticleName)
def test_(self):
  # Enter code here
  assert validate_input("A,12,16,20") == False

#(validInput)
def test_(self):
  # Enter code here
  assert validate_input("A,12,16,20") == False

#(invalidSizeValue)
def test_(self):
  # Enter code here
  assert validate_input("Coffee,12,16,100") == False

#(invalidSizeOrder)
def test_(self):
  # Enter code here
  assert validate_input("Coffee,12,16,10") == False

#(emptyInput)
def test_(self):
  # Enter code here
   assert validate_input("") == False

#(singleSize)
def test_(self):
  # Enter code here
  assert validate_input("Coffee,12") == True

#(maxSizes)
def test_(self):
  # Enter code here
  assert validate_input("Coffee,1,2,3,4,5") == True

#(extraSpaces)
def test_(self):
  # Enter code here
  assert validate_input("   Coffee  ,  12,  16, 20  ") == True

#(invalidSizeNotInteger)
def test_(self):
  # Enter code here
  assert validate_input("Coffee,12,16,a") == False