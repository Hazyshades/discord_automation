import schedule

import timetable
import requests

from test import typegm
from timetable import *
import timetable






def main():
    schedule.every(24).hour.do(typegm)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()