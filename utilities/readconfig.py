import configparser

config = configparser.RawConfigParser()
config.read("D:\\Python Automation Practicals\\Pytest Practicals\\Pytest_All_Folder_practice\\Configuration\config.ini")


class Readconfig:

    @staticmethod
    def get_user_email():
        user_email = config.get('login data','UserEmail')
        return user_email 

    @staticmethod
    def get_password():
        password = config.get('login data','Password')
        return password

