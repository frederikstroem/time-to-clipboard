import time
import pyperclip
from argparse import ArgumentParser
from datetime import datetime, timedelta

# Command-line arguments.
parser = ArgumentParser()
# strftime format.
# Source: https://stackoverflow.com/a/21168121 (2019-04-03)
default = "%Y_%m_%dT%H_%M_%SZ"
parser.add_argument("--format",
                    default="%Y_%m_%dT%H_%M_%SZ",
                    help='"strftime" time format to return. Default is "%s".' % default.replace(r"%", r"%%"))
# Timezone.
parser.add_argument("--timezone",
                    default="utc",
                    help='Timezone, "utc" for UTC time (default), "local" for local time or a UTC offset eg. "+05:00" or just "+05".')
# Parse arguments.
args = parser.parse_args()

strftimeFormat = args.format
timezone = args.timezone

# Create return string.
returnString = None

if timezone == "utc":
    returnString = time.strftime(strftimeFormat, time.gmtime())
elif timezone == "local":
    returnString = time.strftime(strftimeFormat, time.localtime())
else:
    # If there is an offset, it gets tricky.
    # Source: https://stackoverflow.com/a/46402186 (2019-04-03)
    currentTime = datetime.today()
    unformatedReturnString = None
    hourOffset = 0
    minuteOffset = 0
    hourOffset = int(timezone[1:3])
    if len(timezone) == 6:
        minuteOffset = int(timezone[4:6])
    if timezone[0:1] == "+":
        unformatedReturnString = currentTime + timedelta(hours=hourOffset, minutes=minuteOffset)
    else:
        unformatedReturnString = currentTime - timedelta(hours=hourOffset, minutes=minuteOffset)
    returnString = unformatedReturnString.strftime(strftimeFormat)

# Copy to clipboard.
pyperclip.copy(returnString)
