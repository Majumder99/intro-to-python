message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😄",
    ":3": "🥴"
}

output = ""
for word in words:
    if word == ":)":
        output += emojis[":)"]
    elif word == ":3":
        output += emojis[":3"]
    else:
        output += word
print(output)

# or

output = ""

# get(word, word) if there is no matching in dictionaries then the second parameter will print
for word in words:
    output += emojis.get(word, word) + ""

print(output)
