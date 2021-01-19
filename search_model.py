
from Trie_model import Auto_complation_trie

def regular_search(model : Auto_complation_trie, user_input):
    first_result = model.auto_complation(user_input.lower())
    
    return [(user_input, r, len(user_input) * 2) for r in first_result]


def change_char_search(model : Auto_complation_trie, user_input):
    alphabet = 'a'
    orignal_input = user_input
    score = len(user_input) * 2
    result = []
    for i in range(len(orignal_input)):
        for k in range(ord('z') - ord('a')):
            user_input = orignal_input[0:i] + chr(ord(alphabet) + k) + orignal_input[i+1:]
            search_result = model.auto_complation(user_input)
            if i == 0:
                score -= 5
            elif i == 1:
                score -= 4
            elif i == 2:
                score -= 3
            elif i == 3:
                score -= 2
            else:
                score -= 1
            [result.append((user_input, r, score)) for r in search_result]
            score = len(orignal_input) * 2
    return result

def delete_char_search(model : Auto_complation_trie, user_input):
    # delete one char
    orignal_user_input = user_input
    result = []
    score = len(user_input) * 2
    for i in range(len(orignal_user_input)):
        user_input = user_input[0:i] + user_input[i+1: len(orignal_user_input)]
        search_result = model.auto_complation(user_input)
        if i == 0:
            score -= 10
        elif i == 1:
            score -= 8
        elif i == 2:
            score -= 6
        elif i == 3:
            score -= 4
        else:
            score -= 2

        [result.append((user_input, r, score)) for r in search_result]
        score = len(orignal_user_input) * 2
    return result

def search(model : Auto_complation_trie, user_input):
    result = []
    result += regular_search(model, user_input)
    result += change_char_search(model, user_input)
    result += delete_char_search(model, user_input)

    return sorted(result, key=lambda tup: tup[2],reverse=True)[:5]
