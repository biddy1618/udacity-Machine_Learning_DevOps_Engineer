#!/usr/bin/env python
import argparse
import logging
import pathlib
import wandb


logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(message)s')
logger = logging.getLogger()


def go(args):

    logger.info('Creating run in project exercise_1')
    run = wandb.init(project='exercise_1', job_type='use_file')

    logger.info('Getting artifact')

    # YOUR CODE HERE: get the artifact and store its local path in the variable "artifact_path"
    # HINT: you can get the artifact path by using the "file()" method
    # declaring that we are using this artifact but not downloading it yet
    artifact = run.use_artifact(args.artifact_name)

    # to download, we have to use artifact.file() method that returns local path
    # to the file within wandb folder
    artifact_path = artifact.file()
    logger.info(f'Artifact path: {artifact_path}')

    logger.info('Artifact content:')
    with open(artifact_path, 'r') as fp:
        content = fp.read()

    print(content)
    run.finish()

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
        description='Use an artifact from W&B', fromfile_prefix_chars='@'
    )

    parser.add_argument(
        '--artifact_name', type=str, help='Name and version of W&B artifact', required=True
    )

    args = parser.parse_args()

    go(args)
