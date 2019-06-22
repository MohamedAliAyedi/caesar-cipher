print("\t**************************************************")
print("\t* decrypte caesar-cipher (BruteForce It) By Dali *")
print("\t**************************************************\n")
message = raw_input ("msg encrypted >> ")
words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'

for i in range(len(words)):
	
 decry = ''
 for symbol in message:
    if symbol in words:
        symbolIndex = words.find(symbol)
        movee = symbolIndex - i
        if movee < 0:
             movee = movee + len(words)
        decry = decry + words[movee]
    else:
       decry = decry + symbol
 print('Brute n,#%s: %s' % (i, decry))
