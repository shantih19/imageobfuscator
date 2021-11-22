from PIL import Image
import random
import sys
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Image Obfusctator",description="Encode and decode data in an image using a seed as a \"password\"")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--decode', help='decode (default)', dest='mode', action="store_false")
    group.add_argument('-e', '--encode', help="encode", dest='mode', action="store_true")
    parser.add_argument('path', help="image path")
    parser.add_argument('seed', help="seed/password")
    parser.add_argument('phrase', help="phrase to encode", nargs= '?')
    parser.add_argument('-o', '--output', help="output path", nargs='?', dest='output')
    args = parser.parse_args()
    filename = args.path
    mode = args.mode
    password = args.seed
    if mode:
        if args.phrase ==  None:
            parser.error("missing phrase to encode")
        phrase = args.phrase.encode('utf-8')
    
    random.seed(password)
    with Image.open(filename) as img:
        w, h = img.size
        if mode:
            im2 = img.copy()
            length = len(phrase)
            x = tuple(random.sample(range(w), w))
            y = tuple(random.sample(range(h), h))
            im2.putpixel((x[0], y[0]), (length//2, length%2, length//2))
            for i in range(0, length, 3):
                v = []
                pixel = (x[(i//3)+1],y[(i//3)+1])
                for b in range(3):
                    if i + b < length:
                        v.append(phrase[i+b])
                    else:
                        v.append(img.getpixel(pixel)[b])
                im2.putpixel(pixel, tuple(v))
            if args.output == None:
                im2.save(os.path.splitext(filename)[0] + "_encoded.png")
            else:
                im2.save(output)
            print("Saved.")
        else:
            text = []
            x = tuple(random.sample(range(w), w))
            y = tuple(random.sample(range(h), h))               
            length = sum(img.getpixel((x[0], y[0])))
            for i in range(0, length, 3):
                for b in range(3):
                    if b + i < length:
                        text.append(img.getpixel((x[(i//3)+1],y[(i//3)+1]))[b])
            print(bytes(text).decode('utf-8'))
            