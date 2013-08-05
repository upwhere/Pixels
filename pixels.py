"""
Gets pixels every X seconds and draws an image out of them.
A lazy Sunday afternoon hack!
"""

import time

import Image
manualgrab = "" # false, for now.
try:
    import ImageGrab
except ImportError:
    try:
        import pyscreenshot as ImageGrab # fall back on pyscreenshot, cross-platform.
    except ImportError:
        import os
        linuxTmpFilename = "/tmp/Pixels.onepixel.png" # we have to use an intermediate file when no appropriate libraries are loadable, write to /tmp/, the ramdisk, to prevent unneccesary disk activity.
        manualgrab = "import -silent -window root %s" % linuxTmpFilename # the OS command to create a screenshot file ( -silent: don't ring the system bell on each screenshot, -window root: capture the entire screen, not just the active window )





X = 1 # seconds to pause before taking next pixel
WIDTH = 1366 # the width of the image drawn, higher number = slower
HEIGHT = 768 # the height of the image drawn, higher number = slower

if __name__ == '__main__':

    start = time.time()
    
    pixels_img = Image.new('RGB', (WIDTH, HEIGHT), 'black') # create a new Image instance
    pixels = pixels_img.load()
    
    for w in xrange(WIDTH):
        if not manualgrab:
            img = ImageGrab.grab() # take a screenshot
        else:
            os.system(manualgrab)
            img = Image.open(linuxTmpFilename)

        img = img.resize((WIDTH, HEIGHT)) # create a thumbnail
        for h in xrange(HEIGHT):
            pixels[w, h] = img.getpixel((w, h)) # pixels(x, y) = (r, g, b)
        time.sleep(X)

    pixels_img.save('pixel.png', 'PNG')
    pixels_img.show()

    print time.time() - start
