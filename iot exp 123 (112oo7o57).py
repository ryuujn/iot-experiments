#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input("Enter the number a= "))
b=int(input("Enter the number b= "))
#ARITHMETIC OPERATORS
summ=a+b
sub=a-b
mul=a*b
div=a/b
floordiv=a//b
mod=b%a
exp=b**a
print("The sum of numbers is ",summ)
print("\nThe subs of numbers is ",sub)
print("\nThe product of numbers is ",mul)
print("\nThe division of numbers is ",div)
print("\nThe floor division of numbers is ",floordiv)
print("\nThe modulus of numbers is ",mod)
print("\nThe exponent of numbers is ",exp)


# In[2]:





# In[ ]:


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amount):
    cipher_text =""
    for letter in plain_text:    
        position = alphabet.index(letter)
        new_position = position +shift_amount
        if new_position > 25:
            new_position2 = new_position-26
            new_letter2 = alphabet[new_position2]
            cipher_text += new_letter2
        else:
            new_letter1 = alphabet[new_position]
            cipher_text += new_letter1
    print(f"The encoded text is {cipher_text}.")

encrypt(plain_text = text,shift_amount = shift)


# In[ ]:


def decrypt(cipher_text, shift_amount):

  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

