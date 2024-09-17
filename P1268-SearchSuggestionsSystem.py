class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        def buildTrie(products):
            self.root = {}
            for product in products:
                node = self.root
                for c in product + "$":
                    node = node.setdefault(c, {})
                    node.setdefault("<words>", []).append(product)
        products.sort()
        buildTrie(products)

        def findMatches(word):
            ans = []
            node = self.root
            for c in word:
                node = node.get(c, {})
                ans.append(node.get("<words>", [])[:3])
            return ans

        return findMatches(searchWord)
