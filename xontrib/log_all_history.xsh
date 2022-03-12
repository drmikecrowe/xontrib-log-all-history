import os
from datetime import datetime

__all__ = ()

if "LOG_DESTINATION" not in ${...}:
    $LOG_DESTINATION="{}/.logs".format($HOME)

def init():
    if $XONSH_HISTORY_BACKEND == 'sqlite':
        from xonsh.history.sqlite import SqliteHistory
        class HistoryProxy(SqliteHistory):
            pass
    else:
        from xonsh.history.json import JsonHistory
        class HistoryProxy(JsonHistory):
            pass

    class SaveAllHistory(HistoryProxy):
        cache = []

        def append(self, cmd):
            try:
                $LOG_ALL_HISTORY_DIR = "{}{}".format($LOG_DESTINATION, $PWD)
                if not os.path.exists($LOG_ALL_HISTORY_DIR):
                    os.makedirs($LOG_ALL_HISTORY_DIR)
                $LOG_ALL_HISTORY_FILE = "{}/xonsh-history-{}.log".format($LOG_ALL_HISTORY_DIR, datetime.now().strftime("%Y-%m-%d"))
                self.cache.append("{} {}".format(datetime.now().strftime("%Y-%m-%d.%H.%M.%S"), cmd["inp"]))
                open($LOG_ALL_HISTORY_FILE, "a").write("\n".join(self.cache))
                self.cache.clear()
            except Exception as ex:
                print("History not being saved", ex)
                pass
            super().append(cmd)
    $XONSH_HISTORY_BACKEND = SaveAllHistory

    aliases['hgrep'] = lambda args: execx('grep -ERh {} {}'.format(repr(args[0]), $LOG_DESTINATION))
    aliases['hdgrep'] = lambda args: execx('grep -ERh {} {}'.format(repr(args[0]), $LOG_DESTINATION + $PWD))
init()
