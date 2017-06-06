# -*- coding:utf-8 -*-
__author__ = 'yangxin'
import chardet
def convert(filename, toEncode):
    #gain the src file encode
    f = open(filename, 'rb')
    data = f.read()
    fromEncode = chardet.detect(data)['encoding']
    print fromEncode

    #read the content
    file = open(filename, 'r')
    s = file.read()
    print chardet.detect(s)['encoding']
    file.close()

    #convert the encode
    middle = s.decode(fromEncode)
    s = middle.encode(toEncode)

    #write the content
    f = open(filename, 'wb')
    f.write(s)
    f.close()

filename = "/usr/testData/import1.csv"
convert(filename, "utf-8")