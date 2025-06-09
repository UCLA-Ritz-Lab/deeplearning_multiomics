# deeplearning_multiomics

Project using Tensorflow to integrate multiple omics sources into a deep learning network.  Architecture is inspired by "visible networks" idea as highlighted in GenNet paper:

https://www.nature.com/articles/s41540-024-00405-w

Hidden layers can represent Parkinson's Disease gene networks.

## Setup

- Install Anaconda to create an isolated Python environment by visiting:

 https://www.anaconda.com/download

- At this point to avoid version issues you can create a notebook environment for Tensor flow and the notebooks. From the base directory of this repo:

	conda create -n omics python=3.12.2 jupyter tensorflow scipy pandas matplotlib
	conda activate omics
	jupyter-notebook --ip=127.0.0.1

- Download the input data (dataset.tfrecords) and metadata (feature_dict.pkl) from 

https://app.box.com/folder/165663162890

Save these files in a folder called data located on the same level as notebooks.


- ntact me (garyc@caseyandgary.com) if you need dataset.tfrecords and feature_dict.pkl.  These are the input data and its metadata for the PEG1 case control omics data. These should be saved under a directory called data on the same level as notebooks.


