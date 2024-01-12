with open("input.txt", "r") as f:
    lyric = f.read()

from jp2py import jp2py
from py2hz_im import py2hz
from gpt import generate_text

temp = """
\"{sentence}\"
在括号中填写内容（也可以不填），得到一个完整有意义的的故事，除了故事外不要回复其他信息。
"""

process_history = {}
explain_history = {}

def process_sentence(sentence):
    if (sentence in process_history):
        return process_history[sentence]
    pinyin = jp2py(sentence)
    sentence = py2hz(pinyin)
    pinyin = ' '.join(pinyin)
    process_history[sentence] = (sentence, pinyin)
    return (sentence, pinyin)

def get_explain(sentence):
    if (sentence in explain_history):
        return explain_history[sentence]
    modified_sentence = ''.join(['()' + i for i in sentence]) + '()'
    prompt = temp.format(sentence = modified_sentence)
    explain = generate_text(prompt, model = "gpt-4-1106-preview")
    explain = explain.replace("\"", "").replace(" ", "").replace('(', '').replace(')', '')
    explain_history[sentence] = explain
    return explain

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    hzs = []
    pys = []
    explains = []
    processed_lines =[]
    for id, line in enumerate(lines):
        sentences = line.split()  
        processed_lines.append([process_sentence(sentence) for sentence in sentences])
        hzs.append(' '.join([i[0] for i in processed_lines[id]]))
        pys.append(' '.join([i[1] for i in processed_lines[id]]))

    for id, line in enumerate(lines):
        explains.append('\n'.join([get_explain(i[0]) for i in processed_lines[id]]))

    with open(output_file, 'w', encoding='utf-8') as file:
        for hz, py, explain in zip(hzs, pys, explains):
            file.write("**" + hz + "** " + py + "\n" + explain + "\n\n")
            

input_file = 'input.txt'  
output_file = 'output.txt'  
process_file(input_file, output_file)
