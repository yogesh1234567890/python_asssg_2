"""3. Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text."""

paragraph = str(input("Enter a paragraph: "))
word_list=paragraph.split(' ')
anagram_list = []
for word_1 in word_list:
    for word_2 in word_list:
        if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
            anagram_list.append(word_1)

print(anagram_list)