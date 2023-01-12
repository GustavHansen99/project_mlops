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

    if not os.path.exists(os.path.join(output_filepath, 'train')):
        logger.exception('Output train folder does not exist')
        raise Exception('Output train folder does not exist')

    if not os.path.exists(os.path.join(output_filepath, 'test')):
        logger.exception('Output test folder does not exist')
        raise Exception('Output test folder does not exist')

    if not os.path.exists(os.path.join(output_filepath, 'validate')):
        logger.exception('Output validation folder does not exist')
        raise Exception('Output validation folder does not exist')

    images_healthy = []
    images_tumor = []
    for root, _, files in os.walk(input_filepath):
        for file in files:
            if 'jpg' in file:
                if 'NotCancer' in file:
                    images_healthy.append([root, file])
                else:
                    images_tumor.append([root, file])

    for i in range(len(images_healthy)):
        if i < 0.8*len(images_healthy):
            shutil.copy2(os.path.join(images_healthy[i][0], images_healthy[i][1]), os.path.join(output_filepath, 'train', images_healthy[i][1]))
        if i >=0.8*len(images_healthy) and i < 0.9*len(images_healthy):
            shutil.copy2(os.path.join(images_healthy[i][0], images_healthy[i][1]), os.path.join(output_filepath, 'validate', images_healthy[i][1]))
        if i >= 0.9*len(images_healthy):
            shutil.copy2(os.path.join(images_healthy[i][0], images_healthy[i][1]), os.path.join(output_filepath, 'test', images_healthy[i][1]))

    for i in range(len(images_tumor)):
        if i < 0.8*len(images_tumor):
            shutil.copy2(os.path.join(images_tumor[i][0], images_tumor[i][1]), os.path.join(output_filepath, 'train', images_tumor[i][1]))
        if i >=0.8*len(images_tumor) and i < 0.9*len(images_tumor):
            shutil.copy2(os.path.join(images_tumor[i][0], images_tumor[i][1]), os.path.join(output_filepath, 'validate', images_tumor[i][1]))
        if i >= 0.9*len(images_tumor):
            shutil.copy2(os.path.join(images_tumor[i][0], images_tumor[i][1]), os.path.join(output_filepath, 'test', images_tumor[i][1]))
                

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
