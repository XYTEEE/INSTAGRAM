import os, sys
try:
    __import__("Instagram").check_license()
except Exception as e:
    exit(str(e))
 
