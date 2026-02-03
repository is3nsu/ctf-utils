import sys
import base64

try: 
    source_file = sys.argv[1]
    target_file = sys.argv[2]
    mode = sys.argv[3]

    with open(source_file, "r") as source:
        content = source.read().strip()
    decoded = base64.b64decode(content + '===')

    
    if mode in ('--bin' or '-b'):
        with open(target_file, 'wb') as target:
            target.write(decoded)
    elif mode in ('--txt' or '-t'): 
        try: 
            with open(target_file, "w") as target:
                target.write(decoded.decode('utf-8'))
        except UnicodeDecodeError: # if decoded is binary, force binary
            with open(target_file, "wb") as target:
                target.write(decoded)

except IndexError:
    print('Use: python3 b64dec.py <filename>.txt <filename2>.txt --output_type')

