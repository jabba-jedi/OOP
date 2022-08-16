#!/usr/bin/env python3

class Student:
    def __init__(self, first_name: str, last_name: str, group: str, \
        marks: dict(type=list, help='The student\'s marks'), **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.marks = marks

    def __str__(self):
        return f'I\'m a student. My name is {self.first_name} {self.last_name}'

    def add_mark(self, mark):
        """Add a student's mark to a list of their marks."""
        if 0 > int(mark) > 10:
            return "Invalid mark"
        else:
            self.marks.append(int(mark))

    def _get_average_mark(self):
        """Calculate the student's average grade. Takes an array of marks, \
        returns float."""
        if len(self.marks) > 0:
            return (sum(self.marks) / len(self.marks))

    usual_scholarship = 150
    extra_scholarship = 500

    def get_scholarship(self):
        if self._get_average_mark() == 5:
            return self.extra_scholarship
        else:
            return self.usual_scholarship


class Aspirant(Student):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #for key, value in kwargs.items():
        #    setattr(self, key, value)
        self.scientific_publications = kwargs['scientific_publications']

    def __str__(self):
        return f'I\'m an aspirant. My name is {self.first_name} \
{self.last_name} and I have these scientific publications: \
{", ".join(str(x) for x in self.scientific_publications)}'

    usual_scholarship = 250
    extra_scholarship = 700

severuses_works = ["Practical Magic", "Theoretical Magic"]

harry = Student(first_name="Harry", last_name="Potter", group="Gryffindor", \
    marks=[])
severus = Aspirant(first_name="Severus", last_name="Snape", group="Slytherin", \
    marks=[], scientific_publications=severuses_works)
print(harry)
print(severus)
harry.add_mark(10)
harry.add_mark(8)
severus.add_mark(5)
severus.add_mark(5)
print(harry._get_average_mark(), harry.get_scholarship())
print(severus._get_average_mark(), severus.get_scholarship())
