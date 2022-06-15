# mosaic Generator
program that generates pictures out of pictures

# Requirements
numpy
opencv_python
tqdm

# Workflow
the generator reqires a map file consisting of a map of pictures names and there average colour
so to generate custom images you will a large datasett of pictures and run the mapfunction on the directory where that is kept

then you should be able to simply run the program with all thouse variables inserted 

# Warning
this program is very stupid and has no trouble generating image files that are many Gb's in size
when opencv tries to display such large files YOUR COMPUTER WILL CRASH
