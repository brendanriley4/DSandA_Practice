class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        dict = self.trie
        for c in word:
            if c not in dict:
                dict[c] = {}
            dict = dict[c]
        dict['.'] = '.'

    def search(self, word: str) -> bool:
        dict = self.trie
        for c in word:
            if c not in dict:
                return False
            dict = dict[c]
        return '.' in dict

    def startsWith(self, prefix: str) -> bool:
        dict = self.trie
        for c in prefix:
            if c not in dict:
                return False
            dict = dict[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)