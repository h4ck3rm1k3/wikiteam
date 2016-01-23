#set -e 

export PYTHONPATH=$HOME/experiments/wikiteam/
pushd ${HOME}/experiments/wikiteam/data
python $HOME/experiments/wikiteam/dumpgenerator.py
echo going to run process
#pwd
python $HOME/experiments/wikiteam/process.py
popd
rm -rf  ${HOME}/experiments/wikiteam/data/enwikipedia*
#rm -rf  ${HOME}/experiments/wikiteam/data/Api*
