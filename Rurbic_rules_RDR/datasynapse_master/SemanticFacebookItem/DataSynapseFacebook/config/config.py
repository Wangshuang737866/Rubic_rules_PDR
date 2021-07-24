import configparser
import os


def config_file(section, variable):
    config = configparser.RawConfigParser()
    filename = os.getcwd()
    print("filename", filename+'/config/config.ini')
    config.read(filename + '/config/config.ini')
    path_str=config.get(section,variable)
    #path_str = "/Users/iti/PycharmProjects/Rurbic_rules_RDR/datasynapse_master/SemanticFacebookItem/DataSynapseFacebook/Facebook"#config.get(section, variable)
    return path_str


#print(config_file('dir', 'path'))
