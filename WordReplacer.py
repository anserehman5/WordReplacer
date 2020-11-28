print("What word would you like to replace?")
replace = input()

print("What would you like to replace '"+ replace + "' with?")
replaceWith = input()

f = open("textFile.txt", "r+")
newText = f.read().replace(replace, replaceWith)
f.truncate(0)
f.write(newText)
f.close()

print("Done. Check the file to see your new text.")