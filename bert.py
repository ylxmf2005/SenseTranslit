import torch
import math
import jieba
from transformers import BertTokenizer, BertForMaskedLM
import torch.nn.functional as F

tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
model = BertForMaskedLM.from_pretrained('bert-base-chinese')
model.eval()

def get_ppl(sentence, temperature=1.0):
    sentence = list(jieba.cut(sentence))
    x = " ".join(sentence)

    inputs = tokenizer(x, return_tensors="pt")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    mask_id = tokenizer.mask_token_id
    origin_ids = input_ids[0][1:-1].tolist() 
    length = len(origin_ids)

    all_probability = []

    for i in range(length):
        tmp_input_ids = input_ids.clone()
        tmp_input_ids[0, i + 1] = mask_id
        outputs = model(tmp_input_ids, attention_mask=attention_mask).logits
        outputs = F.softmax(outputs / temperature, dim=-1)
        word_prob = outputs[0, i + 1, origin_ids[i]].item()
        all_probability.append(word_prob)

    l_score = sum(math.log(p, 2) for p in all_probability) / len(all_probability)
    ppl = math.pow(2, -l_score)
    return ppl