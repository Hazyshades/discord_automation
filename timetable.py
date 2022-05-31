import schedule
import requests
from test import typegm
from timetable import *


def main():
    schedule.every(14).hours.do(typegm)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
