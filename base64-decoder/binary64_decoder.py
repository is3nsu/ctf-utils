'''
binary64_decoder.py is a binary version of base64_decoder.py

'''

import sys
import base64

try: 
    source_file = sys.argv[1]
    target_file = sys.argv[2]

    with open(source_file, "rb") as source:
        content = source.read()
        decoded = base64.b64decode(content)
    with open(target_file, "wb") as target:
        target.write(decoded)

except IndexError:
    print('Use: python3 binary64_decoder.py <filename>.txt <filename2>.txt')

