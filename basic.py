def flames(name1, name2):
    # Remove spaces and convert to lower
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Count non-matching letters
    temp_name1 = list(name1)
    temp_name2 = list(name2)

    for char in name1:
        if char in temp_name2:
            temp_name2.remove(char)
            temp_name1.remove(char)

    count = len(temp_name1) + len(temp_name2)

    flames = ['F', 'L', 'A', 'M', 'E', 'S']

    while len(flames) > 1:
        idx = (count % len(flames))-1
        if idx == -1:
            flames = flames[:-1]
        else:
            flames = flames[idx+1:] + flames[:idx]

    return flames[0]

# Example usage
name1 = input("Enter first name: ").strip()
name2 = input("Enter second name: ").strip()
print("The relation is :", flames(name1, name2))
