"""Main module."""
import cchardet as chardet

def get_encoding(filename):
    '''
    输入文件路径，返回文件编码
    '''
    with open(filename, "rb") as f:
        msg = f.read()
        result = chardet.detect(msg)
        return result