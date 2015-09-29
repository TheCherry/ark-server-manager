import struct
import zlib
import sys


def str_to_l(st):
    return struct.unpack('L', st)[0]


def z_unpack(src, dst):
    with open(src, 'rb') as f_src:
        with open(dst, 'wb') as f_dst:
            f_src.read(8)
            size1 = str_to_l(f_src.read(8))
            f_src.read(8)
            size2 = str_to_l(f_src.read(8))
            if(size1 == -1641380927):
                size1 = 131072L
            runs = (size2 + size1 - 1L) / size1
            array = []
            for i in range(runs):
                array.append(f_src.read(8))
                f_src.read(8)
            for i in range(runs):
                to_read = array[i]
                compressed = f_src.read(str_to_l(to_read))
                decompressed = zlib.decompress(compressed)
                f_dst.write(decompressed)

if __name__ == "__main__":
    z_unpack(sys.argv[1], sys.argv[2])
