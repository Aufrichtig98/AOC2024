import aoc_helper
from collections import defaultdict
from copy import deepcopy


def letter_dfs_old(current_word, possible_words, cached_results, result):

    if current_word in cached_results:
        return cached_results[current_word]

    for letter in possible_words[current_word[0]]:
        if len(letter) > len(current_word):
            continue
        if len(letter) == len(current_word) and letter == current_word:
            if current_word not in cached_results:
                cached_results[current_word] = 1
            else:
                cached_results[current_word] += 1
            return cached_results[current_word]
        if letter == current_word[:len(letter)]:
            tmp = letter_dfs(current_word[len(letter):], possible_words, cached_results, result)
            result += tmp
        else:
            continue

    cached_results[current_word] = result
    return result

def letter_dfs(current_word, possible_words, cached_results, result):

    if current_word in cached_results:
        return cached_results[current_word]

    for letter in possible_words[current_word[0]]:
        if len(letter) > len(current_word):
            continue
        if len(letter) == len(current_word) and letter == current_word:
            if current_word not in cached_results:
                cached_results[current_word] = 1
            result += 1
            continue
        if letter == current_word[:len(letter)]:
            tmp = letter_dfs(current_word[len(letter):], possible_words, cached_results, result)
            result += tmp
        else:
            continue

    cached_results[current_word] = result
    return result


def part_one():
    def letter_dfs(current_word, possible_words, cached_results):

        if current_word in cached_results:
            return cached_results[current_word]

        for letter in possible_words[current_word[0]]:
            if len(letter) > len(current_word):
                continue
            if len(letter) == len(current_word) and letter == current_word:
                cached_results[current_word] = True
                return True
            if letter == current_word[:len(letter)]:
                if letter_dfs(current_word[len(letter):], possible_words, cached_results):
                    cached_results[current_word] = True
                    return True
                else:
                    cached_results[current_word[len(letter):]] = False
            else:
                continue

    if __name__ == '__main__':
        requests = list()
        start_letters = defaultdict(list)

        with open("test.txt", "rt") as myfile:
            switch = False
            for line in myfile:
                if line == "\n":
                    switch = True
                    continue
                if not switch:
                    for i in line.strip("\n").strip(", ").split(", "):
                        start_letters[i[0]].append(i)
                else:
                    requests.append(line.strip("\n"))

        cached_results = dict()

        result = 0
        for i in requests:
            print(i)
            start_letters_cp = deepcopy(start_letters)
            for val in start_letters.values():
                for element in val:
                    if element not in i:
                        start_letters_cp[element[0]].remove(element)
            if letter_dfs(i, start_letters_cp, cached_results):
                result += 1
        print(result)


if __name__ == '__main__':
    requests = list()
    start_letters = defaultdict(list)

    with open("input.txt", "rt") as myfile:
        switch = False
        for line in myfile:
            if line == "\n":
                switch = True
                continue
            if not switch:
                for i in line.strip("\n").strip(", ").split(", "):
                    start_letters[i[0]].append(i)
            else:
                requests.append(line.strip("\n"))

    cached_results = dict()

    result = 0
    for i in requests:
        start_letters_cp = deepcopy(start_letters)
        for val in start_letters.values():
            for element in val:
                if element not in i:
                    start_letters_cp[element[0]].remove(element)
        cached_results = dict()
        letter_dfs(i, start_letters_cp, cached_results, 0)
        if i in cached_results:
            result += cached_results[i]
            print(i, cached_results[i])
        else: print(i,0)

    print(result)

