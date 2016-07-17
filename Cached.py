import time
import pickle
import os

__author__ = 'tivvit'


def _rename(new_name):
    def decorator(f):
        f.__name__ = new_name
        return f

    return decorator


class Cached(object):
    """
    Decorator object providing caching for functions
    Suitable for time consuming computations
    Stores result in pickle
    Checks if function args matches
    Always use newest result
    """

    def __init__(self, force_run=False, output_path="cached_data", name=""):
        self.force_run = force_run
        self.output_path = output_path
        self.name = name

    def __call__(self, f):
        if not os.path.isdir(self.output_path):
            os.mkdir(self.output_path)
        if not self.name:
            self.name = f.__name__

        # rename is used because other decorators using __name__
        @_rename(self.name)
        def wrapped_f(*args, **kwargs):
            self.name_params = self.name + "_" + str(
                hash(str(args) + "|" + str(kwargs)))

            if not self.force_run:
                return_value = self.__load()

            if self.force_run or not return_value:
                return_value = f(*args, **kwargs)
                out_file_name = self.name_params + "_" + str(
                    time.time()) + ".pkl"
                with open(os.path.join(self.output_path, out_file_name),
                          "wb+") as out_file:
                    pickle.dump(return_value, out_file)

            return return_value

        return wrapped_f

    def __load(self):
        import glob

        files = glob.glob(
            os.path.join(self.output_path, self.name_params + "*"))
        if files:
            newest_file = max(files)
            with open(newest_file, "rb") as out:
                from datetime import datetime

                create_time = float(
                    newest_file.replace(".pkl", "").split("_")[-1])
                created = datetime.fromtimestamp(create_time).strftime(
                    "%d.%m.%Y %H:%M:%S")
                print "loading %s (created %s)" % (newest_file, created)
                return pickle.load(out)
        else:
            print "%s_*.pkl not found (maybe different args). RUNNING" % os.path.join(
                self.output_path,
                self.name_params)
