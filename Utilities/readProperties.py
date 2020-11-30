import configparser

config = configparser.RawConfigParser()
configfilepath = "C:\\Users\\Suresh\\PycharmProjects\\001\\Configurations\\config.ini"
config.read(configfilepath)

class ReadConfig:
    @staticmethod
    def getApplicationurl():
        url = config.get('common data','url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common data','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data','password')
        return password

    @staticmethod
    def getPath():
        path = config.get('common data','path')
        return path


