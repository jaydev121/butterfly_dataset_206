import pickle as pkl

with open('dataset_207.pkl', 'rb') as handle:
    data = pkl.load(handle)

data['annotations'].shape
data['images'].shape
