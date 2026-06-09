S = "Hello, World"

print("Indexing::1st "+str(S[0]))
print("Indexing::last "+str(S[-1]))
print("Indexing::range of 5words "+str(S[0:5]))
print("Indexing::After 7 "+str(S[7:]))
print("Indexing::Until 5 "+str(S[:5]))
print("Indexing::Every 2nd "+str(S[::2]))
print("Indexing::Reverse "+str(S[::-1]))


print("Upper "+S.upper())
print("Lower "+S.lower())
print("Title "+S.title())
print("replacing "+S.replace("World","Home"))
print("Splitting", S.split(","))
print("LStrip "+S.lstrip())
print("RStrip "+S.rstrip())
print("Strip "+S.strip())
print("Find "+S.find("World"))
print("Count "+S.count("l"))



