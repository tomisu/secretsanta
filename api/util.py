import hashlib

def computeMD5hash(string):
    m = hashlib.md5()
    try:
        m.update(string.encode('utf-8'))
    except AttributeError:
        return None
        
    return m.hexdigest()
