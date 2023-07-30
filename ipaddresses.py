
ip_addresses = [
    "123.211.100.13",
    "271.142.67.142",
    "225.217.132.58"
]
# Write your code here
ans = []
for ip in ip_addresses:
    s = ip.split(".")
    for i in range(len(s)):
        s[i] = int(s[i])
    if (s[0]<0 or s[1]<0 or s[2]<0 or s[3]<0 or s[0]>255 or s[1]>255 or s[2]>255 or s[3]>255):
        ans.append(-1)
    elif (s[0] <128):
        ans.append(1)
    elif (s[0] < 192):
        ans.append(2)
    elif (s[0] < 224):
        ans.append(3)
    elif (s[0] < 240):
        ans.append(4)
    elif (s[0] < 256):
        ans.append(5)

print(ans)