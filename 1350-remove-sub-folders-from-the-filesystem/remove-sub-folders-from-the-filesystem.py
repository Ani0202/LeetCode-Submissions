class Trie:
    def __init__(self):
        self.nodes = dict()
        self.isLeaf = False

    def isSubFolder(self, folder):
        node = self
        isSubFolder = False
        for path in folder:
            if path not in node.nodes:
                node.nodes[path] = Trie()

            node = node.nodes[path]
            if node.isLeaf:
                isSubFolder = True

        node.isLeaf = True
        return isSubFolder


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folderList = [i.split("/") for i in folder]
        ans = []
        trie = Trie()
        for folderPath in sorted(folderList, key=lambda x: len(x)):
            if not trie.isSubFolder(folderPath):
                ans.append("/".join(folderPath))

        return ans
