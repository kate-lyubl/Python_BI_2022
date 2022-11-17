import re
import seaborn as sns


def extract(path_to_file, regex, output_file):
    matches = []
    with open(path_to_file) as f:
        file_content = f.readlines()
        for line in file_content:
            matches += re.findall(regex, line)
    with open(output_file, 'a') as f:
        for match in matches:
            f.write(match + '\n')


def extract_unique_words(path_to_file):
    words = []
    with open(path_to_file) as f:
        file_content = f.readlines()
        for line in file_content:
            words += re.findall(r'[a-zA-z\']+', line)
    return set(map(lambda x: x.lower(), words))


def translator(input_text):
    input_text = re.sub(r'([eyuioaEYUIOA])', r'\1k\1', input_text)
    input_text = re.sub(r'([уеыаоэяиюёУЕЫАОЭЯИЮЁ])', r'\1к\1', input_text)
    return input_text


def plot_hist(dataset):
    words_len = [len(word) for word in dataset]
    plot = sns.displot(words_len, bins=[i + 0.5 for i in range(max(words_len))])
    plot.savefig("Word's length distribution")


if __name__ == '__main__':
    # Task 1
    extract(path_to_file="references", regex=r'\b(ftp[\w\d/._#]+)[\s;]', output_file="reference_links")

    # Task 2
    extract(path_to_file="2430AD", regex=r'\d+[.,]?\d+', output_file="2430AD_numbers")

    # Task 3
    extract(path_to_file="2430AD", regex=r'\w*[Aa]+\w*', output_file="2430AD_words_with_a")

    # Task 4
    extract(path_to_file="2430AD", regex=r'[A-Z][\w\s,]*!', output_file="2430AD_exclamation")

    # Task 5
    plot_hist(extract_unique_words(path_to_file="2430AD"))

    # Task 6
    print(translator("Сделайте функцию-переводчик с русского на кирпичный язык"))

