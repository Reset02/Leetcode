class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # 將句子分割成單詞列表
        word_array = sentence.split()
        # 將字典轉換為集合，方便快速查找
        dict_set = set(dictionary)

        def shortest_root(word, dict_set):
            # Find the shortest root of the word in the dictionary
            for i in range(len(word)):
                root = word[0:i]
                if root in dict_set:
                    return root
            # There is not a corresponding root in the dictionary
            return word
        
        # Replace each word in sentence with the corresponding shortest root 替換句子中的每個單詞
        for word in range(len(word_array)):
            word_array[word] = shortest_root(word_array[word], dict_set)
        
        return " ".join(word_array)