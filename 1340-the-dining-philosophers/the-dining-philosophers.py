from threading import Lock


class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: "Callable[[], None]",
        pickRightFork: "Callable[[], None]",
        eat: "Callable[[], None]",
        putLeftFork: "Callable[[], None]",
        putRightFork: "Callable[[], None]",
    ) -> None:
        leftFork = philosopher
        rightFork = (philosopher + 1) % 5
        if philosopher == 4:
            self.forks[rightFork].acquire()
            self.forks[leftFork].acquire()
        else:
            self.forks[leftFork].acquire()
            self.forks[rightFork].acquire()

        try:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
        finally:
            self.forks[rightFork].release()
            self.forks[leftFork].release()
