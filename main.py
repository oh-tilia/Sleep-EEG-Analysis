import pandas as pd
import mne
import seaborn as sns
import matplotlib.pyplot as plt

# load edf file
edf_file = 'sub-1_task-Sleep_acq-psg_eeg.edf'

# open the edf file and read it with mne
raw = mne.io.read_raw_edf(edf_file, preload=True)   
time = raw.times
channel_names = raw.ch_names

# create a dataframe with the data, time and channel names in pandas
edf_data = raw.get_data()
edf_data = pd.DataFrame(edf_data.T, columns=channel_names)
edf_data['time'] = time

# select only the columns we need for analysis
sleep_data = edf_data[["time", "PSG_F3", "PSG_C", "PSG_ECG", "PSG_EOG", "PSG_EMG"]]
print(sleep_data.head())

# create another df with time and sleep labels from json file
json_file = 'sub-1_task-Sleep_acq-psg_eeg.json'
labels_data = pd.read_json(json_file)

#concatenate both dfs on the time column

# sub samples the dataframe every 30s 


# plot all signals on a 5x1 grid


#plot all signals in one graph with time on x axis and signal values on y axis
