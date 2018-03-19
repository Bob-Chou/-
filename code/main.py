#!/usr/bin/python
import os

# Link to the UIUC Car Database
# http://l2r.cs.uiuc.edu/~cogcomp/Data/Car/CarData.tar.gz
# dataset_url = " "
# dataset_path = "../data/dataset/CarData.tar.gz"

# Fetch and extract the dataset
# if not os.path.exists(dataset_path):
#     os.system("wget {} -O {}".format(dataset_url, dataset_path))
#     os.system("tar -xvzf {} -C {}".format(dataset_path, os.path.split(dataset_path)[0]))

# # Extract the features
# pos_path = "../data/train/pos"
# neg_path = "../data/train/neg"
# os.system("python ./extract-features.py -p {} -n {}".format(pos_path, neg_path))

# # Perform training
# pos_feat_path =  "../data/features/pos"
# neg_feat_path =  "../data/features/neg"
# os.system("python ./train-classifier.py -p {} -n {}".format(pos_feat_path, neg_feat_path))

# Perform testing 
test_im_path = "../data/test/raw/test-001.png"
# test_im_path = "../data/test/raw/Selection_013.png"
# os.system("python ./test-classifier.py -i {} -d {} --visualize".format(test_im_path,1.25))
os.system("python ./test-classifier.py -i {} -d {}".format(test_im_path, 1.25))