

from typing import List


def print_results(result : list, user_input : str):

    print("======= Suggestions =======")

    for correct_to, auto_complation, score in result:
        print("User input: ", user_input)
        print("Coricting user input to : ", correct_to)
        print("Auto complation to:", auto_complation)
        print("Score of:", score)
        print("---------------------\n")