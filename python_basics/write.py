# Do not need to use file.close when implementing 'with'
# r:w parameters for read/write
# reverses list and write the list back to the file
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
