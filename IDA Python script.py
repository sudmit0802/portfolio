from idaapi import *
from idautils import *

TemplateFunctions = ["sprintf", "snprintf", "vsprintf", "vsnprintf", "gets", "scanf", "sscanf", "snscanf", "fopen", "fgets", "fread", "strcpy", "strncpy", "strcat", "strncat", "makepath", "_splitpath", "memset", "memcpy", "atoi", "atof", "atol", "calloc", "malloc", "realloc"]

print("\n\nSEARCHING...")
print("THESE UNSAFE FUNCTIONS WERE FOUND:\n")

for funcea in Functions():
    if(get_func_name(funcea) in TemplateFunctions):
        for ref in CodeRefsTo(funcea, 1):
            print(get_func_name(funcea) + " at 0x%08x" % ref)