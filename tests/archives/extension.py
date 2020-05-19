import mimetypes

print(mimetypes.guess_extension(mimetypes.guess_type('./something.tar.xz')[0]))
