from heapq import *


class State:
    def __init__(self):
        self.g = False
        self.c = 0

    def is_green(self):

        return self.g

    def add_car(self):

        self.c = self.c + 1

    def purge_cars(self):

        self.c = 0

    def waiting_cars(self):

        return self.c

    def turn_green(self):

        self.g = True

    def turn_red(self):

        self.g = False

    def __str__(self):

        return "Green light =" + str(self.g) + ", cars=" + str(self.c)


Tc = 30
Tp = 10


class Event:
    def time(self):

        return self.t

    def __str__(self):

        return self.name + "(" + str(self.t) + ")"

    def __lt__(self, other):

        return self.t < other.t


class CAR(Event):
    def __init__(self, time):
        self.t = time
        self.name = "CAR"

    def action(self, queue, state):
        if not state.is_green():
            state.add_car()
            if state.waiting_cars() == 1:
                queue.insert(R2G(self.t + Tc))


class R2G(Event):  # red to green
    def __init__(self, time):
        self.t = time
        self.name = "R2G"

    def action(self, queue, state):
        queue.insert(G2R(self.t + state.waiting_cars() * Tp))
        state.turn_green()
        state.purge_cars()


class G2R(Event):  # green to red
    def __init__(self, time):
        self.t = time
        self.name = "G2R"

    def action(self, queue, state):
        state.turn_red()


class EventQueue:
    def __init__(self):
        self.q = []

    def notEmpty(self):

        return len(self.q) > 0

    def remaining(self):

        return len(self.q)

    def insert(self, event):

        heappush(self.q, event)

    def next(self):

        return heappop(self.q)


Q = EventQueue()

Q.insert(CAR(10))
Q.insert(CAR(25))
Q.insert(CAR(35))
Q.insert(CAR(60))
Q.insert(CAR(75))

S = State()

# Processing events until the queue is Q is empty
while Q.notEmpty():
    e = Q.next()
    print(e)
    e.action(Q, S)
