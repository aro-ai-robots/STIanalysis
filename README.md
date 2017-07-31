# STIanalysis
Visualiztion for STI timeseries.

After running the insect-poison experiment an STIDUMP file should be created.  
To analyze this data:
	cd STIanalysis 
	chmod 777 split_data.py
	gedit split_data.py
    		Fix the paths on lines 26, 29, 30, 32, 33
	./split_data.py ~/STIanalysis/STIDUMP.txt 
    This will create an csv files. It has a few bugs with the IIT matrix, but for the most part, runs like a charm. It makes three directories. IIT, Histograms, and a time series directory. The script will make a new file in each directory each time you run the script. This can fill up your directories pretty quick, so you can get a fresh start by running the clear_experiments.sh. 
    The histograms directory will contain a file that has a fel rows and one column. It makes a histogram of all the STI values. IT combines no matter the node. The number of bins is set to 100 by default and can be changed within the script itself. Open this csv file in a ‘excel’ program. Graph it, bing batta boom. 

