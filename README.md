[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


# xontrib log_all_history

[xonsh](https://xon.sh) history logger

`log_all_history` persists all shell history in `$HOME/.logs` while also supporting both the `JsonHistory` and `SqliteHistory` backends.

- [xontrib log_all_history](#xontrib-log_all_history)
  - [Install](#install)
  - [Architecture](#architecture)
  - [Searching History](#searching-history)
    - [`hgrep` -- "H"istory "Grep"](#hgrep----history-grep)
    - [`hgrep` -- "H"istory in this "D"irectory "Grep"](#hgrep----history-in-this-directory-grep)
  - [Optional Configuration](#optional-configuration)

## Install

Install using pip

```sh
pip install xontrib-log_all_history
```

Add to your `.xonshrc` as follows:

```sh
xontrib load log_all_history
```

> :warning: If you using `SqliteHistory` backend, you **must** include `$XONSH_HISTORY_BACKEND = 'sqlite'` **before** loading.  For example:

```xonsh
$XONSH_HISTORY_BACKEND = 'sqlite'
xontrib load 'log-all-history'
```


## Architecture

This plugin intercepts history before sending to the `JsonHistory` or `SqliteHistory` backend. In short:

* Take the current command line and append to a history named:
    `$HOME/.logs/$PWD/xonsh-history-{DateTime}.log`
* For example:

```sh
 ~/P/P/x/xontrib-log-all-history  cat README.md > /dev/null
 ~/P/P/x/xontrib-log-all-history  tail $LOG_ALL_HISTORY_FILE
2022-03-11.21.17.01 cat README.md > /dev/null
 ~/P/P/x/xontrib-log-all-history 
```

I've been using this method since October in 2019 (both in bash and now xonsh). Here's stats on my logs directory:

```sh
 ~/P/P/x/xontrib-log-all-history  du -sh ~/.logs
16M     /home/mcrowe/.logs
 ~/P/P/x/xontrib-log-all-history  egrep '^201' ~/.logs -Rh | cut -b -7 | sort | uniq | head -n 1
2019-10
 ~/P/P/x/xontrib-log-all-history  find ~/.logs | wc -l
3645
 ~/P/P/x/xontrib-log-all-history 
```

## Searching History

Two helper aliases are enabled to assist in searching your accumulated history:

### `hgrep` -- "H"istory "Grep"

This command is simply `grep -ERh {SEARCH_STRING} $HOME/.logs` -- it searches all folders.

### `hgrep` -- "H"istory in this "D"irectory "Grep"

This command is simply `grep -ERh {SEARCH_STRING} $HOME/.logs/$PWD` -- it searches all logs you've done in this specific directory. The use-case for this is:

* You use the `python` command frequently
* You remember using a `python` command in the past for the current project with a lot of parameters you figured out, but you didn't save it.
  * If you did `hgrep python`, you'd find many entries.
  * By using `hdgrep python`, you find the specific command.

Example:

```sh
 ~/P/P/x/xontrib-log-all-history  hgrep cat | wc -l
1427
 ~/P/P/x/xontrib-log-all-history  hdgrep cat | wc -l
10
 ~/P/P/x/xontrib-log-all-history 
```

(yes, I did several `cat`s testing for the readme...)

## Optional Configuration

If you want to place to the logs in a different folder, set:

```xonsh
$LOG_ALL_HISTORY_DIR = f"{$HOME}/.all-logs"
xontrib load 'log-all-history'
```


[forks-shield]: https://img.shields.io/github/forks/drmikecrowe/xontrib-log-all-historye.svg?style=for-the-badge
[forks-url]: https://github.com/drmikecrowe/xontrib-log-all-historye/network/members
[stars-shield]: https://img.shields.io/github/stars/drmikecrowe/xontrib-log-all-historye.svg?style=for-the-badge
[stars-url]: https://github.com/drmikecrowe/xontrib-log-all-historye/stargazers
[issues-shield]: https://img.shields.io/github/issues/drmikecrowe/xontrib-log-all-historye.svg?style=for-the-badge
[issues-url]: https://github.com/drmikecrowe/xontrib-log-all-historye/issues
[license-shield]: https://img.shields.io/github/license/drmikecrowe/xontrib-log-all-historye.svg?style=for-the-badge
[license-url]: https://github.com/drmikecrowe/xontrib-log-all-historye/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mwcrowe/
