import os

marker = '/tmp/c02-hook-executed'
with open(marker, 'w') as f:
    f.write('c02-pwned-by-hook ' + os.getlogin())
