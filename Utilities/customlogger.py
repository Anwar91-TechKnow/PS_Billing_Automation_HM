import logging


class LogGen:
    @staticmethod
    def loggentestcase():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename="C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//Logs//Demo.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%b/%y %I:%M:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def loggenndep():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename="C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Logs//NDEP"
                                     ".log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%b/%y %I:%M:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

# logging.debug("Hello debug")
# logging.info("Hello info")
# logging.warning("Hello Warning")
# logging.error("Hello error")
# logging.critical("Hello Critical")
