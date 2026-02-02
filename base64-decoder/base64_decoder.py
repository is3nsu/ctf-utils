import sys
import base64

try: 
    source_file = sys.argv[1]
    target_file = sys.argv[2]

    with open(source_file, "r") as source:
        content = source.read()

    if content.endswith('=='):
        decoded = base64.b64decode(content)
    elif content.endswith('='):
        content += '='
        decoded = base64.b64decode(content)
    else:
        content += '=='
        decoded = base64.b64decode(content)

    with open(target_file, "w") as target:
        target.write(str(decoded))

except IndexError:
    print('Use: python3 base64_decoder.py <filename>.txt <filename2>.txt')

