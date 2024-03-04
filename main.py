def main():
    def get_num_words(text):
        words = text.split()
        return len(words)

    def get_book_text(path):
        with open(path) as f:
            return f.read()

    def get_num_letters(text):
        letter_dict = {}

        for letter in text:
            lower = letter.lower()
            if lower in letter_dict:
                letter_dict[lower] += 1
            else:
                letter_dict[lower] = 1

        return letter_dict

    def sort_on(book):
        return book["num"]

    def aggregate_data(book):
        letters = []

        for letter in book:
            if letter.isalpha():
                letters.append({"letter": letter, "num": book[letter]})

        letters.sort(reverse=True, key=sort_on)

        for letter in letters:
            print(f"The {letter['letter']} character was found {letter['num']} times")

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    aggregate_data(get_num_letters(text))
    print("--- End report ---")


main()
