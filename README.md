## Usage
Execute the following shell command in this folder to run the cellular automaton and export the resulting matrix to an image file (with f1 and f2 set to 204 as default):

`python ./main.py`

The script comes with a simple commandline interface. Show the available parameters and their descriptions by running

`python ./main.py --help`

The exported image file will be named according to the parameter values you pass in.
For example:

`python ./main.py -t 500 -l 0.3 -f1 10 -f2 204`

will result in the image file name **timesteps-500\_\_f1-10\_\_f2-204\__lambda-0.3.png**, exported to the top-level directory (i.e. the directory in which this readme file is located).
