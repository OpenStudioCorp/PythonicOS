import configparser

# create a new ConfigParser object
config = configparser.ConfigParser()

# read an existing configuration file
config.read('config.ini')

# set a value for a setting
config[desktop_config']['setting_name'] = 'setting_value'


# save the configuration to the file
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# get a value for a setting
setting_value = config['section_name']['setting_name']
