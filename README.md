# Time To Clipboard
A Python command-line tool to copy the current time to the clipboard.

It is possible to change the timezone and the output format. The output format is customized using [the strftime format](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior).

## Table of Contents
- [Arguments](#arguments)
- [Example](#example)
- [Quickstart](#quickstart)
  - [Download latest stable version](#download-latest-stable-version)
  - [Install requirements](#install-requirements)
  - [Use the command-line tool](#use-the-command-line-tool)

## Arguments
To get all the arguments type `python timeToClipboard.py -h`.
```
$ python timeToClipboard.py -h
usage: timeToClipboard.py [-h] [--format FORMAT] [--timezone TIMEZONE]

optional arguments:
  -h, --help           show this help message and exit
  --format FORMAT      "strftime" time format to return. Default is
                       "%Y_%m_%dT%H_%M_%SZ".
  --timezone TIMEZONE  Timezone, "utc" for UTC time (default), "local" for
                       local time or a UTC offset eg. "+05:00" or just "+05".
```

## Example
```
$ python timeToClipboard.py
```
Will copy something like this to the clipboard:
> 2019_04_03T20_56_30Z

```
$ python timeToClipboard.py --format "%H:%M" --timezone "+05:00"
```
Will copy something like this to the clipboard:
> 04:06

## Quickstart
### Download latest stable version

### Install requirements

### Use the command-line tool
