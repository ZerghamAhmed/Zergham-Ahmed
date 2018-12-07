We used the inspiration of psets like survey, finance, similarities to create a program that, from a list of courses that the user has
inputted (selected from a drop-down menu that we imported of all of the STEM courses explicitly mentioned in the handbook as requirements
[doesn’t encapsulate all classes or even all STEM classes]), compares courses the students has taken with the course requirements.

First the user is directed to the home page through the flask app route just as in finance. This weaves simple html, jinja, flask and python
programming together to dynamically display a home page with a navbar (implemented with bootstrap) that leads to the different pages of the program.

We start with a registration page written in html very similar to that of the finance problem set, with sections for username, password,
and confirmed password, storing them as values. We use those values in a python function to check that that username or password has not
been used before. We used a form to prompt the user to enter this information and then used if (or if not) statements to ensure that
the user entered all necessary information, has a password and confirmation password that match, and did not enter a username that is
already in use and return apology messages accordingly. The registered users are saved into a SQL databse, so that they can use the same
username and password to log back in.

The login page uses the same structure as finance and follows the same principles as the register page. It uses a SQL query to check if the
user exists in our database, then if it does, logs the user in.

If there were no errors, we passed the user to a page where they could chose between finding their own concentration match or that of their blocking group.

Once the user chooses between these two options, they are brought to a page where they enter either their own classes or the class of
their whole blocking group.

For the individual match, we used pandas, which was a document we came about from searching stack overflow for research on how to
iterate over a csv file. Pandas is easy to use since you can iterate over columns of csv data easily by refering to them.
Here is the stack overflow post that we used as inspiration: https://stackoverflow.com/questions/28218698/how-to-iterate-over-columns-of-pandas-dataframe-to-run-regression
Then, we simply looked at the Pandas manual on how to use Pandas: https://pandas.pydata.org/pandas-docs/stable/10min.html

We used pd.read_csv() to store the csv in our application.py and a for loop (after opening the csv with all the required courses for each
concentration) to read through the csv file in python. The match.html file allows the student to class names as input (using request.form.get)
into a form by choosing the classes they've taken from a dropdown menu. We borrowed the code on how do to make a dropdown menu for the value a user
has to enter from this website: https://blog.teamtreehouse.com/creating-autocomplete-dropdowns-datalist-element which parses through
(using javascript) the available courses left from the list of total courses that are required for all STEM concentrations, based on the letters or numbers the user
has already entered. We then store the inputted courses from this form into a list called "courses".

Then we made an empty list of best fit concentrations (called overlap) that we wanted to fill later with matched concentrations. Then, we iterate over the columns
of our csv which has all the courses, with the courses for each concentration in a column for that concentration. We iterated over it using a for loop
and we stored those columns in a set then intersected it with a set that we made out of the list "courses". This returned a set that contained the
name of all the concentrations that had even a single match with the "courses" list, and if the length of that set was greater than an initial count we had (the count was initially set to 0), then we
made the set equal to the count and appended that count to the empty list talked about earlier.

Next, we wanted to determine which of these concentrations had the most intersections. So, we used the max function that comes with Python for sets.
We set this equal to a variable called best, and made an initial counter called match that we wanted to edit later. Then, we iterate over the columns
of our csv once more (in order to make sets of each concentration that includes the number of courses matched with the list of inputed courses then we
return another set intersection of the columns and courses. Then, we we know if the length of this set is equal to best, which is the set of
the concentration with the greatest number of matches, then we want it to print the col (which is the best matched concentration). This was to test out,
in just our python program, whether or not the match was successfully made.

Overall, the individual matching worked in two routes. First there was a route to the select menu (with def match and match.html being the
files for this route) with the course input options for the user, which used the csv reader and a for loop to read line by line a list of every single Harvard course. Then, we took the
results of this and returned it as options and passed it through flask to display the select menus.
Next, we had a route to a function called pair and pair.html which simply displayed the results of our code that we explained above.
This was based on quote from finance.

For the blocking group feature, the exact same structure is used, except that there are more requests made for courses, thus
a larger pool of data is used to find a best fit concentration for the blocking group.

To make the csv file of all the course requirements for each concentration, we went through the Harvard College handbook online and
made an excel sheet of all the required courses listed for each STEM concentration we saw. We limited it to STEM concentrations because
social sciences and arts & humanities concentrations did not have definitive course names for their concentration requirements, and
we wanted students to be able to simply enter in courses they had taken rather than spend time deciding whether the courses they have
taken fit the criteria of a less defined concentration requirement. We pasted these required courses from STEM concentrations into an excel
sheet where the columns were each concentration with a list of required courses (we did this rather than scraping the handbook because
much of the time, concentrations have unique stipulations for course requirements [e.g. "course XXXX will NOT count for this divisional
credit", having optional courses like thesis tutorials, etc.], so if we had just gone off of what courses were mentioned in the handbook
the program may have counted courses that shouldn't count directly toward concentration requirements). We then compiled a list of all
courses available from this spreadsheet, so we could use that list as our dropdown menu.



