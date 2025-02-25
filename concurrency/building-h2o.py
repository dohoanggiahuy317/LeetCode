from threading import Semaphore

class H2O:
    def __init__(self):
        self.o_sem = Semaphore(1)
        self.h_sem = Semaphore(2)
        self.can_release_o = False

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:  
        self.h_sem.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.o_sem.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None: 
        self.o_sem.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
		 # release 2 hydrogen atoms for every oxygen atom. 
        self.h_sem.release()
        self.h_sem.release()