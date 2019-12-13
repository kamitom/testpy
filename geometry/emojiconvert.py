
def emoji(msg):
    emojis_dict = {
        ":)": "😆",
        ":(": "😂",
        ":|": "🥺"
    }

    msg1 = msg.split(" ")

    output = ""
    for w in msg1:
        output += emojis_dict.get(w, w) + " "
    # print(output)
    return output



# print(emoji("good morning tom :) "))



