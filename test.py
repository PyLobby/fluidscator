# This is default obf-test file!

import random as rnd

enable = 1
helloworld = "Hello, World! ( helloworld var)" if 1==enable else "Bye-Bye, World!" + 'a' + 'b'

print(rnd.uniform(0, enable))

class World:
    def __init__(self, string):
        self.string = string
        self.info = "WORLD CLASS"

    def lLIIIlLiiliiI71(self):
        print(self.string)

    def lllIl1LIi1ILI61(self):
        return self.info

if helloworld == "Hello, World! ( helloworld var)":
    print(helloworld + ";")

    world = World("bla-bla...")
    world.lLIIIlLiiliiI71()
    print("^ it was function from " + world.info)
else:
    try:
        print("string" + 1)
    except Exception as e:
        print(e.with_traceback)

words = ['Foo!', 'Boo!', 'Bar!']

def python(words):
    for word in words:
        print(word)

def nopython():
    print("No python() here!")

python(words=words)
strwords = ' '.join(words)
print(strwords)
print(strwords.split("o"))
print(strwords.replace(" ", "; "))