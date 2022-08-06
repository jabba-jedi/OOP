#!/usr/bin/env python3

class Nobody:
    def __init__(self, name):
        if name == "Nobody":
            self.name = name
        else:
            self.name = "I'm Nobody, not " + str(name)

n1 = Nobody("Nobody")
n2 = Nobody("Steven")

print(n1.name)
print(n2.name)