#Program to empty Windows Recycle Bin
 
import winshell
 
try:
    winshell.recycle_bin().empty(confirm=True)
    print("Recycle Bin emptied!")
 
except:
    print("Recycle Bin already empty!")
