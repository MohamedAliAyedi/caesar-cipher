print("\t************************************************")
print("\t* crypte caesar-cipher (BruteForce It) By Dali *")
print("\t************************************************\n")

message = raw_input ("msg > ")
print("=====================")
print("= majus of A no a ! =")
print("=====================")
key_smb = raw_input ("A == ")
mode = 'encrypt'
words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'
key = words.find(key_smb)
crypteed = ''
for symbol in message:
 if symbol in words:
   symbolIndex = words.find(symbol)
   if mode == 'encrypt':
     movedd = symbolIndex + key
   elif mode == 'decrypt':
     movedd = symbolIndex - key
   if movedd >= len(words):
     movedd = movedd - len(words)
   elif movedd < 0:
     movedd = movedd + len(words)  
   crypteed = crypteed + words[movedd]
 else:
    crypteed = crypteed + crypteed
print("crypte >  "+crypteed)
