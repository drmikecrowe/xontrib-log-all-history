<p align="center">
The xontrib save shell session history in `$HOME/.logs`.
</p>

<p align="center">
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/drmikecrowe/xontrib-log-all-history" target="_blank">tweet</a>.
</p>

# Install

To install use pip:

```bash
xpip install xontrib-log-all-history
# or: xpip install -U git+https://github.com/drmikecrowe/xontrib-log-all-history
```

## Usage

```bash
xontrib load log_all_history
# TODO: what's next?
```

> :warning: If you using `SqliteHistory` backend, you **must** include `$XONSH_HISTORY_BACKEND = 'sqlite'` **before** loading.  For example:

```xonsh
$XONSH_HISTORY_BACKEND = 'sqlite'
xontrib load log_all_history
```

## Architecture

This plugin intercepts history before sending to the `JsonHistory` or `SqliteHistory` backend. In short it takes the current command line and append to a history named `$HOME/.logs/$PWD/xonsh-history-{DateTime}.log`.

For example:
```xsh
cat README.md > /dev/null
tail $LOG_ALL_HISTORY_FILE
# 2022-03-11.21.17.01 cat README.md > /dev/null
```

I've been using this method since October in 2019 (both in bash and now xonsh). Here's stats on my logs directory:

```xsh
du -sh ~/.logs
# 16M     /home/mcrowe/.logs
egrep '^201' ~/.logs -Rh | cut -b -7 | sort | uniq | head -n 1
# 2019-10
find ~/.logs | wc -l
# 3645
```

## Searching History

Two helper aliases are enabled to assist in searching your accumulated history.

* `hgrep` -- "H"istory "Grep". This command is simply `grep -ERh {SEARCH_STRING} $HOME/.logs` -- it searches all folders.
* `hdgrep` -- "H"istory in this "D"irectory "Grep". This command is simply `grep -ERh {SEARCH_STRING} $HOME/.logs/$PWD` -- it searches all logs you've done in this specific directory.

For example you use the `python` command frequently. You remember using a `python` command in the past for the current project with a lot of parameters you figured out, but you didn't save it. If you did `hgrep python`, you'd find many entries. By using `hdgrep python`, you find the specific command.

Example:

```xsh
hgrep cat | wc -l
# 1427
hdgrep cat | wc -l
# 10
```

## Environment variables

#### `$LOG_ALL_HISTORY_DIR` 

If you want to place to the logs in a different folder, set:

```xonsh
$LOG_ALL_HISTORY_DIR = f"{$HOME}/.all-logs"
xontrib load 'log-all-history'
```

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
