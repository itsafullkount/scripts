from shutil import copyfile

src = '/home/ivan/.zshrc'
dstone = '/home/ivan/Dropbox/.zshrc'
dsttwo = '/home/ivan/Repos/zshrc/.zshrc'

result = copyfile(src, dstone)
result = copyfile(src, dsttwo)

print(result)
