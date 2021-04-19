import yaml
import os


BASEDIR = os.getcwd()
conf_path = os.path.join(BASEDIR, 'conf')

def get_conf(conf_name: str) -> dict :
    with open(os.path.join(conf_path, conf_name), 'r') as file:
        conf = yaml.load(file, Loader=yaml.FullLoader)

    return conf
