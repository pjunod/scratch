import sys
#strs = ["flower","flow","flight"]
strs = ["ab","a"]

idx = 0
min_len = 0
for word in strs:
    if min_len == 0:
        min_len = len(word)
    elif len(word) < min_len:
        min_len = len(word)
pfx = strs[0][:idx+1]
while idx < min_len:
    print(f"prefix is {pfx}")
    for word in strs:
        if word.startswith(pfx):
            continue
        else:
            if idx == 0:
                print("nothing")
                sys.exit(0)
            else:
                print(f"final prefix is {strs[0][:idx]}")
                sys.exit(0)
    idx += 1
    pfx = strs[0][:idx+1]
print(f"end prefix is {strs[0][:idx]}")