def convert(string):
    return " ".join(sorted(list(set(string.lower().split()))))

print(convert("HI hello my Name is HI hi netra netra"))