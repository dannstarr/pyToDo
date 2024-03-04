# List comprehension example
# Take a list of filenames, and use a list comprehension to transform the list

filenames = ["1.doc", "1.report", "1.presentation"]
 # Replace the . with a - and add .txt to the end of each file name
 
new_filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]
print(new_filenames)