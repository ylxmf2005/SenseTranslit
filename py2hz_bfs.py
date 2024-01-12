import json
import math
from bert import get_ppl

with open('filter_py2hz.json', "r") as f:
    dict = json.load(f)

ans = []
threshold = 1000

def bfs(id, old, pinyin):
    # print(id)
    
    if (id >= len(pinyin)):
        ans.append(old)
        return 

    cur = pinyin[id]
    new = []
    
    if (len(old[0][1]) < 4):
        for hz in dict[cur]:
            for _, sentence in old:
                now = sentence + hz
                ppl = get_ppl(now)
                if ((ppl <= threshold) or len(now) <= 2):
                    new.append((ppl, now))

    if (len(new) == 0):
        ans.append(old)
        new = [(math.inf, "")]
        bfs(id, new, pinyin)
        return 

    if (len(new) > 3 and len(new[0][1]) > 1):
        new.sort()
        new = new[:3]

    bfs(id + 1, new, pinyin)


def py2hz(pinyin):
    valid = [py for py in pinyin if py in dict]
    invalid = [(i, py) for i, py in enumerate(pinyin) if py not in dict]

    bfs(0, [(math.inf, "")], valid)
    res = ''.join(i[0] for i in ans)
    res = res.replace('\'', '')

    res = list(res)
    for index, py in invalid:
        res.insert(index, py)

    return res

# print(py2hz(['you', 'mai', 'na', 'la', 'ba', 'dao', 'lai', 'hao', 'dao', 'yo', 'ka', '~', 'ta', 'die', 'xiao', 'wu']))

