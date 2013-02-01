from appdirs import AppDirs
from os import path

PLUGIN_MOD = 'qtimer.plugins.%s.plugin'
COMMANDS_MOD = 'qtimer.commands.%s'

APP_NAME = 'qTimer'
ORG_NAME = 'Solipsis Development'
INI_NAME = '.qtimer'
DEFAULT_NAME = 'default.ini'
LOG_NAME = 'debug.log'

APP_DIRS = AppDirs(APP_NAME, ORG_NAME, roaming=True)

SCRIPT_ROOT = path.dirname(path.realpath(__file__))

DATA_DIR = APP_DIRS.user_data_dir

CONFIG_PATH = path.expanduser(path.join('~', INI_NAME))

LOG_PATH = path.join(APP_DIRS.user_log_dir, LOG_NAME)