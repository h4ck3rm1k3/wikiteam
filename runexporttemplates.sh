export PYTHONPATH=/home/mdupont/experiments/wikipedia/wikiteamgit/
cd /home/mdupont/experiments/wikipedia/wikiteamgit/data
python /home/mdupont/experiments/wikipedia/wikiteamgit/templatedumpgenerator.py   --api=http://en.wikipedia.org/w/api.php --xml

# now upload the wikia
cd /home/mdupont/experiments/wikipedia/pywikipediabot/
python process.py
