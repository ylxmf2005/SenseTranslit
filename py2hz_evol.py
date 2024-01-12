from gpt import generate_text
import json
import re

with open('filter_py2hz.json', "r") as f:
    dict = json.load(f)

temp = """
现在，你要根据已有的备选句子 {old}，通过在某个备选句子的末尾添加上一个新的汉字的方式，来形成有意义的新句子，要求:

- 新汉字的拼音是 {cur}
- 参考: {dict}
- 你的输出应以 [ 作为开头, 以 ] 作为结尾，只包含一个列表 ["新句子一", "新句子二", ...], 列表的长度最大为 5，不要包含其它多余信息或注释。
- 输出中的每个新句子都应该有意义，即常用、通顺、适用于特定语境。抛弃排除所有意义不大的句子。
```
"""

def extract(s, pattern):
    match = re.search(pattern, s, re.S)
    return match.group(1) if match else s

def py2hz(pinyin):

    valid = [py for py in pinyin if py in dict]
    invalid = [(i, py) for i, py in enumerate(pinyin) if py not in dict]

    pinyin = valid
    ans = []
    old = []
    for cur in pinyin:
        # print(cur)
        if (len(old) == 0):
            old = dict[cur]
            continue

        prompt = temp.format(old = old, cur = cur, dict = dict[cur])
        response = generate_text(prompt)
        new = extract(response, r"\[(.*?)\]").replace("\"", "").replace(" ", "").split(",")
        
        if (len(new) == 0):
            ans.append(old)
            
        old = new

    if (len(old)):
        ans.append(old)
    
    res = ''.join(i[0] for i in ans)
    res = res.replace('\'', '')

    res = list(res)
    for index, py in invalid:
        res.insert(index, py)

    return res

# print(py2hz(['you', 'mai', 'na', 'la', 'ba', 'dao', 'lai', 'hao', 'dao', 'yo', 'ka', '~', 'ta', 'die', 'xiao', 'wu']))