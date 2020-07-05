"""11. Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length?"""

def main():
    file_name = input("Enter the file name :")
    ext_name = file_name.split(".")[1]
    name_without_ext = file_name.split(".")[0]

    print("The name without extension is: "+name_without_ext)
    print("The extension is: " + ext_name)

main()