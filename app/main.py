import time


class Service:
    def __init__(self, clock):
        self.clock = clock
        return

    def bonjour_bonsoir(self, name):
        return 'Bonsoir ' + name if self.clock.get_hour() > 12 else 'Bonjour ' + name


class Clock:
    def __init__(self):
        return

    def get_hour(self):
        return time.localtime(time.time()).tm_hour