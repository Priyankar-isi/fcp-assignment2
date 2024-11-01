import random
content = open("fortune.txt").read()
print(random.choice(content.split("%")))
