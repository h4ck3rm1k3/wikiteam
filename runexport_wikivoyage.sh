#set -e 

export PYTHONPATH=$HOME/experiments/wikiteam/
cd ${HOME}/experiments/wikiteam/data
python $HOME/experiments/wikiteam/dumpgenerator-wikivoyage.py

echo going to run process
cd ${HOME}/experiments/wikiteam/data
#pwd
python $HOME/experiments/wikiteam/process_wikivoyage.py
rm -rf  ${HOME}/experiments/wikiteam/data/enwikivoya*
#rm -rf  ${HOME}/experiments/wikiteam/data/Api*
