
# coding: utf-8
# @author: zhenguo
# @date: 2020-12-16
# @describe: functions about automatic file processing

import pandas as pd  
import os 
import chardet



def get_encoding(filename):
    """
    返回文件编码格式
    """
    with open(filename,'rb') as f:
        return chardet.detect(f.read())['encoding']



def to_utf8(filename):
    """
    保存为 to_utf-8
    """
    encoding = get_encoding(filename)
    ext = os.path.splitext(filename)
    if ext[1] =='.csv':
        if 'gb' in encoding or 'GB' in encoding:
            df = pd.read_csv(filename,engine='python',encoding='GBK')
        else:
            df = pd.read_csv(filename,engine='python',encoding='utf-8')
        df.to_excel(ext[0]+'.xlsx')
    elif ext[1]=='.xls' or ext[1] == '.xlsx':
        if 'gb' in encoding or 'GB' in encoding:
            df = pd.read_excel(filename,encoding='GBK')
        else:
            df = pd.read_excel(filename,encoding='utf-8')
        df.to_excel(filename)
    else:
        print('only support csv, xls, xlsx format')


def batch_to_utf8(path,ext_name='csv'):
    """
    path下，后缀为 ext_name的乱码文件，批量转化为可读文件
    """
    for file in os.listdir(path):
        if os.path.splitext(file)[1]=='.'+ext_name:
            to_utf8(os.path.join(path,file))

