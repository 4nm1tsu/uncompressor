import mimetypes
import tarfile
import zipfile

print(mimetypes.guess_type('./something.tar'))
print(mimetypes.guess_type('./something.tar.bz2'))
print(mimetypes.guess_type('./something.tar.gz'))
print(mimetypes.guess_type('./something.tar.xz'))
print(mimetypes.guess_type('./something.zip'))

filepath = input()

"""
tar = tarfile.open(filepath)
tar.extractall()
tar.close()
"""
with zipfile.ZipFile(filepath, 'r') as myzip:
    myzip.extractall()
