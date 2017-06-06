# -*- coding:utf-8 -*-
__author__ = 'yangxin'
import codecs
import chardet

def convert_encoding(filename, target_encoding):
    content = codecs.open(filename, 'r').read()
    source_encoding = chardet.detect(content)['encoding']
    if source_encoding != 'utf-8':
        print "SRC File ENCode : " + source_encoding + " FileName : " + filename
        content = content.decode(source_encoding, 'ignore')
        codecs.open(filename, 'w', encoding=target_encoding).write(content)

def main():
    filename = "/data/sftp/mysftp/upload/20170606/ODS_CMBCTBCT.del"
    convert_encoding(filename,'utf-8')

if __name__ == '__main__':
    main()