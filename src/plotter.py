import re
from . import config
import json
import matplotlib.pyplot as plt
from . models import TimeLog, FunctionLogs, AllFunctionLogs


def _plot_and_save(f_name: str, y: list, y_name: str, t: list, t_name: str = "time_delta"):
    plt.scatter(y, t)
    plt.xlabel(y_name)
    plt.ylabel(t_name)
    plt.title(f'Scatter Plot: {y_name} vs. {t_name}')
    plt.savefig(f"{config.PLOT_DIR}/{f_name}_{y_name}.png")


def _parse_logs() -> AllFunctionLogs:
    functions = AllFunctionLogs()
    log_pattern = re.compile(r'(?P<timestamp>.*?) \[TIMEFILE\] \[(?P<function_name>.*?)\]: (?P<message>.*)')
    with open(config.LOG_FILEPATH, 'r') as log_file:
        for line in log_file:
            match = log_pattern.match(line)
            if not match:
                continue

            function_name = match.group('function_name')
            time_log = TimeLog(**json.loads(match.group('message')))
            functions.add_timelog(function_name=function_name, time_log=time_log)
    return functions

def timeplot():
    functions = _parse_logs()
    print(functions)
