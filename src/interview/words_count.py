class WordSorter:
    """An object to count and sort words in a document.

    Create a class that ingests a document containing words separated by spaces. Then
    create two methods, one to get a count of each word, and one to return the top n
    words with the highest frequency of occurrence.
    """

    def __init__(self) -> None:
        self.words_dict = {}

    def process_document(self, doc: str) -> None:
        words = doc.split(" ")
        for word in words:
            if word in self.words_dict:
                self.words_dict[word] += 1
            else:
                self.words_dict[word] = 1

    def get_top_n_words(self, n: int):
        word_tuples = [(k, v) for k, v in self.words_dict.items()]
        words_desc = sorted(word_tuples, key=lambda x: x[1], reverse=True)
        return words_desc[:n]


if __name__ == "__main__":
    word_sorter = WordSorter()
    word_sorter.process_document("test test one two two three three three")
    print(word_sorter.get_top_n_words(3))
