from shutil import copyfile

src = '/home/ivan/.zshrc'
dst = '/home/ivan/Dropbox/.zshrc'

result = copyfile(src, dst)

print(result)
