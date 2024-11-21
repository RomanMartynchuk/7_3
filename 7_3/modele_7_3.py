class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for i in files:
            self.file_names.append(i)
        #print(self.file_names)

    def get_all_words (self):
        all_words = {}
        words = {}
        for text in self.file_names:
            with open(text) as file:
                text_in_file = []
                for line in file:
                    extract = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in extract:
                        line = line.replace(symbol, '')
                    text_in_file.extend(line.lower().split())
                words[text] = text_in_file
        all_words.update(words)
        return all_words

    def find(self, word):
        all_words = WordsFinder.get_all_words(self)
        position = {}

        for key in all_words:
            number = []
            for item in all_words[key]:
                if item != word.lower():
                    number.append(item)
                elif item == word.lower():
                    number.append(item)
                    break
            position[key] = (len(number))
        return position

    def count(self, word):
        all_words = WordsFinder.get_all_words(self)
        position = {}
        for key in all_words:
            number = []
            for item in all_words[key]:
                if item == word.lower():
                    number.append(item)
                position[key] = (len(number))
        return position


finder2 = WordsFinder('test_file.txt', 'test_file2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))