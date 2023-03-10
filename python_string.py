name = "kamrul"
# print(name)
# print(name[0])

#if we can print multi line then use this format
msg = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(msg)

# for i in "kamrul":
#     print(i)

fName = "kamrul"
# print(len(fName))

txt = "python is a OOP programming language"
# print("python" in txt)
# print("OOP" not in txt)


# if "python" in txt: 
#     print("Yes, 'python' is present")

# if 'kamrul' not in txt:
#     print("No, 'kamrul' is not present")

# msg = "Hello, How are you"
# print(msg[0:5])
# print(msg[:3])
# print(msg[7:])
# articleNo = "sks-40511327540"
# print(articleNo[-4:-2]) #get last 4 digit and removed last 2 digit
# print(articleNo[:-2]) #removed last 2 digit
# print(articleNo.upper())
# print(articleNo.lower())

# msg = " Hello, Bangladesh "
# print(msg.strip()) #emoves any whitespace from the beginning or the end

# print(msg.replace("H", "h"))
# print(msg.split(","))

fName = "kamrul"
lName = "hasan"
fullName = fName + ' ' + lName
print(fullName)
print(fullName.capitalize())
age = 26

info = "My Name is " + fullName + ", I am {} years old"
print(info.format(age))

qty = 36
item = 7
price = 854.36
myOrder = "I want {} pieces of item {} for {} taka"
myOrder2 = "I want to pay {2} taka for {0} pieces of item {1}"
print(myOrder.format(qty, item, price))



