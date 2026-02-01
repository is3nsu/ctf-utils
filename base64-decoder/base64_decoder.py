import base64

print('Input base64 encoded text:')
encoded = input(">")

if encoded.endswith('==') or encoded.endswith('='):
    decoded = base64.b64decode(encoded)
else:
    encoded = encoded + '=='
    decoded = base64.b64decode(encoded)

print(f'Decoded text: {decoded}')
