class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = text.replace(',', ' ').replace('.', ' ').replace('=', ' ').replace('!', ' ').replace('?',
                                                                                                            ' ').replace(
                    ';', ' ').replace(':', ' ').replace('-', ' ')
                words = text.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        result = {}

        for file_name, words in self.get_all_words().items():
            if word in words:
                position = words.index(word) + 1
                result[file_name] = position

        return result

    def count(self, word):
        word = word.lower()
        result = {}

        for file_name, words in self.get_all_words().items():
            count_word = words.count(word)
            if count_word > 0:
                result[file_name] = count_word

        return result

finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))