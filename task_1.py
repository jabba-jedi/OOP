#!/usr/bin/env python3

class Nobody:
    def __init__(self, name):
        if name == "Nobody":
            self.name = name
        else:
            self.name = "I'm Nobody, not " + str(name)

    def __str__(self):
        return f"I'm an object of class Nobody. My name is {self.name}"

n1 = Nobody("Nobody")
n2 = Nobody("Steven")

print(n1.name)
print(n2.name)