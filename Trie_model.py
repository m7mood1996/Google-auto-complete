import time
import sys
class Trie_node:

    def __init__(self):
        self.ch = None
        self.childrens = []
        # self.apperance = []

    def get_next_node(self, ch):
        for node in self.childrens:
            if ch == node.ch:
                return node
        
        return None


class Auto_complation_trie:

    def __init__(self, files_path):
        self.hash_map = {}
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.hash_map[char] = self.getNode()
            self.hash_map[char].ch = char
        self.files_path = files_path

    def getNode(self):
        return Trie_node()
        
    def search(self, key : str): 
        """
        DFS search for a phrase in the trie tree
        """
        if len(key) == 0:
            return None

        node = self.hash_map[key[0]] 
        length = len(key)
        for level in range(1, length):
            child = node.get_next_node(key[level])
            if child == None:
                return node, level
            node = child
        return node, level

    def insert(self, prefix):
        pCrawl, index = self.search(prefix)
        for i in range(index, len(prefix)):
            node = self.getNode()
            node.ch = prefix[i]
            pCrawl.childrens.append(node)
            pCrawl = node
        
            
        # newList = Auto_complation_trie.get_updated_list(pCrawl.apperance, (file_id, line, orignal_sentince, score) )
        # pCrawl.apperance = newList
    

    def fill_model(self): 

        file_id = 0
        for path in self.files_path:
            print("File id: ", file_id)
            start = time.time()
            with open(path, encoding='utf-8') as file:
                i = 0
                lines = file.readlines()
                for line in lines:
                    # read all the file at once
                    if not Auto_complation_trie.ligal(line):
                        continue
                    if not line:
                        break
                    #start = time.time()
                    self.analyze_sentince(line, file_id, i)
                    
                    i += 1
            end = time.time()
            print("file: " , file_id , ", with size of: " ,sys.getsizeof(lines) , ", time takes: " , end - start )

            file_id += 1


    def analyze_sentince(self, sentince, file_id, line):
        sentince = sentince.lower()
        orignal_sentince = sentince
        while sentince:
            
            self.insert(sentince) 
            sentince = sentince[1:]


    @staticmethod
    def ligal(line):
        count = 0
        for char in line[:len(line) - 1]:
            if char in " ,./'][/{\}-=+-`~<>:;_":
                count += 1
        return not count == len(line) - 1

  
    

    def auto_complation(self, key : str):
        node = self.hash_map.get(key[0])
        if not node:
            return []
        length = len(key)
        for level in range(length):

            node = node.get_next_node(key[level]) 
            if not node: 
                return []
        
        candidates = []

        for child in node.childrens:
            candidates += Auto_complation_trie.find_all_candidates(child, key)

        return candidates

    def find_all_candidates(node : Trie_node, sentince : str):
        sentince_candidate = []
        if len(node.childrens) == 0:
            sentince += node.ch
            return [sentince]
        else:
            sentince += node.ch
            for child in node.childrens:
                sentince_candidate += Auto_complation_trie.find_all_candidates(child, sentince)
            return sentince_candidate



