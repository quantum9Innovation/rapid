"""
File docstring at the top
Multi-line docstring: distinguish paragraphs by line breaks

This is a new paragraph
If you have some really long text to put in a docstring that goes over 110 characters,
create line breaks after a sentence, comma, phrase, word, and character in the order shown.
First ==> most prefereable
Last ==> least preferable

Stick to GitHub-flavored Markdown but avoid :emoji: or <tags>
Distinguish code blocks with:
>>> print('Something')
Distinguish large code blocks with a new line like:

>>> print('Large code block')
>>> 'Large code block'

>>> print(2+2)
>>> 4

Write terminal code with
$ echo 'hello world'

Any project-wide headers should be in all caps like:

STRUCTURE:
NOTES:
CONTRIBUTIONS:
etc.
"""


class CamelCase_ABBR_Capitalized(object):
    """One line docstring"""
    
    def __init__(self, parameter_with_underscores, nonrequired_param=None, *packed_params):
        
        pass

    def camelCase_ABBR_Capitalized(
        param1,
        param2,
        param3,
        param4,
        too_many_params_to_fit_120_chars,
        etc
    ):

        pass



def camelCase_ABBR_Capitalized():

    pass


def anotherFunction():

    pass



lowercase_with_underscores_ABBR = None
very_long_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 
                   9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 
                   2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9]
                   # comment on long array
SameCaseAsClass = {
    "property": None,
    "next property": None,
    "last property": None
}

different_variable_group = None
x = 2
expression = (5 * x) ** (1 - x) + abs(x / (1 + x))  # spaces everywhere except inside parentheses
"""
Long comment on some section of code
Follow docstring format from top of file
"""


for i in range(10):  # short for loop
    pass

for i in range(10):  # long for loop
    
    e = 3
    y = 2 * e  # follow mathematical convention--coefficient before variable



if x: pass  # short if statement
if e: pass  # another short if statement

if x + e:  # a long if statement

    z = x + e
    y = x - e



InstanceOfClassUseSameClassCaps = CamelCase_ABBR_Capitalized
method_of_class_use_same_var_caps = InstanceOfClassUseSameClassCaps.camelCase_ABBR_Capitalized(
    3,
    1,
    4,
    1,
    5,
    9,  # comma for last element optional
)  # this is what you do when you call a function with a lot of arguments



long_variable_name1 = 3
long_variable_name2 = 1
long_variable_name3 = 4
new_expression = long_variable_name1 \
                 + long_variable_name2 \
                 - long_variable_name3 \



_prefix_hidden_things_with_underscores = 'hidden'
__metadata__ = 'also hidden'  # metadata definition
#                               ^ bad comment; don't do this (it's obvious)
confusing_variable = '23rnjs23'  # key for API
#                                  ^ good comment; do this

if _prefix_hidden_things_with_underscores is not confusing_variable: pass
# Use `foo is not` *not* `not foo is`



"""
Copyright, legal, and other information about this file goes here.
Use whatever formatting scheme you like.
"""

# newline at end of file optional
