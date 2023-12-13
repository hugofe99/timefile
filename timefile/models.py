import json
from typing import Any, Iterator
import warnings
from .config import MAX_LOG_WARNING
import math


class TimeLog:
    _instances = {}

    def __init__(
        self, kwargs: dict[str, Any], time_delta: float, _fn: str | None = None
    ) -> None:
        self.kwargs = kwargs
        self.time_delta = time_delta

        if not _fn:
            return

        if _fn not in self.__class__._instances:
            self.__class__._instances[_fn] = 1
        self.__class__._instances[_fn] += 1

        if self.__class__._instances[_fn] > MAX_LOG_WARNING:
            warning_message = f"\n\n WARNING: The function '{_fn}' has been logged > 10^{int(math.log10(MAX_LOG_WARNING))} times. This might affect performance. Consider an outer wrapper of these function calls :)"
            warnings.warn(warning_message)

    def json_str(self) -> str:
        return json.dumps(self.__dict__)


class FunctionLogs:
    def __init__(self, function_name: str, time_logs: list[TimeLog] = None) -> None:
        self.function_name = function_name
        self.time_logs = time_logs or []

    def __repr__(self) -> str:
        s = ""
        for time_log in self.time_logs:
            i = str(time_log.kwargs)[1:-1].replace(": ", "=").replace("'", "")
            s += f"T({self.function_name}({i})) = {time_log.time_delta}" + "\n"
        return s

    def as_series(self) -> dict:
        series = {"time_delta": []}
        for time_log in self.time_logs:
            series["time_delta"].append(time_log.time_delta)
            for k, v in time_log.kwargs.items():
                if k not in series:
                    series[k] = []
                series[k].append(v)
        return series


class AllFunctionLogs:
    def __init__(self, all_function_logs: dict[str, FunctionLogs] = None) -> None:
        self.all_function_logs = all_function_logs or {}

    def add_timelog(self, function_name: str, time_log: TimeLog) -> None:
        if function_name not in self.all_function_logs:
            self.all_function_logs[function_name] = FunctionLogs(
                function_name=function_name
            )
        self.all_function_logs[function_name].time_logs.append(time_log)

    def __iter__(self) -> Iterator[FunctionLogs]:
        for function_logs in self.all_function_logs.values():
            yield function_logs
