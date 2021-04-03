# yapet2bitwarden

Convert Yapet csv files to import them in Bitwarden

## How To
* Export your Yapet vault into a csv file with `yapet2csv -H src.pet dst.csv`
* Edit `yapet2bitwarden.py` and set:
  * `yapet_filename` should have the name of the csv file created with the previous command. For example `dst.csv`
  * `bitwarden_filename` is the name of the csv file that will be created and that you could import in Bitwarden
  * `folder_name` the name of the folder that will be created in Bitwarden when you import the previous file
* Run `python yapet2bitwarden.py`
* Import the vault in Bitwarden Web going to  `Tools` > `Import Data` > Select `Bitwarden (csv)` > Click on `Browse` and select the converted csv file > Click on `Import Data`
