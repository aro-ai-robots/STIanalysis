# STIanalysis
Visualiztion for STI timeseries.

After running the insect-poison experiment an STIDUMP file should be created.  
To analyze this data:
	cd STIanalysis 
	chmod 777 split_data.py
	gedit split_data.py
    		Fix the paths on lines 26, 29, 30, 32, 33
	./split_data.py ~/WhereEverThisIsLocatedSTIDUMP.txt 
    
	
This will create csv files. It has a few bugs with the IIT matrix, but for the most part, runs like a charm. It makes three directories. IIT, Histograms, and a time series directory. The script will make a new file in each directory each time you run the script. This can fill up your directories pretty quick, so you can get a fresh start by running the clear_experiments.sh. 
    

The histograms directory will contain a file that has a few rows and one column. It makes a histogram of all the STI values. IT combines no matter the node. The number of bins is set to 100 by default. It can be changed within the script itself. Open this csv file in a ‘excel’ program. Graph it, bing batta boom, you just made a histogram of the STI values you just made. 
    

The IIT files are saved in the IIT directory. They will contain one matrix per file. They are supposed to be saved in a perfect matrix containing the sti’s. It is supposed to be organized by row and column. The rows should be the different nodes. Each entry in the first column is the names and UUID numbers. The next column is the first STI value in the time series. The following is the next and so on and so forth. 
 

