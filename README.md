# LZW Compressor

This software is designed to compress files using the universal lossless data compression algorithm Lempel-Ziv-Welch (LZW).
Interaction with the program is possible through a graphical interface or through a command line interpreter.

## How to start using the software
### GUI
To launch the GUI:

`...\LZWCompressor> python LZWCompressor.py`


### Command Line Interpreter
Using a command window for compression:

`...\LZWCompressor> python LZWCore.py compress <FILE> [PATH] [-t]`

Using a command window for decompression:

`...\LZWCompressor> python LZWCore.py decompress <FILE> [PATH] [-t]`

Arguments:
<pre>
FILE - input file
PATH - directory for saving converted file (optional)
If "PATH" is not specified, the file will be saved to the program directory.
</pre> 

Examples:
<pre>
LZWCore.py compress     /temp/img.bmp   /temp/compressed
LZWCore.py decompress   /temp/img.lzw   /temp/decompressed

LZWCore.py compress     /temp/img.bmp   -t
LZWCore.py decompress   /temp/img.lzw   /temp/decompressed -t

LZWCore.py -h
</pre>

Options:
<pre>
-h, --help    Show help.
-t            Show lead time.
</pre>

## Details
Programming language: Python 3.9

The compression level depends on the file size and type. 
The larger the file size and the more duplicate values it contains, the higher the compression level.
For this reason, the software is better at compressing file formats such as ".bmp" or ".txt".
With other file formats, the compressed file may be larger than the original size.

In the directory "LZWCompression\tests\" you can see the results of the program. 
"text_test_1.txt" is a duplicate text.
"text_test_2.txt" is not a duplicate text. 
Duplicate text ("text_test_1.txt") is compressed better by the software.

After compression, there are two extensions in the file name, the first is the original file extension, the second is ".lzw". 
For example "file_name.txt.lzw". This file name helps to restore the original file extension when decompressed.

### This software was developed for educational purposes.

Other optimized python modules such as "gzip" should be used to compress files.

