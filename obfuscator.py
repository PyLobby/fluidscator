import binascii
import random
import re

class Obfuscator:
    def __init__(self, code='print("Hello, World!")', obfstr=False, obfimp=False, obffun=False, obfvar=False, obfclasses=False, obfcomments=False):
        self.obfstr = obfstr
        
        self.code = "import binascii\n" + code if self.obfstr else code
        self.names = ['L', 'l', '1', 'i', 'I']
        
        self.obfimp = obfimp
        self.obffun = obffun
        self.obfvar = obfvar
        self.obfclasses = obfclasses
        self.obfcomments = obfcomments

    def generate_name(self):
        name = random.choice(['L', 'l', 'i', 'I']) # You can't name variable with number as first character
        
        # 15,504 variations
        for i in range(16):
            name += random.choice(self.names)
        
        return name
    
    def obf_comments(self):
        self.code = re.sub(r'(?=#).+', '', self.code)
    
    def obf_imports(self):
        imports = re.findall(r'import (\w+) as (\w+)', self.code)
        
        for original, signed in imports:
            sign_as = self.generate_name()
            
            self.code = re.sub(f'import {original} as {signed}', f'import {original} as {sign_as}', self.code)
            self.code = re.sub(r'(?<![a-zA-Z_"\'])' + signed + r'(?![a-zA-Z0-9_"\'])', sign_as, self.code)

    
    def obf_strings(self):
        
        # THIS OBFUSCATION DOESN'T WORK, IF YOU CAN FIX IT, PLEASE CONTACT ME ON GITHUB OR DISCORD - yer#7700
        # What's going on here?
        # The problem is F-Strings, when I trying to obfuscate python script with f-string, it doesn't save variables from the original f-string
        # For example:
        # print(f"Hello {world}!")
        # Output:
        # > Hello {world}!
        # As you can see, the f-string doesn't apply any changes...
        
        strings = re.findall(r'(u".+?"|r".+?"|f".+?"|".+?"|\'.+?\')', self.code)

        for string in strings:
            prestr = string.replace('\"','').replace('\'','')
            print(binascii.unhexlify(str(binascii.hexlify(string.encode()).decode())).decode())
            self.code = self.code.replace(string, f"f'binascii.unhexlify({str(binascii.hexlify(string.encode()).decode())}).decode()'")
            
            # This method doesn't work, if you have solution, please contact me on github or on discord - yer#7700
            # self.code = re.sub(f"{string}", f"binascii.unhexlify({str(binascii.hexlify(prestr.encode()))}).decode()", self.code)

    def obf_classes(self):
        classes = re.findall(r'class (\w+)', self.code)

        for code_class in classes:
            if not code_class.startswith("__") and not code_class.endswith("__"):
                name = self.generate_name()
                
                self.code = re.sub(code_class, name, self.code)
                self.code = re.sub(r'(?<![a-zA-Z_"\'])' + code_class + r'(?![a-zA-Z0-9_"\'])', name, self.code)
    
    def obf_functions(self):
        functions = re.findall(r'def (\w+)', self.code)

        for func in functions:
            if not func.startswith("__") and not func.endswith("__"):
                name = self.generate_name()
                
                #self.code = re.sub(func, name, self.code)
                self.code = re.sub(r'(?<![a-zA-Z_"\'])' + func + r'(?![a-zA-Z0-9_"\'])', name, self.code)
    
    def obf_variables(self):
        variables = re.findall(r'(\w+)(?=( = .*))', self.code)
        
        for var in variables:
            name = self.generate_name()
            
            self.code = re.sub(r'(?<![a-zA-Z_"\'])' + var[0] + r'(?![a-zA-Z0-9_"\'])', name, self.code)
    
    def obfuscate(self):
        # init obfuscation
        
        if self.obfstr:
            self.obf_strings()
        if self.obfcomments:
            self.obf_comments()
        if self.obfimp:
            self.obf_imports()
        if self.obfclasses:
            self.obf_classes()
        if self.obffun:
            self.obf_functions()
        if self.obfvar:
            self.obf_variables()
        
        return self.code