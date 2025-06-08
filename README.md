# deeplearning_multiomics

Project using Tensorflow to integrate multiple omics sources into a deep learning network.  Architecture is inspired by "visible networks" idea as highlighted in GenNet paper:

https://www.nature.com/articles/s41540-024-00405-w

Hidden layers can represent Parkinson's Disease gene networks.

## Setup

- Install Anaconda to create an isolated Python environment by visiting:

 https://www.anaconda.com/download

- At this point to avoid version issues you can create a notebook environment for Tensor flow and the notebooks. From the base directory of this repo:

	conda create -n omics python=3.12.2 jupyter tensorflow
	conda activate omics
	jupyter-notebook --ip=127.0.0.1

- Navigate to the notebooks folder when the browser opens the notebook.  Open peg.ipynb

- Please contact me (garyc@caseyandgary.com) if you need dataset.tfrecords and feature_dict.pkl.  These are the input data and its metadata for the PEG1 case control omics data. These should be saved under a directory called data on the same level as notebooks.


