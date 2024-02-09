import logging
import logging
class LogGenerator:

    def __init__(self):
        self.logger = logger.bind(classname=self.__class__.__name__)
    @staticmethod
    def logg_in():

        logfile = logging.FileHandler("D:\\Python Automation Practicals\\Pytest Practicals\\Pytest_All_Folder_practice\Logs\\CredKarAutomation.log")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)s -%(message)s")
        logfile.setFormatter(format)

        logger = logging.getLogger()
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger