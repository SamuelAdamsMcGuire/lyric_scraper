Lyrics Recognition Project

This project was a lesson in webscraping and using text classification to 
recognize lyrics from different msuicians using a compiled dataframe.

I broke the project into 5 parts and in turn 5 programs. If the user goes through
the programs in order in the end they will have a predictor based on the musicians
they chose to scrape from the lyrics.com website.

1) artist_websearch: this asks for the desired musician and returns a link to the
artist's website. It is bascially an iterface with the search line from lyrics.com

2) webscraper: this program will scrape lyrics from the give artist. It will go through
each song link and grap the lyrics and store them in a dataframe (I am currently trying 
to add argparse to the program

3) lyric_compiler_function: this program will iterate through the saved .csv files in the 
local directory and compile them into one large dataframe. This goes under the assuption 
tha the user will not have any other .csv file in the directory where they saved the 
programs

4) model_bow_generator: this program just will generate the bag of words and model used to 
make the artist prediction. There is no user interface here. I also did not try too many 
different models. I spent more time on working on my low leve programmin skills. At the end
of the program a model and a bow are made presistant so they can be used in the final program
without haveing a even longer time delay.

5) artist_pred: asks for the user to enter any song text and the output is the artist from 
the compiled dataframe that would most likey have said or would say these lyrics. I used 
a while loop so that the program would only have to be uploaded once and then it would work 
fast. Once the user wants to exit they must type break with no quotation marks.

What I would like to improve:

1) I would like to get more models and hyperperameters.
2) Would like to add some code to remove songs that are scrape multiple times
3) improve the interface between the programs, automate it a bit more


