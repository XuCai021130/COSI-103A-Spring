def letter_count(string):
    return {c:string.count(c) for c in string}

statement = "hello"

def letter_count2(string):
    chars = list(string)
    letter = set(chars)
    count = {w:chars.count(w) for w in letter}
    return count

print(letter_count(statement))