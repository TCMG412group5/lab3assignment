# Lab 3 Assignment
Python assignment for lab 3.

## Instructions for Lab 3:
Here’s the scenario: you work for a medium sized company that sells widgets directly to consumers through brick-and-mortar retail stores. The marketing department wants to try a new promotional campaign to ramp up direct internet sales, but needs better data about current traffic to your website. Your boss has asked you to take the HTTP server logs from the webserver and provide some analytics to Marketing.

### STEPS:
1. Your program will be parsing and analyzing log files from an Apache web server. The first thing your program must do is retrieve the log file across the network. It is available here: ./http_access_log

2. Once you download the file, you need to save a local copy to disk (a cached copy) so the next time you run your script, you don't have to wait for the download.

3. Marketing wants to know two things: 
    * How many total requests have been made in the 6 months?
    * How many total requests were made in the time period represented by the log?

4. You will need to output this data to the screen. The format you choose to do this is up to you, but your decisions and your implementation should be logical and consistent.