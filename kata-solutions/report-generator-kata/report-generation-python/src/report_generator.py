from functools import reduce


class FileStatistics:
    def __init__(self, lines):
        self._empty_lines = 0
        self._numbers = []
        self._words = []

        for line in lines:
            line = line.strip()
            if line == "":
                self._empty_lines += 1
            elif self._is_number(line):
                self._numbers.append(float(line))
            else:
                self._words.append(line)

    def _is_number(self, line):
        try:
            float(line)
            return True
        except Exception:
            return False

    def _word_frequencies(self):
        word_counts = {}
        for word in self.lower_case_words():
            word_counts[word] = 1 if word not in word_counts.keys(
            ) else word_counts[word] + 1
        return word_counts

    def lower_case_words(self):
        return [word.lower() for word in self._words]

    def word_frequencies_max(self):
        word_counts = self._word_frequencies()
        return 0 if len(word_counts.items()) == 0 else reduce(max, word_counts.values())

    def most_common_words(self):
        most_common_words = []
        for item in self._word_frequencies().items():
            count = item[1]
            if count == self.word_frequencies_max():
                most_common_words.append(item[0])

        return sorted(most_common_words)

    def max_value(self):
        return None if len(self._numbers) == 0 else reduce(max, self._numbers)


class FileReader:
    def read_file(self, path):
        with open(path) as data_file:
            return data_file.readlines()


class ReportGenerator:
    def get_report(self, stats):
        most_common_str = "".join(
            word + ", " for word in stats.most_common_words())
        # remove the last comma and space
        common_words_as_string = most_common_str[0: len(most_common_str) - 2]

        return (
            f"missing values: {stats._empty_lines}\n"
            f"highest number: {stats.max_value()}\n"
            f"most common words: {common_words_as_string}\n"
            f"occurrences of most common: {stats.word_frequencies_max()}\n"
            f"#####\n"
            f"numbers: {stats._numbers}\n"
            f"words: {stats.lower_case_words()}"
        )
