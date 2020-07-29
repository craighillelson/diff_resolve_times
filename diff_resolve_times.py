"""Calculate resolution times."""

import csv
from collections import namedtuple
from datetime import datetime

INCIDENTS_DCT = {}


def format_date(inc_datetime):
    """Format dates."""
    date_fmt = '%Y-%m-%d %H:%M:%S'
    inc_datetime = datetime.strptime(inc_datetime, date_fmt)
    return inc_datetime


def open_csv(inc_file, dct):
    """Open csv and populate a dictionary with its contents."""
    with open(inc_file) as csv_file:
        f_csv = csv.reader(csv_file)
        column_headings = next(f_csv)
        csv_row = namedtuple('Row', column_headings)
        for rows in f_csv:
            row = csv_row(*rows)
            num = row.number
            opened = row.opened_at
            resolved = row.resolved_at
            dct[num] = opened, resolved


open_csv('incidents.csv', INCIDENTS_DCT)

for inc_num, times in INCIDENTS_DCT.items():
    if times[0] and times[1]:
        inc_open = format_date(times[0])
        inc_res = format_date(times[1])
        diff = inc_res - inc_open
        diff_minutes = (diff.days * 24 * 60) + (diff.seconds/60)
        print(inc_num, inc_open, inc_res, "{:.2f}".format(diff_minutes))
    else:
        pass
