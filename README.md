# WMATA Pass Analyzer
Upload your WMATA month data to see what monthly pass would have been the cheapest.

Warning: I wrote this for myself. I can in no way guarentee that it will produce accurate information in all cases. In the case that WMATA fares change, this program's output has no meaning.

Additionally, the true fare of a trip can be ambiguous in the case that it is less than what is covered by your pass (e.g. you have the $2.50 pass and went on a trip that cost $0.00. It is impossible to know if the true fare was $2.00, $2.50, or somewhere in between). This is why the results file lists both minimum and maximum costs for each pass.

## Use

* On the [SmarTrip website](https://smartrip.wmata.com/Account/Summary), click on your card.
* On the right side, click "Use History".
* Select the month you are interested in and click "Submit".
* On the right side of the page, click "Export to Excel". This will download a file.
* There is now a file in your downloads folder with a long name (something like "Card_Usage_...-mm.dd.yy.csv").
* copy this file and paste it somewhere else in your file system (such as "~/Documents").
* rename this file for convenience (like "data.csv")
* Now install this program. In a terminal, type `pip install git+https://github.com/tedjohnson12/wmata_pass_analyzer@main`
* In the terminal, navigate to your data file. Maybe that is `cd ~/Documents`
* Type `python3`
* Type `from pass_analyzer import read_month`
* Type `read_month('data.csv','results.txt)`
* Type `quit()` to exit python
* Now open "results.txt" in your favorite text editor. It should give you info on each pass.
