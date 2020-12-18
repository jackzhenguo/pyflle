
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
        if 'gb' in encoding.lower():
            df = pd.read_csv(filename, engine='python', encoding='GBK',index_col=False)
        else:
            df = pd.read_csv(filename,engine='python',encoding=encoding,index_col=False)
        df.to_csv(filename, encoding='utf-8-sig', index=False)
        
    elif ext[1] in ('.xls','.xlsx'):
        if 'gb' in encoding or 'GB' in encoding:
            df = pd.read_excel(filename,encoding='GBK')
        else:
            df = pd.read_excel(filename,encoding='utf-8')
        df.to_excel(filename)
    else:
        print('only support csv, xls, xlsx format')
    print('to_utf8 succeed')


def batch_to_utf8(path,ext_name='csv'):
    """
    path下，后缀为 ext_name的乱码文件，批量转化为可读文件
    """
    for file in os.listdir(path):
        if os.path.splitext(file)[1]=='.'+ext_name:
            to_utf8(os.path.join(path,file))


def combine_files(path, save_name='combine.csv'):
    """
    @param: path下合并所有后缀为csv的文件到save_name一个文件里
    @param: save_name 合并后的文件名称
    @return: 打印成功信息表明合并OK，并在path的上一级目录输出合并后save_name文件
    """
    if 
    tmp = pd.DataFrame()
    for filename in os.listdir(path):
        fs = os.path.splitext(filename)
        if fs[1] == '.csv':
            df = pd.read_csv(filename, engine='python', index_col=False)
        elif fs[1] in ('.xls','.xlsx'):
            df = pd.read_excel(filename, index_col=False)
        if len(df) <= 0:
            continue
        df.loc[:,'unnamed'] = fs[0]
        tmp = tmp.append(df)

    if 'csv' in save_name:
        tmp.to_csv('../' + save_name, encoding='utf-8-sig', index=False)
    elif 'xls' in save_name or 'xlsx' in save_name:
        tmp.to_excel('../' + save_name)
    else:
        print('the name of outputting file must be with csv, xls, xlsx format')

    print('combining succeed')


if __name__ == '__main__':
    combine_files('./testdata/titanic-train.csv')