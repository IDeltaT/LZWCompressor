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


    # -------------------------- COMPRESS --------------------------- #
    def read_file_binary(self, path):
        '''   '''

        with open(path, 'rb') as file:
            file_content = str(file.read())
        file_content = file_content[2:-1] # remove b''

        return file_content


    def save_compress_file(self, encoded_data, output_path):
        '''   '''
        _save_compress_file(encoded_data, output_path)


    def compress(self, path = 'tests/text_test_1.txt', output_path = 'tests/compressed/'):
        '''   '''

        file_content = self.read_file_binary(path)
        encoded_data = self.encoder.encode(file_content, 32)       
        self.save_compress_file(encoded_data, output_path)


    # ------------------------- DECOMPRESS -------------------------- #
    def read_compress_file(self, path):
        '''   '''

        compressed_data = _read_compress_file(path)
        return compressed_data


    def save_decompress_file(self, decompressed_data):
        '''   '''
       
        with open('tests/decompressed/' + 'DecompressFile', 'wb') as file:
            file.write(decompressed_data)



    def decompress(self, path = 'tests/compressed/'):
        '''   '''

        compressed_data = self.read_compress_file(path)

        decompressed_data = self.decoder.decode(compressed_data, 32)
        decompressed_data = "b'" + decompressed_data + "'"
        decompressed_data = eval(decompressed_data)

        self.save_decompress_file(decompressed_data)


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



@jit()
def _read_compress_file(path):
       
    compressed_data = []

    file_name = 'CompressFile.lzw'

    if file_name:
        file = open(path + file_name, "rb")
        while True:
            rec = file.read(4)
            if len(rec) != 4:
                break
            (data, ) = struct.unpack('>I', rec)
            compressed_data.append(data)

    return compressed_data


print('Read .lzw:')
#compressed_data = insert_text()

print('Decode:')



print('Final time:')
print(time.time() - main_t)



if __name__ == '__main__':
    # DocOpt
    arguments = docopt(__doc__)
    print(arguments)
    print(type(arguments))
    print(arguments['<FILE>'])
    print(arguments['compress'])

    ##################################################################






