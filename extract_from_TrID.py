from pathlib import Path
import codecs
data = Path(r"triddefs.trd").read_bytes()

nbCurrent = data.find(b'DEF ') # return -1 if not found

delimiters = ['DEF ', 'DATA', 'PATT', 'INFO', 'TYPE', 'EXT ', 'MIME', 'NAME', 'USER', 'URL', 'FNUM', 'MAIL', 'HOME']
delsToNum = ['DEF ', 'DATA', 'INFO']

results = []

i = 0 

def hexToNb (arraybyte) :
    nb = '0x' + ''.join([format(c, '02X') for c in reversed(arraybyte)])
    return int(nb, 16)

def hexToText (arraybyte) : 
    tmpArray = arraybyte[0:2]
    nb = hexToNb (tmpArray)

data = data[nbCurrent:]

while data :
    print(i) 
    i += 1
    # On réduit data
    nbCurrent = 8 + hexToNb(data[4:8])
    current = data[:nbCurrent]
    nbPatt = hexToNb(current[12:16])
    
    obj = {}
    obj['Pattern'] = current[20:20-4+nbPatt]
    current = current[20-4+nbPatt:]
    nbInfo = hexToNb(current[4:8])
    current = current[8:]
    
    while len(current) > 3: 
        nbField = hexToNb (current[4:6])
        field = codecs.decode(current[0:4])
        current = current[6:]
        try : obj[field] = codecs.decode(current[:nbField])
        except : obj[field] = current[:nbField]
        
        current = current[nbField:]
    
    results.append(obj)
    data = data[nbCurrent:]
    
    


#byte = bytes([data[11]])
# b')'.hex()
