# Transliteration-to-Mandarin

## Table of Contents

- [Transliteration-to-Mandarin](#transliteration-to-mandarin)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Principle](#principle)
  - [Installation](#installation)
  - [Usage](#usage)
  - [To-Do](#to-do)

## Introduction

The Transliteration-to-Mandarin tool is adept at transliterating text from various languages into Mandarin, focusing on phonetic similarity and meaningful interpretations in Mandarin. This tool finds its utility in language learning, cultural studies, and as a practical demonstration of linguistic transliteration.

## Features

- **Phonetic Accuracy** 

  Transforms texts from multiple languages into Mandarin, ensuring a close match to the original sounds.

- **Meaningful Mandarin Transliterations** 

  Produces Mandarin transliterations that are not just phonetically similar, but also carry contextual meanings.

- **Advanced Transliteration Techniques**
  
  - Retrieval-Augmented Generation
  - Input Method-Based Simulation
  - BFS Based on Perplexity Log Average
  - Character-by-Character Generation with LLM



## Principle



## Installation

```python
git clone https://github.com/ylxmf2005/Transliteration-to-Mandarin
pip install -r requirements.txt
```



## Usage

Put the content for transliteration into input.txt first, and then run:

```python
python3 main.py
```

Check the result in output.txt.



## To-Do

- Add GUI
- Add support for French, English, and Cantonese.
- Add the method of using GPT-4 for RAG.
- Try the method of Text-to-Audio-to-Text.
- Optimized the generation of explanations
