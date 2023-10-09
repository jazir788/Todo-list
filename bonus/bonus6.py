contents = ["The carrots were reportedly sliced",
            "The number of items are correlated",
            "Content for presentation"
            ]

filenames = ["doc.txt","report.txt","presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)

