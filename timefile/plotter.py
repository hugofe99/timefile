import re
from . import config
import json
import matplotlib.pyplot as plt
from .models import TimeLog, FunctionLogs, AllFunctionLogs
from .helpers import string_to_rgb
from datetime import datetime
import numpy as np


def _plot_and_save(
    f_name: str, y: list, y_name: str, t: list, t_name: str = "Time (s)"
):
    ffig, ax = plt.subplots()
    scatter = ax.scatter(y, t, color=string_to_rgb(f_name))
    ax.set_xlabel(y_name)
    ax.set_ylabel(t_name)
    ax.set_title(f"Time of {f_name} vs {y_name}")
    ax.grid(True, linestyle="--", alpha=0.7)
    plt.savefig(
        f"{config.PLOT_DIR}/{f_name} {y_name} vs {t_name} @{datetime.now().strftime(config.LOGGING_DATETIME)}.png"
    )
    plt.close()


def _plot_each(all_function_logs: AllFunctionLogs) -> None:
    for function_logs in all_function_logs:
        if function_logs.function_name == config.TOTAL_RUNTIME:
            continue

        series_function_logs = function_logs.as_series()
        time_series = series_function_logs.pop("time_delta")
        for arg_name, arg_values in series_function_logs.items():
            if len(set(arg_values)) == 1:  # constant = boring ?
                continue
            _plot_and_save(
                f_name=function_logs.function_name,
                y=arg_values,
                y_name=arg_name,
                t=time_series,
            )
        if len(series_function_logs) > 1:
            _plot_and_save(
                f_name=function_logs.function_name,
                y=[i for i in range(len(time_series))],
                y_name="function call #",
                t=time_series,
            )


def _plot_total(all_function_logs: AllFunctionLogs) -> None:
    function_names = []
    function_total_times = []
    colours = []
    for function_logs in all_function_logs:
        function_names.append(function_logs.function_name)
        if function_logs.function_name == config.TOTAL_RUNTIME:
            colours.append("grey")
        else:
            colours.append(string_to_rgb(function_logs.function_name))
        total_time = 0
        for time_log in function_logs.time_logs:
            total_time += time_log.time_delta
        function_total_times.append(total_time)

    if len(function_names) - 1 == 0:  # -1 for tot runtime
        return

    fig, ax = plt.subplots()
    bars = ax.bar(function_names, function_total_times, color=colours)

    title = "Total Execution Time by Function"
    ax.set_title(title)
    ax.set_ylabel("Time (seconds)")
    ax.set_xlabel("Function name")
    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.7,
    )
    ax.set_axisbelow(True)
    for bar, name, time in zip(bars, function_names, function_total_times):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"~{time:.2f} s",
            ha="center",
            va="bottom",
            fontsize=10,
        )
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(
        f"{config.PLOT_DIR}/{title} @{datetime.now().strftime(config.LOGGING_DATETIME)}.png"
    )
    plt.close()


def _parse_logs() -> AllFunctionLogs:
    functions = AllFunctionLogs()
    log_pattern = re.compile(
        r"(?P<timestamp>.*?) \[TIMEFILE\] \[(?P<function_name>.*?)\]: (?P<message>.*)"
    )
    with open(config.LOG_FILEPATH, "r") as log_file:
        for line in log_file:
            match = log_pattern.match(line)
            if not match:
                continue

            function_name = match.group("function_name")
            time_log = TimeLog(**json.loads(match.group("message")))
            functions.add_timelog(function_name=function_name, time_log=time_log)
    return functions


def timeplot():
    all_function_logs = _parse_logs()
    _plot_total(all_function_logs)
    _plot_each(all_function_logs)
