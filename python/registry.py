import configparser

config = configparser.ConfigParser()

config.add_section('Section1')
config.set('Section1', 'Option1', 'Value1')
config.set('Section1', 'Option2', 'Value2')

config.add_section('Section2')
config.set('Section2', 'Option3', 'Value3')
config.set('Section2', 'Option4', 'Value4')

# INI is not really recommended for configuration
with open('config.ini', 'w') as configfile:
    config.write(configfile)
    print('File created')