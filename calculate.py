import circle
import square
import triangle


figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {}


def calc(figure, function, length):
    assert figure in figs
    assert function in funcs

    result = eval(f'{figure}.{function}(*{length})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input(
            "Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    calc(fig, func, size)
