import string
import random
from PIL import Image

def random_generator(size = 8, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def rotation(deg, name, label):
    img = Image.open('/home/xxx/tasse_full/images/grun.png')
    img = img.rotate(deg, expand = True)
    img.save('/home/xxx/tasse_full/test/green/' + label + '/' + name + '.jpg')


def fill(x):
    for i in range(x):
        rotation(i, random_generator(), '20')

    for i in range(x):
        rotation(i + 20, random_generator(), '40')

    for i in range(x):
        rotation(i + 40, random_generator(), '60')

    for i in range(x):
        rotation(i + 60, random_generator(), '80')

    for i in range(x):
        rotation(i + 80, random_generator(), '100')

    for i in range(x):
        rotation(i + 100, random_generator(), '120')

    for i in range(x):
        rotation(i + 120, random_generator(), '140')

    for i in range(x):
        rotation(i + 140, random_generator(), '160')

    for i in range(x):
        rotation(i + 160, random_generator(), '180')

    for i in range(x):
        rotation(i + 180, random_generator(), '200')

    for i in range(x):
        rotation(i + 200, random_generator(), '220')

    for i in range(x):
        rotation(i + 220, random_generator(), '240')

    for i in range(x):
        rotation(i + 240, random_generator(), '260')

    for i in range(x):
        rotation(i + 260, random_generator(), '280')

    for i in range(x):
        rotation(i + 280, random_generator(), '300')

    for i in range(x):
        rotation(i + 300, random_generator(), '320')

    for i in range(x):
        rotation(i + 320, random_generator(), '340')

    for i in range(x):
        rotation(i + 340, random_generator(), '360')




fill(20)