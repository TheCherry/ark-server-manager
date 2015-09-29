import struct
import zlib

def strhex(st):
    out = "0x"
    for char in st[::-1]:
        out += hex(ord(char))[2:4]
    return out


def print_lhex(lo):
    print(hex(lo))


def str_to_l(st):
    #out = 0L
#    for char in st:
#        out += ord(char)
    #return out
    return struct.unpack('L', st)[0]


def z_unpack(src, dst):
    with open(src, 'rb') as f_src:
        with open(dst, 'wb') as f_dst:
            t = f_src.read(8)
            s = f_src.read(8)
            uncompressedSize = str_to_l(s)
            f_src.read(8)
            uncompressedSize2 = str_to_l(f_src.read(8))
            num = uncompressedSize
            if(num == -1641380927):
                num = 131072L
            runs = (uncompressedSize2 + num - 1L) / num
            array = []
            i = 0
            while(i < runs):
                array.append(f_src.read(8))
                f_src.read(8)
                i += 1
            i = 0
            data = ""
            while(i < runs):
                compressed = array[i]
                array2 = f_src.read(str_to_l(compressed))
                data += array2
                i += 1
            array3 = zlib.decompress(data)
            f_dst.write(array3)

z_unpack("/home/dk/steamcmd/steamapps/workshop/content/346110/525603940/LinuxNoEditor/VH_Buggy/Blueprint/PrimalItemVHBuggy.uasset.z",
"/home/dk/steamcmd/steamapps/workshop/content/346110/525603940/LinuxNoEditor/VH_Buggy/Blueprint/PrimalItemVHBuggy.uasset")
