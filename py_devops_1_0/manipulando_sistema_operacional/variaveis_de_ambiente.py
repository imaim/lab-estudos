import os

print(os.environ['ALLUSERSPROFILE'])
print(os.environ.get('HOME', 'C:\ProgramData'))
print(os.getenv('HOME', 'C:\ProgramData2'))