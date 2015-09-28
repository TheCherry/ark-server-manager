
def z_unpack(src, dst):
    with open(src, 'rb') as f_src:
        with open(dst, 'wb') as f_dst:
            compressedSize = f_src.read(8)
            uncompressedSize = f_src.read(8)
            compressedSize2 = f_src.read(8)
            uncompressedSize2 = f_src.read(8)
            num = uncompressedSize
            if(num == -1641380927):
                num = 131072L
            num2 = (uncompressedSize2 + num - 1L) / num
            array = []
            num3 = 0L
            num4 = 0
            while(num4 < num2):
                data = f_src.read(16)
                array[num4] = data[0-7]
                num3 = Math.Max(array[num4], num3)
                num4 += 1
                num5 = 0L
                while(num5 < num2):
                    compressed = array[num5]
                    array2 = f_src.read(compressed)
                    array3 = ZlibStream.UncompressBuffer(array2)
                    binaryWriter.Write(array3, f_dst)
                    num5 += 1L
