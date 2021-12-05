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



class LZWCore():
    '''   '''
    
    def __init__(self):
        ''' 
        Init Encoder and Decoder.
        Adding selected ranges to encoder and decoder dictionaries.
        
        '''

        # Encoder init
        self.encoder = Encoder()

        # ASCII punctuation and symbols
        self.encoder.trie_update(32, 47)
        self.encoder.trie_update(58, 64)
        self.encoder.trie_update(91, 96)
        self.encoder.trie_update(123, 126)

        # ASCII digits
        self.encoder.trie_update(48, 57)

        # Latin alphabet
        self.encoder.trie_update(65, 90)
        self.encoder.trie_update(97, 122)


        # Decoder init
        self.decoder = Decoder()

        # ASCII punctuation and symbols
        self.decoder.trie_update(32, 47)
        self.decoder.trie_update(58, 64)
        self.decoder.trie_update(91, 96)
        self.decoder.trie_update(123, 126)

        # ASCII digits
        self.decoder.trie_update(48, 57)

        # Latin alphabet
        self.decoder.trie_update(65, 90)
        self.decoder.trie_update(97, 122)


    def read_fyle_binary(self, path):
        '''   '''

        with open(path, 'rb') as file:
            file_content = str(file.read())
        file_content = file_content[2:-1] # remove b''

        return file_content


    def save_compress_file(self, encoded_data, output_path):
        _save_compress_file(encoded_data, output_path)


    def encode(self, path = 'tests/text_test_1.txt', output_path = 'tests/compressed/'):

        file_content = self.read_fyle_binary(path)
        encoded_data = self.encoder.encode(file_content, 32)       
        self.save_compress_file(encoded_data, output_path)


main_t = time.time()

print('Init decoder and encoder:')


print('Read file (bin mode):')

#t1 = time.time()
#print(time.time() - t1)

print('Encode:')




@jit()
def _save_compress_file(encoded_data, output_path):

    file_name = 'CompressFile' + '' + '.lzw'
    if file_name:
        file = open(output_path + file_name, "wb")
        for data in encoded_data:
            file.write(struct.pack('>I', int(data)))  
        file.close()


#save_result(result)
print('Save .lzw:')









if __name__ == '__main__':
    # DocOpt
    arguments = docopt(__doc__)
    print(arguments)
    print(type(arguments))
    print(arguments['<FILE>'])
    print(arguments['compress'])

    ##################################################################

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