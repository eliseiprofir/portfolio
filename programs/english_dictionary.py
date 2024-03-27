import json

def define(data, word):
    if word in data:
        return data[word]


def main():
    file = open('english_dictionary.json')
    data = json.load(file)
    word = input("Enter a word: ").lower()
    definition = define(data, word)
    if definition:
        for index, define in enumerate(definition):
            index = '–'
            print(index, define)
    else:
        print("Word was not found.")


if __name__ == "__main__":
    main()