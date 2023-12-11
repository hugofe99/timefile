import json
from typing import Any, Iterator

class TimeLog:
    def __init__(self, kwargs: dict[str, Any], time_delta: float) -> None:
        self.kwargs = kwargs
        self.time_delta = time_delta

    def json_str(self) -> str:
        return json.dumps(self.__dict__)
    

class FunctionLogs:
    def __init__(self, function_name: str, time_logs: list[TimeLog] = None) -> None:
        self.function_name = function_name
        self.time_logs = time_logs or []

    def __repr__(self) -> str:
        s = ""
        for time_log in self.time_logs: 
            i = str(time_log.kwargs)[1:-1].replace(": ","=").replace("'","")
            s += f"T({self.function_name}({i})) = {time_log.time_delta}" + "\n"
        return s

class AllFunctionLogs:
    def __init__(self, all_function_logs: dict[str, FunctionLogs] = None) -> None:
        self.all_function_logs = all_function_logs or {}

    def add_timelog(self, function_name: str, time_log: TimeLog) -> None:
        if function_name not in self.all_function_logs:
            self.all_function_logs[function_name] = FunctionLogs(function_name=function_name)
        self.all_function_logs[function_name].time_logs.append(time_log)
        
    def __iter__(self) -> Iterator[FunctionLogs]:
        for function_logs in self.all_function_logs.values():
            yield function_logs