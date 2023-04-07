# WMATA Pass Analyzer
Upload your WMATA month data to see what monthly pass would have been the cheapest.

(Not affiliated with WMATA, I just use their trains and buses)

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

Here is an example output (March 2023, Data obtained using a $2.00 pass)
```
Product Type             Min Cost  Max Cost  
Stored Value             $171.20    $171.20    
Monthly Pass ($2.00)     $82.00     $82.00     
Monthly Pass ($2.25)     $90.00     $90.00     
Monthly Pass ($2.50)     $98.00     $98.00     
Monthly Pass ($2.75)     $106.00    $106.00    
Monthly Pass ($3.00)     $114.00    $114.00    
Monthly Pass ($3.25)     $122.00    $122.00    
Monthly Pass ($3.50)     $130.00    $130.00    
Monthly Pass ($3.75)     $138.00    $138.00    
Monthly Pass ($4.00)     $146.00    $146.00    
Monthly Pass ($4.25)     $154.00    $154.00    

```
