def reader(path: str):
    with open(path, "r") as file:
        output = file.readlines()
    return "".join(output)
