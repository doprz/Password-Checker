#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Diego Perez
# Created Date: Fri July 31, 2020
# =============================================================================

##########################################################
#                    Password Checker                    #
##########################################################

# 1. Check if password is inbetween 8 and 32 characters
# 2. At least one lowercase, uppercase, number, and special character


# Extra: Use bitwise operations for more effincieny

# Used to perform bitwise checks
# passwordCheck = int('000000', 2) # 6-bit binary, idealy 8-bit for consistancy

# Initializing to prevent errors
correctLength = 0
verifiedTwice = 0
lowercaseLetter = 0
uppercaseLetter = 0
hasNumber = 0
specialCharacter = 0

# Use bitwise operations to update password check
passwordCheck = correctLength<<5 | verifiedTwice<<4 | lowercaseLetter<<3 | uppercaseLetter<<2 | hasNumber<<1 | specialCharacter


def correctPasswordLength(l_password, min, max):
  if len(l_password) >= min and len(l_password) <= max:
    return True
  elif len(l_password) < min:
    print("\033[91m  Password is too short\033[00m")
  elif len(l_password) > max:
    print("\033[91m  Password is too long\033[00m")

def passwordMeetsRequirements(password):
  lc = False
  uc = False
  hn = False
  sc = False

  for i in password:
    if i.islower():
      lc = True

    if i.isupper():
      uc = True
      
    if i.isnumeric():
      hn = True
    elif not(i.isalpha()):
      sc = True
      
  if lc and uc and hn and sc:
    return True

def update5BitBin(a, b, c, d, e, f):
  return a<<5 | b<<4 | c<<3 | d<<2 | e<<1 | f

def resetPasswordCheck():
  # Access the global variables
  global correctLength
  global verifiedTwice
  global lowercaseLetter
  global uppercaseLetter
  global hasNumber
  global specialCharacter
  global passwordCheck
  
  correctLength = 0
  verifiedTwice = 0
  lowercaseLetter = 0
  uppercaseLetter = 0
  hasNumber = 0
  specialCharacter = 0
  passwordCheck = update5BitBin(0, 0, 0, 0, 0, 0)


print("=" * 40)
print("Password must contain:\n  \033[93m8 - 32 charactrs\033[00m\nAtleast:\n  \033[93mA lowercase character\n  A uppercase character\n  A number\n  And a special character/symbol\033[00m")
print("=" * 40)

# Check for correct password length, and have it verified twice
while ((passwordCheck >> 5 & 1) == 0) and ((passwordCheck >> 4 & 1) == 0):
  password = input("\nEnter your password: ")
  if (correctPasswordLength(password, 8, 32)):
    correctLength = 1

    if passwordMeetsRequirements(password):
      lowercaseLetter = 1
      uppercaseLetter = 1
      hasNumber = 1
      specialCharacter = 1
      # Update Password Check
      passwordCheck = update5BitBin(correctLength, verifiedTwice, lowercaseLetter, uppercaseLetter, hasNumber, specialCharacter)

      # Check password again
      password2 = input("Enter your password again: ")
      if password == password2:
        verifiedTwice = 1
        # Update Password Check
        passwordCheck = update5BitBin(correctLength, verifiedTwice, lowercaseLetter, uppercaseLetter, hasNumber, specialCharacter)
        print("\033[92mPassword Verified\033[00m\n")
      else:
        # Reset Checks
        resetPasswordCheck()
        print("\033[91m  Incorrect Password. Try Again\033[00m")

    else:
      resetPasswordCheck()
      print("\033[91m  Password Character Requirements NOT Met\033[00m")
  else:
    # Reset checks
    resetPasswordCheck()
    # print("\033[91m  Password Length Requirement NOT Met\033[00m")


# De Bugging Tools 
# print(passwordCheck)
# print(bin(passwordCheck)[2:])
# print("\n")

# for i in range(5, -1, -1):
#   print(bin(passwordCheck >> i & 1)[2:])
   
