message_file = open('alice.txt','r')
line_counter = 0
words_to_change = {"Alice":"Nope", "ALICE":"NOPE",
"she":"he","She":"He","SHE":"HE","Her":"Him","her":"him","HER":"HIM",
"Lewis":"Preston","Carroll":"Getz"}
from time import sleep

for line in message_file:
    for word in words_to_change:
      line = line.replace(word, words_to_change[word])
    print(line, end="")
    line_counter = line_counter + 1
    if line_counter%20 == 0:
      input()
message_file.close()
