from os import listdir
import os.path
import glob

def GetDataset(folder_name, dataset_type):

    DATA_PATH = os.path.join('..', 'datasets', folder_name, 'LibriSpeech', f'{folder_name}-{dataset_type}')
    files = glob.glob(DATA_PATH + '/**/*.trans.txt', recursive=True)

    samples = []
    for file in files:

        with open(file) as f:

            lines = f.readlines()

            for line in lines:

                file_path = os.path.normpath(file).split(os.sep)[:-1]
                file_path.append(line.split()[0])
                file_path = os.path.normpath('/'.join(file_path) + '.flac')
                identifier = line.split()[0]
                label = line.split()[1:]
                samples.append((file_path, identifier, label))


    return samples
