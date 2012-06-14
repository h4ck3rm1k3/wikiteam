export PYTHONPATH=$HOME/experiments/wikiteam/
cd ${HOME}/experiments/wikiteam/data
python $HOME/experiments/wikiteam/dumpgenerator.py   --api=http://en.wikipedia.org/w/api.php --xml

# now upload the wikia
cd $HOME/experiments/pywikipediabot/
python process.py
