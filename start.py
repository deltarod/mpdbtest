from multiprocessing import Process
from mp import db


def openDb(procNum):
    print('start', procNum)
    db.openEnv()

    db.addExitRegister()

    db.openDBs()
    print('end', procNum)


numProcesses = 2


def doTest():
    db.openEnv(recover=True)

    processes = []

    for i in range(0, numProcesses):
        p = Process(target=openDb, args=(i,))
        processes.append(p)
        p.start()

    for proc in processes:
        proc.join()


if __name__ == '__main__':
    while True:
        doTest()


