s = "Take up one idea and make that idea your life."\
    "Think and dream of that idea and leave other idea alone."
subs = "idea"
found = False
position = -1
length = len(s)
while True:
    position = s.find(subs,position+1,length)
    if position == -1:
        break
    print("Found the substring at position ",position)
    found = True
if found == False:
    print("Substring not found")