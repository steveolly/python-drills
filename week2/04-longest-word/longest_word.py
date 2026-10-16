def longest_word(sentence):
    sentence = sentence.strip().split()
    if not len(sentence):
        return ""
    new_sentence = []
    for word in sentence:
        rerun = True
        while rerun:
            if not len(word):
                rerun = True
                break
            if word[0].isalpha() and word[-1].isalpha():
                rerun = False
            elif not word[0].isalpha():
                word = word[1:]
            elif not word[-1].isalpha():
                word = word[:-1]
        if len(word):
            new_sentence.append(word)
    if not len(new_sentence):
        return ""
    count = 0
    Highest_word = None
    for word in new_sentence:
        if len(word) > count:
            count = len(word)
            Highest_word = word
    return Highest_word

# bonus


def longest_words(sentence):
    sentence = sentence.strip().split()
    if not len(sentence):
        return []
    new_sentence = []
    for word in sentence:
        clean_word = ""
        length = len(word)
        for i in range(length):
            if not ("a" <= word[i] <= "z" or "A" <= word[i] <= "Z"):
                if not (i-1 < 0) and not ("a" <= word[i-1] <= "z" or "A" <= word[i-1] <= "Z"):
                    continue
                elif i+1 != length and ("a" <= word[i+1] <= "z" or "A" <= word[i+1] <= "Z"):
                    clean_word += word[i]
                else:
                    continue
            else:
                clean_word += word[i]
        if len(clean_word):
            new_sentence.append(clean_word)

    if not len(new_sentence):
        return []
    word_dic = {}
    count = 0
    highest = 0
    for word in new_sentence:
        count = len(word)
        if word not in word_dic:
            word_dic[word] = count
        if count > highest:
            highest = count

    result = []
    for key, value in word_dic.items():
        if highest == value:
            result.append(key)

    return result
