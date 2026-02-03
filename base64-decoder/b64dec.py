import sys
import base64

source_file = sys.argv[1]
target_file = sys.argv[2] 
mode = None

if len(sys.argv) == 4:
    mode = sys.argv[3]
elif len(sys.argv) != 3:
    print("Use: b64dec <input> <output> [--bin|-b|--txt|-t]")
    sys.exit(1)

with open(source_file, "r") as source:
    content = source.read().strip()
decoded = base64.b64decode(content + '===')

if mode in ('--bin', '-b'):
    with open(target_file, 'wb') as target:
        target.write(decoded)
elif mode in ('--txt', '-t'): 
    try: 
        with open(target_file, "w") as target:
            target.write(decoded.decode('utf-8'))
    except UnicodeDecodeError: # if decoded is binary, force binary
        with open(target_file, "wb") as target:
            target.write(decoded)
elif mode is None:
    try: 
        with open(target_file, "w") as target:
            target.write(decoded.decode('utf-8'))
    except UnicodeDecodeError: # if decoded is binary, force binary
        with open(target_file, "wb") as target:
            target.write(decoded)


