# otr-decoder-gui
  
#### About:

A small python script I wrote because the official Linux GUI for  
the decoder onlinetvrecorder.com provides did not work for me.  
The python file requires the otrdecoder binary to be in the same  
folder as itself, if you dont want that edit line 77 of the python  
file to point to the binary.  
  
#### Usage:
  
Get the otrdecoder binary from [onlinetvrecorder.com](https://www.onlinetvrecorder.com/v2/software/Linux) and download  
the static 64-bit version. Extract the archive and put the 'otrdecoder'  
file next to the python file. Install [PyQt5](https://pypi.org/project/PyQt5/) and execute the  
python file using Python 3.
  
#### Future Plans:
  
I want to use [otrtool](https://github.com/otrtool/otrtool) instead of the official binary,  
might add that in the future.
