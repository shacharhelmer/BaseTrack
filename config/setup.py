import yaml
import logging
from os.path import join, realpath, dirname

def load_conf():
    with open(join(dirname(realpath(__file__)), 'conf_file.yaml'), 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except Exception:
            logging.error('Tracker - config file failed to load')
            return None
