import pykakasi

def sol(input_text):
    mapping = {
        'シャ': 'xia ',
        'シュ': 'xiu ',
        'ショ': 'xiao ',
        'チャ': 'qia ',
        'チュ': 'qiu ',
        'チョ': 'qiao ',
        'ニュ': 'niu ',
        'ニョ': 'niao ',
        'ミュ': 'miu ',
        'ミョ': 'miao ',
        'リャ': 'lia ',
        'リュ': 'liu ',
        'リョ': 'liao ',
        'ジャ': 'jia ',
        'ジュ': 'jiu ',
        'ジョ': 'jiao ',
        'ピョ': 'piao ',
        'ヴァ': 'wa ',
        'ヴィ': 'wei ',
        'ヴ': 'wu ',
        'ヴェ': 'wai ',
        'ヴォ': 'wo ',
        'ツァ': 'ca ',
        'ティ': 'ti ',
        'ファ': 'fa ',
        'フィ': 'fei ',
        'ウィ': 'wei ',
        'ディ': 'di ',
        'トゥ': 'tu ',
        'ドゥ': 'du ',
        'ウェ': 'wai ',
        'シェ': 'xie ',
        'チェ': 'qie ',
        'ツェ': 'cai ',
        'ジェ': 'jie ',
        'ウォ': 'wo ',
        'ツォ': 'cao ',
        'フォ': 'fo ',
        'ア': 'a ',
        'イ': 'yi ',
        'ウ': 'wu ',
        'エ': 'ei ',
        'オ': 'o ',
        'カ': 'ka ',
        'キ': 'ki ',
        'ク': 'ku ',
        'ケ': 'kai ',
        'コ': 'kou ',
        'サ': 'sa ',
        'シ': 'xi ',
        'ス': 'si ',
        'セ': 'sai ',
        'ソ': 'sao ',
        'タ': 'ta ',
        'チ': 'qi ',
        'ツ': 'ci ',
        'テ': 'tie ',
        'ト': 'tao ',
        'ナ': 'na ',
        'ニ': 'ni ',
        'ヌ': 'nu ',
        'ネ': 'nai ',
        'ノ': 'nao ',
        'ハ': 'ha ',
        'ヒ': 'hei ',
        'フ': 'fu ',
        'ヘ': 'hai ',
        'ホ': 'hao ',
        'マ': 'ma ',
        'ミ': 'mi ',
        'ム': 'mu ',
        'メ': 'mai ',
        'モ': 'mao ',
        'ヤ': 'ya ',
        'ユ': 'you ',
        'ヨ': 'yo ',
        'ラ': 'la ',
        'リ': 'li ',
        'ル': 'lu ',
        'レ': 'lai ',
        'ロ': 'lo ',
        'ワ': 'wa ',
        'ヰ': 'wei ',
        'ヱ': 'wai ',
        'ヲ': 'o ',
        'ン': 'en ',
        'ガ': 'ga ',
        'ギ': 'gei ',
        'グ': 'gu ',
        'ゲ': 'gai ',
        'ゴ': 'gao ',
        'ザ': 'za ',
        'ジ': 'ji ',
        'ズ': 'zi ',
        'ゼ': 'zai ',
        'ゾ': 'zao ',
        'ダ': 'da ',
        'ヂ': 'ji ',
        'ヅ': 'zi ',
        'デ': 'die ',
        'ド': 'dao ',
        'バ': 'ba ',
        'ビ': 'bi ',
        'ブ': 'bu ',
        'ベ': 'bai ',
        'ボ': 'bao ',
        'パ': 'pa ',
        'ピ': 'pi ',
        'プ': 'pu ',
        'ペ': 'pai ',
        'ポ': 'pao ',
        'ァ': 'a ',
        'ィ': 'yi ',
        'ゥ': 'wu ',
        'ェ': 'ei ',
        'ォ': 'o ',
        'ャ': 'ya ',
        'ュ': 'you ',
        'ョ': 'yo ',
        'ヮ': 'wa ',
        'ー': '~ '
    }

    for i, j in mapping.items():
        input_text = input_text.replace(i, j)
    return input_text

def to_katakana(input_text):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "K") 
    kakasi.setMode("J", "K")  
    kakasi.setMode("K", "K")  
    kakasi.setMode("r", "Hepburn")  
    converter = kakasi.getConverter()
    result = converter.do(input_text)
    result = result.replace('ッ', 'ー')
    return result

def jp2py(japanese_text):
    katakana_text = to_katakana(japanese_text)
    pinyin = sol(katakana_text)
    # print(katakana_text)
    # print(pinyin)
    pinyin = pinyin.split()
    """
    import json
    with open('filter_py2hz.json', "r") as f:
        dict = json.load(f)
    # for i in pinyin:
    # if i in dict:
    """
    return pinyin

print(jp2py("夢ならばどれほどよかったでしょう"))

"""
夢ならばどれほどよかったでしょう
未だにあなたのことを夢にみる
忘れた物を取りに帰るように
古びた思い出の埃を払う
戻らない幸せがあることを
最後にあなたが教えてくれた
言えずに隠してた昏い過去も
あなたがいなきゃ永遠に昏いまま
きっともうこれ以上傷つくことなど
ありはしないとわかっている
あの日の悲しみさえ あの日の苦しみさえ
そのすべてを愛してた あなたとともに
胸に残り離れない 苦いレモンの匂い
雨が降り止むまでは帰れない
今でもあなたはわたしの光
暗闇であなたの背をなぞった
その輪郭を鮮明に覚えている
受け止めきれないものと出会うたび
溢れてやまないのは涙だけ
何をしていたの 何を見ていたの
わたしの知らない横顔で
どこかであなたが今
わたしと同じ様な
涙にくれ淋しさの中にいるなら
わたしのことなどどうか忘れてください
そんなことを心から願うほどに
今でもあなたはわたしの光
自分が思うより 恋をしていたあなたに
あれから思うように 息ができない
あんなに側にいたのに まるで嘘みたい
とても忘れられない それだけが確か
あの日の悲しみさえ あの日の苦しみさえ
そのすべてを愛してた あなたとともに
胸に残り離れない苦いレモンの匂い
雨が降り止むまでは帰れない
切り分けた果実の片方の様に
今でもあなたはわたしの光
"""




