import json

with open("3500.txt", "r") as f:
    a = f.read()

with open("py2hz.json", "r") as f:
    dict = json.load(f)

for k, v in dict.items():
    filter = [i for i in v if i in a]
    if len(filter) == 0:
        filter = dict[k][0]
    dict[k] = filter

with open("filter_py2hz.json", "w") as f:
    json.dump(dict, f, ensure_ascii=False, indent=4)