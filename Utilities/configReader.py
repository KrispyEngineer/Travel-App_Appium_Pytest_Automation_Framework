from configparser import ConfigParser



def get_config(section, key):
    config = ConfigParser()
    config.read("..//ConfigurationData//config.ini")
    return config.get(section, key)


print(get_config("locators","hotels_ID"))