from obfuscator import Obfuscator
import sys
import os

enabled = []
path = ""
out = ""

for arg in sys.argv:
    if arg.startswith("--path="):
        path = arg[7:]
    elif arg.startswith("--out="):
        out = arg[6:]
    else:
        enabled.append(arg)

def processEnabledModules():
    enabled_modules = [False, False, False, False, False, False]
    
    for module in enabled:
        if module == "--strings":
            enabled_modules[0] = True
        elif module == "--imports":
            enabled_modules[1] = True
        elif module == "--functions":
            enabled_modules[2] = True
        elif module == "--variables":
            enabled_modules[3] = True
        elif module == "--classes":
            enabled_modules[4] = True
        elif module == "--comments":
            enabled_modules[5] = True
    
    return enabled_modules

print(path)
print(out)

try:
    with open(path, 'r', encoding='UTF-8') as code:
        obf = Obfuscator(code.read(), *processEnabledModules())
        code.close()
except:
    print("Invalid source path.")
    input("Enter...")
    os.close()
    
obfuscated = obf.obfuscate()

try:
    with open(out, 'w', encoding='UTF-8') as result:
        result.write(obfuscated)
        result.close()
except:
    print("Invalid out path.")
    input("Enter...")
    os.close()

print("Done!")
input("Enter...")