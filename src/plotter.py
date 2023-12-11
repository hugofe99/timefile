import re
from . import config
import ast
import matplotlib.pyplot as plt


def _plot_and_save(f_name: str, y: list, y_name: str, t: list, t_name: str = "time_delta"):
    plt.scatter(y, t)
    plt.xlabel(y_name)
    plt.ylabel(t_name)
    plt.title(f'Scatter Plot: {y_name} vs. {t_name}')
    plt.savefig(f"{config.PLOT_DIR}/{f_name}_{y_name}.png")


def timeplot():
    functions = {}
    log_pattern = re.compile(r'(?P<timestamp>.*?) \[TIMEFILE\] \[(?P<function_name>.*?)\]: (?P<message>.*)')
    with open(config.LOG_FILEPATH, 'r') as log_file:
        for line in log_file:
            match = log_pattern.match(line)
            if not match:
                continue

            function_name = match.group('function_name')
            if function_name not in functions:
                functions[function_name] = []

            message = match.group('message')
            functions[function_name].append(message)
    print(functions)