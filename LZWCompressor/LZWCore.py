"""Reference.
Usage:
  LZWCore.py compress <FILE> [PATH] [-t]
  LZWCore.py decompress <FILE> [PATH] [-t]

Arguments:
  FILE        input file
  PATH        directory for saving converted file (optional)

Examples:
  LZWCore.py compress /temp/img.bmp /temp/compressed
  LZWCore.py decompress /temp/img.lzw /temp/decompressed

Options:
  -h, --help    Show reference.
  -t            Show lead time.

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
    ''' 
    Implementation of a universal lossless data compression 
    algorithm - LZW.

    The class includes the following main methods:
        compress        - Compress the file using the LZV algorithm.
        decompress      - Decompress the file using the LZV algorithm.
    '''
    
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
    def read_file_binary(self, path: str) -> str:
        ''' Open a file in binary mode and read the whole file. '''

        with open(path, 'rb') as file:
            file_content = str(file.read())
        file_content = file_content[2:-1] # remove b''

        return file_content


    def save_compress_file(self, encoded_data: list, output_path: str):
        '''   '''
        _save_compress_file(encoded_data, output_path)


    def compress(self, path: str = 'tests/text_test_1.txt', 
                 output_path: str = 'tests/compressed/', 
                 l_time: bool = False):
        '''  Compress the file using the LZV algorithm. '''

        lead_time = time.time()

        file_content = self.read_file_binary(path)
        encoded_data = self.encoder.encode(file_content, 32)       
        self.save_compress_file(encoded_data, output_path)

        lead_time = time.time() - lead_time
        if l_time:
            print('Compress - Lead time:', str(lead_time) + 's.')


    # ------------------------- DECOMPRESS -------------------------- #
    def read_compress_file(self, path: str) -> list:
        '''   '''

        compressed_data = _read_compress_file(path)
        return compressed_data


    def save_decompress_file(self, decompressed_data: str):
        '''   '''
       
        with open('tests/decompressed/' + 'DecompressFile', 'wb') as file:
            file.write(decompressed_data)



    def decompress(self, path: str = 'tests/compressed/', 
                   l_time: bool = False):
        ''' Decompress the file using the LZV algorithm. '''

        lead_time = time.time()

        compressed_data = self.read_compress_file(path)

        decompressed_data = self.decoder.decode(compressed_data, 32)
        decompressed_data = "b'" + decompressed_data + "'"
        decompressed_data = eval(decompressed_data)

        self.save_decompress_file(decompressed_data)

        lead_time = time.time() - lead_time
        if l_time:
            print('Decompress - Lead time:', str(lead_time) + 's.')



@jit()
def _save_compress_file(encoded_data, output_path):
    '''   '''
    file_name = 'CompressFile' + '' + '.lzw'
    if file_name:
        file = open(output_path + file_name, "wb")
        for data in encoded_data:
            file.write(struct.pack('>I', int(data)))  
        file.close()


@jit()
def _read_compress_file(path):
    ''' '''
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



if __name__ == '__main__':
    # DocOpt
    arguments = docopt(__doc__)
    print(arguments)
    print(type(arguments))
    print(arguments['<FILE>'])
    print(arguments['compress'])

    ##################################################################


    main_t = time.time()
    print('Final time:')
    print(time.time() - main_t)



