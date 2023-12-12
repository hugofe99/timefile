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


def _plot_total(all_function_logs: AllFunctionLogs) -> None:
    function_names = []
    function_total_times = []
    for function_logs in all_function_logs:
        function_names.append(function_logs.function_name)
        total_time = 0
        for time_log in function_logs.time_logs:
            total_time += time_log.time_delta
        function_total_times.append(total_time)
    fig, ax = plt.subplots()
    ax.bar(function_names, function_total_times)
    plt.show()


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
    _plot_total(functions)