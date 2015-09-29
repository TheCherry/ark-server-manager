import struct
import zlib

def print_strhex(st):
    out = "0x"
    for char in st[::-1]:
        out += hex(ord(char))[2:4]
    print out


def print_lhex(lo):
    print(hex(lo))


def str_to_l(st):
    out = 0L
    for char in st:
        out += ord(char)
    return out

print_lhex(14124124L)


def z_unpack(src, dst):
    with open(src, 'rb') as f_src:
        with open(dst, 'wb') as f_dst:
            f_src.read(8)
            uncompressedSize = str_to_l(f_src.read(8))
            f_src.read(8)
            uncompressedSize2 = str_to_l(f_src.read(8))
            num = uncompressedSize
            if(num == -1641380927):
                num = 131072L
            num2 = (uncompressedSize2 + num - 1L) / num
            array = []
            num3 = 0L
            num4 = 0
            print(num4)
            print(num2)
            while(num4 < num2):
                array.append(f_src.read(8))
                f_src.read(8)
                num3 = max(array[num4], num3)
                num4 += 1
                num5 = 0L
            data = ""
            print("%i %i" % (num5, num2))
            while(num5 < num2):
                compressed = array[num5]
                print(str_to_l(compressed))
                array2 = f_src.read(str_to_l(compressed))
                data += array2
                num5 += 1L
            print_strhex(data)
            array3 = zlib.decompress(data)
            f_dst.write(array3)

z_unpack("/home/dk/steamcmd/steamapps/workshop/content/346110/525603940/LinuxNoEditor/VH_Buggy/Blueprint/PrimalItemVHBuggy.uasset.z",
"/home/dk/steamcmd/steamapps/workshop/content/346110/525603940/LinuxNoEditor/VH_Buggy/Blueprint/PrimalItemVHBuggy.uasset")
