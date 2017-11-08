import time

class SeleniumUtil():
    def __init__(self, unit, driver):
        self.unit = unit

    def wait_func(self, func, count):
        flag = False
        for n in range(count):
            try:
                func()
                flag = True
                break
            except:
                time.sleep(1)
        if not flag:
            raise Exception

