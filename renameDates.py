#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import re
import os
import shutil

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
((0|1)?\d)- # one or two digits for the month
((0|1|2|3)?\d)- # one or two digits for the day
((19|20)\d\d) # four digits for the year
(.*?)$ # all text after the date
w """, re.VERBOSE)

def rename_dates(dir):
    for amerFilename in os.listdir(dir):
        mo = datePattern.search(amerFilename)
        if mo == None:
            continue
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)
        euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

        absWorkingDir = os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)

        print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
        shutil.move(amerFilename, euroFilename)


rename_dates(r"C:\temp\dates")