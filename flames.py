def flames_game(name1,name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)
    total_count = len(name1) + len(name2)
    flames = ["F","L","A","M","E","S"]
    meanings = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    while len(flames) > 1:
        split_index = (total_count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames = flames[:len(flames) - 1]
        final_letter = flames[0]
    return final_letter, meanings[final_letter]
name1 = "Durga"
name2 = "Vaaranya"
result_letter, result_meaning = flames_game(name1, name2)
print(f"The result of FLAMES for {name1} and {name2} is: {result_letter} ({result_meaning})")
