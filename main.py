def count_words(text):
    return len(text.split())

def count_each_symbol(text):
    dict = {}
    lowerText = text.lower()
    for symbol in lowerText:
        if not(symbol in dict):
            dict[symbol.lower()] = 1
        else:
            dict[symbol.lower()] += 1
    return dict

def print_report(count_of_words, list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{ count_of_words } words found in the document\n")
    for dict in list:
        print(f"The '{ dict['symbol'] }' character was found { dict['number'] } times")
    print("--- End report ---")

def get_list_of_dict(dict):
    list = []
    for key in dict:
        if key.isalpha():
            list.append({
                "symbol": key,
                "number": dict[key],
            })
    return list

def sort_on(dict):
    return dict["number"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        number_of_words = count_words(file_contents)
        dict = count_each_symbol(file_contents)
        list = get_list_of_dict(dict)
        list.sort(reverse=True, key=sort_on)
        print_report(number_of_words, list)


main()
