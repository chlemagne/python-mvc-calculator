""" Main entry-point.
"""

from calculator.commands import *
from calculator.window import Window
from calculator.number_builder import NumberBuilder
from calculator.arithmetic_unit import ArithmeticUnit
from calculator.symbol import CalculatorSymbol as Char
from calculator.equation_builder import EquationBuilder

window = Window()
window.create_display()
window.get_display().draw()

# create command dependencies
alu = ArithmeticUnit()
num_builder = NumberBuilder()
eq_builder = EquationBuilder()

# create commands
deps = {
    "num_builder": num_builder,
    "eq_builder": eq_builder,
    "alu": alu,
    "display": window.get_display()
}
build_num_cmd = BuildNumberCommand(**deps)
clear_all_cmd = ClearAllCommand(**deps)
clear_entry_cmd = ClearEntryCommand(**deps)
backspace_cmd = BackspaceCommand(**deps)
change_sign_cmd = ChangeSignCommand(**deps)
build_fraction_cmd = SetBuilderTypeToFractionCommand(**deps)
add_cmd = AdditionCommand(**deps)
sub_cmd = SubtractionCommand(**deps)
mul_cmd = MultiplicationCommand(**deps)
div_cmd = DivisionCommand(**deps)
eq_cmd = EqualityCommand(**deps)


# create buttons
button_map = [
    # label         command                     row     column
    [Char.C,        clear_all_cmd,              2,      0],
    [Char.CE,       clear_entry_cmd,            2,      1],
    [Char.DEL,      backspace_cmd,              2,      2],
    [Char.DIVIDE,   div_cmd,                    2,      3],
    # label         command                     row     column
    [Char.SEVEN,    build_num_cmd,              3,      0],
    [Char.EIGHT,    build_num_cmd,              3,      1],
    [Char.NINE,     build_num_cmd,              3,      2],
    [Char.MULTIPLY, mul_cmd,                    3,      3],
    # label         command                     row     column
    [Char.FOUR,     build_num_cmd,              4,      0],
    [Char.FIVE,     build_num_cmd,              4,      1],
    [Char.SIX,      build_num_cmd,              4,      2],
    [Char.SUBTRACT, sub_cmd,                    4,      3],
    # label         command                     row     column
    [Char.ONE,      build_num_cmd,              5,      0],
    [Char.TWO,      build_num_cmd,              5,      1],
    [Char.THREE,    build_num_cmd,              5,      2],
    [Char.ADD,      add_cmd,                    5,      3],
    # label         command                     row     column
    [Char.SIGN,     change_sign_cmd,            6,      0],
    [Char.ZERO,     build_num_cmd,              6,      1],
    [Char.DOT,      build_fraction_cmd,         6,      2],
    [Char.EQ,       eq_cmd,                     6,      3]
]

# create and draw buttons
window.get_display().draw()
for params in button_map:
    label = params[0].value
    # create
    window.create_button(label=label, command=params[1])
    # draw
    btn = window.get_button(label=label)
    btn.draw(row=params[2], column=params[3])

# show window
window.show()
