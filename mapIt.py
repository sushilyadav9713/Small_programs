import webbrowser, sys
sys.path.append(r"C:\Users\dell\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages")
import clipman

clipman.init()

print(clipman.get())
if len(sys.argv)> 1:
    address = ' '.join(sys.argv[1:])
else:
    address = clipman.get()

webbrowser.open('https://www.google.com/maps/place/' + address)