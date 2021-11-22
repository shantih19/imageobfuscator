# imageobfuscator.py

Encode and decode data in an image using a password

### Usage
    usage: Image Obfustator [-h] [-d | -e] [-o [OUTPUT]] [-f] path seed [phrase]
    
    Encode and decode data in an image using a seed as a "password"
    
    positional arguments:
      path                  image path
      seed                  seed/password
      phrase                phrase to encode
    
    options:
      -h, --help            show this help message and exit
      -d, --decode          decode (default)
      -e, --encode          encode
      -o [OUTPUT], --output [OUTPUT]
                            output path
      -f, --file            phrase is a path to a file to encode

### Dependencies
- Python 3.x
- [Pillow](https://github.com/python-pillow/Pillow "Pillow")

### License

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                        Version 2, December 2004 
    
     Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 
    
     Everyone is permitted to copy and distribute verbatim or modified 
     copies of this license document, and changing it is allowed as long 
     as the name is changed. 
    
                DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
       TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 
    
      0. You just DO WHAT THE FUCK YOU WANT TO.

