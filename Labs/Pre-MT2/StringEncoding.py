

# ASCII
# American Standard Code for Information Interchange
def char_ordinal(char):
    return ord(char)

def char_hexadecimal(char):
    return hex(ord(char))


# Unicode
from unicodedata import name, lookup
def unicode_name(char):
    return name(char)

def name_to_unicode(search):
    return lookup(search)


# Searching available methods for types
def find_methods(t):
    return dir(t)

