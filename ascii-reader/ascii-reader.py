msg = [76, 101, 116, 116, 104, 101, 98, 101, 115, 116, 115, 116, 97, 114, 116, 117, 112, 115, 97, 112, 112, 108, 121, 116, 111, 121, 111, 117, 0]
for m in msg:
    if m is 0:
        break
    print chr(m),

new_msg = "Letthebeststartupsapplytoyou"
new_array = []
for s in new_msg:
    new_array.append(ord(s))
new_array.append(0)
print ""
print new_array
