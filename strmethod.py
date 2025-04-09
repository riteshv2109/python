# strings are immutable i.e. not changable
a="ritesh"

print(a.upper())

b="what are you doing????"
print(b.upper())
print(b.rstrip("?"))
# rstrip skips trailing characters but deosn't skips starting 
print(a.replace("ritesh","manoj"))
print(b.split())