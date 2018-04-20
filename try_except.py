# try / except structure
# You surround a dangerous section of code with try and except
# if the code in the try works, the except is skipped
# if the code in the try fails, it jumps to the except section

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
    
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)



rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')
