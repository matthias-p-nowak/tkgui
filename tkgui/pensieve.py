print(f"importing pensieve {__file__}")

import pickle
import atexit
from platformdirs import user_data_dir
import os
import sys
import logging

config = None
saveFcts = set()


class Empty:
    pass


def saveOnExit():
    global config
    logging.debug("Saving config on exit")
    for f in saveFcts:
        f()
    with open(getFileName(), "wb") as f:
        pickle.dump(config, f)


atexit.register(saveOnExit)


def getFileName():
    app_name = os.path.basename(sys.argv[0])
    app_name = os.path.splitext(app_name)[0]
    cfgDir = user_data_dir(app_name)
    os.makedirs(cfgDir, exist_ok=True)
    return os.path.join(cfgDir, "pensieve.db")


def getConfig():
    global config
    if not config:
        fileName = getFileName()
        if not os.path.exists(fileName):
            config = Empty()
            return config
        with open(fileName, "rb") as f:
            config = pickle.load(f)
    return config
