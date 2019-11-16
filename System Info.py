# Program to check System Information and Python Version

import os
import sys
import platform

print("System:-")
print(os.name)
print(platform.system(),platform.release())
print("----------")
print("Python Version:-")
print(sys.version)
