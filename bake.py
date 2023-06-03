# create "out" folder
# create "src" folder
# init empty git repository
# create .gitignore file with "out/"

import os
import sys
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def main():

    if len(sys.argv) < 2:
        logging.error('ERROR: Empty input, specify folder path')
        return

    PROJECT_PATH = sys.argv[1]

    if os.path.exists(PROJECT_PATH):
        logging.critical(f'ERROR: Project {PROJECT_PATH} already exists')
        return

    logging.info(f'Creating folder {PROJECT_PATH}')    
    os.mkdir(PROJECT_PATH)
    
    logging.info(f'Creating folder src')    
    os.mkdir(f"{PROJECT_PATH}/src/")

    logging.info(f'Creating folder out')    
    os.mkdir(f"{PROJECT_PATH}/out/")

    logging.info('Creating empty git repository')    
    os.system(f"git init \"{PROJECT_PATH}\"")

    logging.info('Creating .gitignore file')    
    os.system(f"echo out/ >> \"{PROJECT_PATH}\"/.gitignore")


if __name__ == "__main__":
    main()
