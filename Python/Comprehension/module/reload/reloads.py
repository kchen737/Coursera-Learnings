import importlib
import sample
import filechanges

importlib.reload(sample)
importlib.reload(sample)
#prints hello world from sample several times, reloadded

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass
    
for i in range(5):
    changes()
    input("Hit enter to reload...")