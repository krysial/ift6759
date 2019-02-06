import argparse
from pathlib import Path

import numpy as np
import torch


def eval_model(dataset_file, model_filename):

    '''
    Skeleton for your testing function. Modify/add
    all arguments you will need.

    '''
    model = None
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # Load your best model
    if model_filename:
        model_filename = Path(model_filename)
        print("\nLoading model from", model_filename.absolute())
        model = torch.load(model_filename, map_location=device)

    if model:

        # # # # # # # # # # # #
        # Add inference here  #
        # # # # # # # # # # # #
        pass

    else:

        print("\nYou did not specify a model, generating dummy data instead!")
        n_classes = 32
        num_data = 10

        y_pred = np.concatenate(
            [np.random.rand(num_data, 3), 
             np.random.randint(0, n_classes, (num_data, 1))
             ], axis=1
        ).astype(np.float32)

    return y_pred


if __name__ == "__main__":

    ###### DO NOT MODIFY THIS SECTION ######
    parser = argparse.ArgumentParser()

    
    parser.add_argument("--dataset", type=str, default='')
    # dataset_dir will be the absolute path to the dataset to be used for
    # evaluation.

    parser.add_argument("--results_dir", type=str, default='')
    # results_dir will be the absolute path to a directory where the output of
    # your inference will be saved.

    args = parser.parse_args()
    dataset_file = args.dataset
    results_dir = args.results_dir
    #########################################


    ###### MODIFY THIS SECTION ######
    # Put your group name here
    group_name = "b1phutN"

    model_filename = None
    # model_filename should be the absolute path on shared disk to your
    # best model. You need to ensure that they are available to evaluators on
    # Helios.

    #################################


    ###### DO NOT MODIFY THIS SECTION ######
    print("\nEvaluating results ... ")
    y_pred = eval_model(dataset_file, model_filename)

    assert type(y_pred) is np.ndarray, "Return a numpy array of dim=1"
    assert len(y_pred.shape) == 1, "Make sure ndim=1 for y_pred"

    results_fname = Path(results_dir) / (group_name + '_eval_pred.txt')

    print('\nSaving results to ', results_fname.absolute())
    write_memfile(results_fname, y_pred)
    #########################################