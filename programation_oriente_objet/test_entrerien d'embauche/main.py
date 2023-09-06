# hello_str = "salut"
#
#
# def reverse_string(string):
#     reverse_str = string[::-1]
#     return reverse_str
#
#
#
# print(reverse_string(hello_str))
#

s = "Un chasseur sachant chasser sait chasser sans son chien"


def get_min_and_max_word(sentence):
    words_list = (sentence.split(" "))
    min_word = min(words_list, key=len)
    max_word = max(words_list, key=len)
    return min_word, max_word


def get_min_and_max_word_sorted(sentence):
    words_list = sorted((sentence.split(" ")))
    min_word_sorted = min(words_list, key=len)
    max_word_sorted = max(words_list, key=len)
    return min_word_sorted, max_word_sorted


min_word, max_word = get_min_and_max_word(s)
min_word_sorted, max_word_sorted = get_min_and_max_word_sorted(s)
print(f"Le mot le plus petit : {min_word}")
print(f"Le mot le plus long : {max_word}")

print(f"Le mot le plus petit : {min_word_sorted}")
print(f"Le mot le plus long : {max_word_sorted}")
