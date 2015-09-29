import struct
import zlib
import sys


def str_to_l(st):
    return struct.unpack('L', st)[0]


def z_unpack(src, dst):
    with open(src, 'rb') as f_src:
        with open(dst, 'wb') as f_dst:
            f_src.read(8)
            uncompressedSize = str_to_l(f_src.read(8))
            f_src.read(8)
            uncompressedSize2 = str_to_l(f_src.read(8))
            if(uncompressedSize == -1641380927):
                uncompressedSize = 131072L
            runs = (uncompressedSize2 + uncompressedSize - 1L) / uncompressedSize
            array = []
            for i in range(runs):
                array.append(f_src.read(8))
                f_src.read(8)
            for i in range(runs):
                compressed = array[i]
                array2 = f_src.read(str_to_l(compressed))
                array3 = zlib.decompress(array2)
                f_dst.write(array3)

if __name__ == "__main__":
    z_unpack(sys.argv[1], sys.argv[2])
