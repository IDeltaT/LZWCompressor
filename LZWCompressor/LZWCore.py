"""Reference.
Usage:
  LZWCore.py compress <FILE> [PATH]
  LZWCore.py decompress <FILE> [PATH]

Arguments:
  FILE        input file
  PATH        directory for saving converted file (optional)

Examples:
  LZWCore.py compress /temp/img.bmp /temp/compressed
  LZWCore.py decompress /temp/img.lzw /temp/decompressed

Options:
  -h, --help
"""

from docopt import docopt


import struct
import time
from numba import jit

import warnings
warnings.filterwarnings('ignore')

from Encoder import Encoder
from Decoder import Decoder


main_t = time.time()


t1 = time.time()
encoder = Encoder()
encoder.trie_update(32, 47)
encoder.trie_update(58, 64)
encoder.trie_update(91, 96)
encoder.trie_update(123, 126)
encoder.trie_update(48, 57)
encoder.trie_update(65, 90)
encoder.trie_update(97, 122)

decoder = Decoder()
decoder.trie_update(32, 47)
decoder.trie_update(58, 64)
decoder.trie_update(91, 96)
decoder.trie_update(123, 126)
decoder.trie_update(48, 57)
decoder.trie_update(65, 90)
decoder.trie_update(97, 122)

print('Init decoder and encoder:')
print(time.time() - t1)
print()


t1 = time.time()
#file = open("test_2_bmp.bmp","rb")
file = open("tests/text_test_1.txt","rb")

fileContent = str(file.read())
file.close()
fileContent = fileContent[2:-1]
print('Read file (bin mode):')
print(time.time() - t1)
print()


t1 = time.time()
result = encoder.encode(fileContent, 32)

print('Encode:')
print(time.time() - t1)
print()


@jit()
def save_result(result):

    file_name = 'CompressFile' + '' + '.lzw'
    if file_name:
        encoded_data = result

        file = open('tests/compressed/' + file_name, "wb")
        for data in encoded_data:
            file.write(struct.pack('>I', int(data)))  
        file.close()

t1 = time.time()
save_result(result)
print('Save .lzw:')
print(time.time() - t1)
print()




@jit()
def insert_text():
       
    compressed_data = []

    file_name = 'CompressFile.lzw'

    if file_name:
        file = open('tests/compressed/' + file_name, "rb")
        while True:
            rec = file.read(4)
            if len(rec) != 4:
                break
            (data, ) = struct.unpack('>I', rec)
            compressed_data.append(data)

    return compressed_data

t1 = time.time()
compressed_data = insert_text()
print('Read .lzw:')
print(time.time() - t1)
print()


t1 = time.time()
result = decoder.decode(compressed_data, 32)
print('Decode:')
print(time.time() - t1)
print()


result = "b'" + result + "'"


t1 = time.time()
file = open('tests/decompressed/' + 'DecompressFile', "wb")
res = eval(result)
file.write(res)
file.close()
print('Save file:')
print(time.time() - t1)
print()

print('Final time:')
print(time.time() - main_t)



if __name__ == '__main__':
    # DocOpt
    arguments = docopt(__doc__)
    print(arguments)
    print(type(arguments))
    print(arguments['<FILE>'])
    print(arguments['compress'])