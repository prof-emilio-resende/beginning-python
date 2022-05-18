from typing import Callable

# Ferramentas
# - python, pip, virutalenv


# Knowing the basics
def main():
    print('main is running...')
    # Dynamic types with hinting
    text = 'text'
    integer_number = 10
    decimal_number = 10.3
    array = list()
    dictionary = dict()

    print(type(text))
    print(type(integer_number))
    print(type(decimal_number))
    print(type(array))
    print(type(dictionary))

    # Testing hints
    # number = hint_test_function(integer_number)  # error is expected
    txt_number = hint_test_function(text)  # error is not expected
    print(txt_number)

    # using a builder function
    logger_builder('[funny logs]')('business message...')
    Logger('[funny logs]').log('business message...')

    # comprehension
    squares = map(lambda n: n**2, range(10))
    squares_comp = [n ** 2 for n in range(10)]
    print(list(squares))
    print(list(squares_comp))

    # filters
    squares2 = map(lambda n: n ** 2, filter(lambda n: not n % 2, range(10)))
    squares2_comp = [n ** 2 for n in range(10) if not n % 2]
    print(list(squares2))
    print(squares2_comp)

# hint for input parameters, hint for function return type
def hint_test_function(textInput: str) -> str:
    print(textInput.encode())

    return (10).__str__()


# basics of functional programming
def logger_builder(prefix):
    func: Callable[[str],
                   None] = lambda txt: print(f'{prefix}[customized functional logging]: {txt}')
    return func

# OO em geral (básico)
class Logger():
    def __init__(self, prefix: str):
        self.prefix = prefix

    def log(self, txt: str) -> None:
        print(f'{self.prefix}[customized oo logging]: {txt}')


if __name__ == '__main__':
    main()
