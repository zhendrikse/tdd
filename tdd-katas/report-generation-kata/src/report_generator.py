class ReportGenerator:
    def get_report(path):
        """
        Creates a report of the file specified as argument.
    
        :param path: path to file from which the report should be created (string)
        :return: the report (string)
        """
        data = _read_file(path)
        missing_count = data[0]
        numbers = data[1]
        words = data[2]
        report = _make_report(missing_count, numbers, words)
        return report
    
    
    def _read_file(path):
        """
        Reads and returns the data from the file specified as argument.
    
        :param path: path to the file to be read.
        :return: a tuple containing
        1. the number of empty lines (int)
        2. numeric values (list of floats)
        3. non-numeric values (list of strings)
        """
        data_file = open(path)
        lines = data_file.readlines()
        line_count = len(lines)
        idx = 0
        empty_lines = 0
        words = []
        numbers = []
        while idx < line_count:
            line = lines[idx]
            line = line.strip()
            if line == "":
                empty_lines = empty_lines + 1
            else:
                is_number = False
                try:
                    number = float(line)
                    is_number = True
                except Exception:
                    pass
    
                if is_number:
                    numbers.append(number)
                else:
                    words.append(line)
            idx = idx + 1
        data_file.close()
    
        return empty_lines, numbers, words
    
    
    def _make_report(missing_values, numbers, words):
        """
        Creates and a report based on data given as arguments.
    
        :param missing_values: number of empty lines (int)
        :param numbers: numeric values (list of floats)
        :param words: non numeric values (list of strings)
        :return: the generated report (string)
        """
        max_value = _get_max_value(numbers)
        lower_case_words = _words_to_lowercase(words)
        most_common_info = _get_most_common_words(lower_case_words)
        most_common_words = most_common_info[0]
        most_common_count = most_common_info[1]
    
        most_common_str = ""
        for idx in range(len(most_common_words)):
            most_common_str += most_common_words[idx] + ", "
        # remove the last comma and space
        most_common_str = most_common_str[0 : len(most_common_str) - 2]
    
        report = (
            "missing values: {}\n"
            "highest number: {}\n"
            "most common words: {}\n"
            "occurrences of most common: {}\n"
            "#####\n"
            "numbers: {}\n"
            "words: {}"
        ).format(
            missing_values,
            max_value,
            most_common_str,
            most_common_count,
            numbers,
            lower_case_words,
        )
    
        return report
    
    
    def _get_max_value(numbers):
        """
        Returns the greatest value of the list given as argument.
    
        :param numbers: numbers (list of numeric values)
        :return: greatest value of numbers, None if numbers is an empty list
        """
        max_value = None
        if len(numbers) > 0:
            max_value = numbers[0]
            for idx in range(len(numbers)):
                if numbers[idx] > max_value:
                    max_value = numbers[idx]
        return max_value
    
    
    def _words_to_lowercase(words):
        """
        :param words: words to be converted (list of strings)
        :return: lowercased words (list of strings)
        """
        lowercased = []
        for idx in range(len(words)):
            value = words[idx].lower()
            lowercased.append(value)
        return lowercased
    
    
    def _get_most_common_words(words):
        """
        Finds the most common words in a list of words.
        If there are multiple different words with the same amount of occurrences,
        they are all included in the return value sorted alphabetically.
        In addition to returning the most common words, the return value
        includes also the count of occurrences of the most common words.
    
        :param words: list of words (list of strings)
        :return: a tuple containing:
        1. most common words (list of strings)
        2. the count of occurrences of the most common words (int)
        """
        word_counts = {}
        idx = 0
        while idx < len(words):
            value = words[idx]
            if value not in word_counts.keys():
                word_counts[value] = 1
            else:
                word_counts[value] += 1
            idx = idx + 1
    
        max_count = 0
        for value in word_counts.values():
            if value > max_count:
                max_count = value
    
        most_common_words = []
        for word in word_counts.keys():
            count = word_counts[word]
            if count == max_count:
                most_common_words.append(word)
    
        most_common_words = sorted(most_common_words)
    
        return most_common_words, max_count
