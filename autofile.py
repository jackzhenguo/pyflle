
# coding: utf-8

# In[2]:


import pandas as pd  
import os 
import chardet


# In[4]:


def get_encoding(file):
    """
    返回文件编码格式
    """
    with open(file,'rb') as f:
        return chardet.detect(f.read())['encoding']

file_name="./2020-10-05 - 排线明细结果.csv"  #此处替换为你自己的文件路径
encoding = get_encoding(file_name)
print(encoding)


# In[17]:


def bad_to_good(filename):
    """
    乱码文件转化为可读文件
    """
for file in os.listdir():
    if os.path.splitext(file)[1]=='.csv':
        print(file)
        encoding = get_encoding(file)
        if 'gb' in encoding or 'GB' in encoding:
            df = pd.read_csv(file,engine='python',encoding='GBK')
        else:
            df = pd.read_csv(file,engine='python',encoding=encoding)
        df.to_excel('各天排线v1.1/'+os.path.splitext(file)[0]+".xlsx")
        


# In[3]:


def bad_to_good(filename):
    """
    乱码文件转化为可读文件
    """
    encoding = get_encoding(filename)
    if 'gb' in encoding or 'GB' in encoding:
        df = pd.read_csv(filename,engine='python',encoding='GBK')
    else:
        df = pd.read_csv(filename,engine='python',encoding=encoding)
    df.to_excel(os.path.splitext(filename)[0]+".xlsx")


# In[ ]:


def bad_to_good_batch(path,ext_name='csv'):
    """
    path下，后缀为 ext_name的乱码文件，批量转化为可读文件
    """
    for file in os.listdir(path):
        if os.path.splitext(file)[1]=='.'+ext_name:
            bad_to_good(os.path.join(path,file))

