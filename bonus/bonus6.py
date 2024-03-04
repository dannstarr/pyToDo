#Create a program to create the 3 files, and in them write the contents

contents = ["All the carrots are to be cut into batons",
            "The carrots were reportedly sliced",
            "The slicing process was well executed"]

filenames = ["doc.txt", "report.txt", "execution.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)