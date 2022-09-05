characters = ["U", "C", "P", "C"]


def main(sentence):
    for c in characters:
        n = sentence.find(c)
        if n == -1:
            return "I hate UCPC"
        sentence = sentence[n + 1 :]
    return "I love UCPC"


s = input()
print(main(s))
