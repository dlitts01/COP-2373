
import re


# This function separates a paragraph into sentences.
def find_sentences(paragraph):
    pattern = r'[A-Za-z0-9].*?[.!?](?=\s+[A-Za-z0-9]|$)'
    sentences = re.findall(pattern, paragraph, re.DOTALL)

    return sentences


# This function displays each sentence and the total count.
def display_sentences(sentences):
    print("\nSentences in the paragraph:\n")

    for sentence in sentences:
        print(sentence.strip())

    print("\nTotal number of sentences:", len(sentences))


# This function gets the paragraph from the user.
def main():
    paragraph = input("Enter a paragraph: ")

    sentences = find_sentences(paragraph)

    display_sentences(sentences)


# Start the program.
if __name__ == "__main__":
    main()
