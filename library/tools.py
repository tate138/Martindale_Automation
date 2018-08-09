import time
import os



class Tools:
    """ Class of short reusable general static methods used as helper methods """
    def __init__(self):
        pass

    IS_DEBUG = True

    @staticmethod
    def log(string):
        """ Togglable print function

        :param str, int string:
        """
        if Tools.IS_DEBUG:
            try:
                print(str(string))

            except Exception as e:
                print("Error Printing String from library.tools.log")

    @staticmethod
    def sleep(sleep_time):
        """ Basic sleep method to sleep for seconds

        :param int sleep_time: sleep time in seconds
        """
        time.sleep(sleep_time)

    @staticmethod
    def build_relative_directory_path(directory_name):
        """Finds the relative path of the directory and creates a temporary python path to the location

        :param str directory_name: the name of the directory

        :rtype: uri
        :return: The relative location of the directory
        """
        COMBINED_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), directory_name)
        return COMBINED_PATH

    @staticmethod
    def object_has_value(object_of_value):
        """ Does the object exist

        :param obj object_of_value:

        :rtype: bool
        :return: True or False
        """
        return object_of_value is not None and len(object_of_value) > 0

    @staticmethod
    def objects_have_value(*arg):
        """ Do the objects exist

        :param object arg:

        :rtype: bool
        :return: True or False
        """
        is_error_free = True
        for is_error_free in arg:
            if Tools.object_has_value(is_error_free):
                pass
            else:
                is_error_free = False
        return is_error_free

    @staticmethod
    def raise_exception(exception):
        """Raises an exception

        :param str exception:
        """
        raise Exception(exception)