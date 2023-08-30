"""
  Lesson 5: ex4.py
"""

# 1. Write a function get_index() that returns the index of
#    a character in a string


def get_index(word: str, char: str) -> int:
    for index, letter in enumerate(word):
        if (letter == char):
            return index

    return 0


print(get_index("redhat", "s"))
# print("redhat".index("s"))

# 2. Write a function shout() that returns each word
#  capitalized with "!" and on it's own line.


def shout(sentence: str) -> str:
    ret_words: str = ""
    for word in sentence.split(" "):
        ret_words += f"{word.upper()}! "
    return ret_words


print(shout("aaa asdf"))

# 3. Write a function extract_longer() that extracts
#    words longer or equal to n-characters and return a list,
#    otherwise return False


def extract_longer(n: int, sentence: str) -> list | bool:
    result: list[str] = []
    for word in sentence.split(" "):
        if len(sentence.split(" ")) >= n:
            result.append(word)
    return result if result else False


print(extract_longer(2, "How is it going?"))
print(extract_longer(5, "How is it going?"))
