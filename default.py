

def my_function(string1, string2="goodbye"):
    return string1 + " " + string2


print(my_function("hello", "world")) # prints "hello world"
print(my_function("hello"))          # prints "hello goodbye"


def positional_and_default(p1, p2, p3, p4="a", p5=1, p6=None):
    # do something
    pass


def say_hi_or_dont(to_say="hi"):
    return to_say

def many_params(p1=1, p2=2, p3=3, p4=4):
    return p1 + p2 + p3 + p4


# def bad_mix(p1="first", p2, p3):
#     print(p1, p2, p3)

print(many_params())
print(many_params(2, 4, 6, 8))
print(many_params(p4=10))
print(many_params(30, p3=40))
print(many_params(p3=3, p1=6))


def print_word_list(word_list=["dog", "cat", "goat"]):
    print(word_list)


print_word_list()
print_word_list()


def print_word_list_add_bird(word_list=["dog", "cat", "goat"]):
    print(word_list)
    word_list.append("bird") # should have no effect, right?


print_word_list_add_bird()
print_word_list_add_bird()
print_word_list_add_bird()
print_word_list_add_bird()


class Person:

    def __init__(self, fn="Jane", ln="Doe"):
        self.firstName = fn
        self.lastName = ln

    def full_name(self):
        return self.firstName + " " + self.lastName


people = [
    Person(),
    Person("Sam", "Samuelson"),
    Person(ln="Jacobs"),
    Person("John")
]

for p in people:
    print(p.full_name())



class ClubMember:

    def __init__(self, fn="Jane", ln="Doe", mem_id=-1):
        self.firstName = fn
        self.lastName = ln
        self.member_id = mem_id
        self.is_member = (mem_id != -1) 

    def member_status(self):
        if (self.is_member):
            status = " is "
        else:
            status = " is not "
            
        return self.firstName + " " + self.lastName + status + "a member"

members = [
    ClubMember(),
    ClubMember("Sam", "Samuelson", 1234),
    ClubMember(ln="Jacobs"),
    ClubMember("John", mem_id=6666)
]

for m in members:
    print(m.member_status())