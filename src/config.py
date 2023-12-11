### Config / Settings

# Logging
LOGGING_LEVEL_VALUE = 22
LOGGING_LEVEL_NAME = 'TIMEFILE'
LOGGING_FORMAT = '%(asctime)s [%(levelname)s] [%(name)s]: %(message)s'
LOGGING_DATETIME = '%Y-%m-%d %H:%M:%S'

# Files and Dirs
TIMEFILE_DIR = './timefile'
LOG_DIR = f'{TIMEFILE_DIR}/logs'
PLOT_DIR = f'{TIMEFILE_DIR}/plots'
LOG_FILENAME = 'timelogs.log'
LOG_FILEPATH = f'{LOG_DIR}/{LOG_FILENAME}'
