from lawgokr import LawgokrSpider
from time import sleep

DAY = 86400

if __name__ == '__main__':
    while True:
        LawgokrSpider.run()
        sleep(DAY * 30)
