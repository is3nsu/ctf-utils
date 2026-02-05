import codecs
import sys

source_file = sys.argv[1]
target_file = sys.argv[2]

with open(source_file, 'r') as source:
    source = source.read().replace(' ', '')
decode = codecs.decode(source, 'hex').decode('utf-8')

with open(target_file, 'w') as target:
    target.write(decode)
