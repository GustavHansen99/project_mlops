# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import shutil
import os 

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Making final data set from raw data')

    if not os.path.exists(input_filepath):
        logger.exception('Input folder does not exist')
        raise Exception('Input folder does not exist')

    if not os.path.exists(output_filepath):
        logger.exception('Output folder does not exist')
        raise Exception('Output folder does not exist')

    for root, dirs, files in os.walk(input_filepath):
        for file in files:
            if 'jpg' in file:
                shutil.copy2(os.path.join(root, file), os.path.join(output_filepath, file))

    logger.info('Process ended succesfully')
if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
