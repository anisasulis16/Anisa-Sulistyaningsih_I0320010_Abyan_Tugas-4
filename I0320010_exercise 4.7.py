#Checking Membership - not in

#Strings
needle = "HA"
haystack = "Hell World"

#Check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")