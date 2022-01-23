import hashlib

openedFile = open("texte.txt")
readFile = openedFile.read()
print(readFile)
readFile=readFile.encode()

md5Hash = hashlib.md5(readFile)
md5Hashed = md5Hash.hexdigest()

sha1Hash = hashlib.sha1(readFile)
sha1Hashed = sha1Hash.hexdigest()

print ("File Name: %s",readFile)
print ("MD5: %r",  md5Hashed)
print ("SHA1: %r" , sha1Hashed)
f= open("texte.sha","w")
f.write(sha1Hash.hexdigest())
f.close()
