### Config / Settings

# DEBUG
RESET = True

# Logging
TOTAL_RUNTIME = "Total Runtime"
MAX_LOG_WARNING = 10**5

LOGGING_LEVEL_VALUE = 22
LOGGING_LEVEL_NAME = "TIMEFILE"
LOGGING_FORMAT = "%(asctime)s [%(levelname)s] [%(name)s]: %(message)s"
LOGGING_DATETIME = "%Y-%m-%d %H:%M:%S"

# Files and Dirs
TIMEFILE_DIR = "./timefiles"
LOG_DIR = f"{TIMEFILE_DIR}/logs"
PLOT_DIR = f"{TIMEFILE_DIR}/plots"
LOG_FILENAME = "timelogs.log"
LOG_FILEPATH = f"{LOG_DIR}/{LOG_FILENAME}"
