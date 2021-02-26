# Kinetics - Downloader

## Usage
First, clone this repository and make sure that all the submodules are also cloned properly.
```
git clone git@github.com:jihun-kr/Kinetics-downloader.git
cd Kinetics-downloader
```

Next, setup your environment
```
conda create -n kinetics-downloader python=2.7
conda activate kinetics-downloader
sudo apt install gcc make
pip install -r requirements.txt
```

Finally, download a dataset split by calling:
```
mkdir <data_dir>; python download.py {dataset_split}.csv <data_dir>
```

