import utils
import time
from Trie_model import Auto_complation_trie

from view import print_results
from search_model import search

if __name__ == '__main__':
    files_path = utils.get_files_path('/Users/mahmoodnael/Desktop/ExcellenTeamCourse/Google2/data')
    start = time.time()
    a = Auto_complation_trie(files_path)
    a.fill_model()
    end = time.time()
    print("time takes = {}, All set what is your input".format(end - start))
    while True:
        user_input = input()
        result = search(a,user_input)
        print_results(result,user_input)

