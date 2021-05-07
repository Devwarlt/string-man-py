def text_out(text: str, words: list) -> str:
    for index in range(len(words)):
        text = ("#" * len(words[index])).join(text.split(words[index]))
    return text
