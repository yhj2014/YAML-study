import yaml
import logging
import os
import sys

with open('logger_config.yml', encoding='UTF-8') as f:
    config = yaml.safe_load(f)

logger = logging.getLogger(config['logger_name'])
os.makedirs(config['log_dir'], exist_ok=True)

sh = logging.StreamHandler(sys.stdout)

info_fh = logging.FileHandler(
    os.path.join(config['log_dir'], config['log_file_name']),
    mode='w',
    encoding='UTF-8'
)

debug_fh = logging.FileHandler(
    os.path.join(config['log_dir'], config['debug_log_file_name']),
    mode='w',
    encoding='UTF-8'
)

log_format = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

sh.setFormatter(log_format)
info_fh.setFormatter(log_format)
debug_fh.setFormatter(log_format)

logger.setLevel(logging.DEBUG)
sh.setLevel(logging.INFO)
info_fh.setLevel(logging.INFO)
debug_fh.setLevel(logging.DEBUG)

logger.addHandler(sh)
logger.addHandler(info_fh)
logger.addHandler(debug_fh)

if __name__ == '__main__':
    logger.debug("This is a DEBUG log")
    logger.info("This is a INFO log")
    logger.warning("This is a WARNING log")
    logger.error("This is a ERROR log")
    logger.critical("This is a CRITICAL log")