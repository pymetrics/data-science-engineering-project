# pymetrics Data Science Engineering Project
Welcome to the pymatrix challenge! We're excited that you've expressed interest in working at pymetrics as a Data Science Engineer, and we look forward to see what you can build. For this role, we are looking for someone with strong python programming skills, proficient in using and building efficient data structures and algorithms, and a general understanding of machine learning techniques and procedures. If you've stumbled upon this repository and are also interested in applying, please feel free to continue reading and complete the project to begin your application.

# What you'll build
For this project you will build a command line application called `pymatrix`, which is a tool for working with matrices. We have provided some skeleton code, and your task will be to fill in the implementation of the different subcommand methods. You will need to handle reading in and managing matrix data of different formats and then perform some operation on the data. 

To help create a command line tool that is quick to setup, easily configurable, and beautiful we are making use of the python package [Click](http://click.pocoo.org/5/), take a look at the documentation if you would like to learn more. The provided skeleton code has a subcommand `echo` that will show you the basics you would need for reading in arguments and options from the command line.

# Getting Setup
First clone this repository locally and create a python 2.7 virtual environment to work in (personally I like to use [Conda](https://conda.io/docs/index.html)). Next, you will want to install the `pymatrix` command line tool itself. This project is pip installable so to make testing of your code easy run `pip install --editable .` and you should now be able to use the command line tool--verify this by running `pymatrix --help`. Using the `--editable` mode will make development and testing easier as any changes you make to the source will automatically be reflected in the command line tool without having to run `pip install` again. If you want to add additional python packages to use, include them in the `install_requires` list of the setup.py file and then in this case run `pip install --editable .` again. 

# Data formats for pymatrix
There are some sample data files provided in the [data](./data/) directory to help you with your testing and understanding of the expected data formats. The json-data format should be able to accept both a valid json string written on the command line or loading json from a file. The csv-file option will read a csv file that use `,` as a delimiter and `\n` for line breaks, there is no header row. The pickle-file will read in a file that was produced via `pickle.dump`. The sparse-coo format will contain three numbers on each line separated by a single space, `row_index column_index value`.

# The Subcommands
Now we'll take a look at the subcommands for `pymatrix` and define the expected behavior of the tool.

### echo
This is a sample command that has already been completed for your reference and for getting comfortable with the tool. You can run `pymatrix echo --help` to get more information about the command and its invocation. For example you can test out the command by running `pymatrix echo -j "[[1,2],[3,4]]" 2`. Take a look at the implementation in [pymatrix.py](./src/pymatrix.py) to see how positional arguments and options are grabbed within the python function.

### closest_to
You will need to implement this command. The help menu for this command describes the functionality: it will "Find the row that is the minimal distance from row_i and optionally display the distance as well" where `row_i` is a positional argument for the row index of the matrix (we're all programmers here so 0 based indexing is cool with me). We want to find the index of another row, call it `row_j`, where `row_i != row_j` and the distance, `d(i,j)`, between `row_i` and `row_j` satisfies `d(i,j) < d(i,k)` for all `k != i,j`. You should use the euclidean distance by default, but if you want to make that a configurable option feel free to add it (the same goes for other commands that may use a distance measure too). Do not change the functionality or format of the predefined options, if you want to make the metric configurable add a new option. The output of the command will be the ordered indices seperated by a single space, for example `row_i row_j` if `row_i < row_j` else you will return `row_j row_i` if `row_j < row_i`. Again, we want to return only the indices and not the entire rows from the matrix. If the `--distance` argument is passed, then in this case you should also return the distance `d(i,j)` after the indices so the output may look something like `4 9 0.34215`, the distance should be rounded to 5 decimal places.

### closest
You will need to implement this command. The help menu for this command describes the functionality: it will "Find the N distinct pairs of rows that are the smallest distance apart and optionally display the distance as well." The calling signature of this command is the same as `closest_to` but now the positional argument is not a row index of the matrix but rather controls how many row pairs will be found and returned. The format of the output rows is the same as `closest_to` except there may be more that one line of output and they will be ordered by increasing distance. For example running a command like `pymatrix closest -f data/yourtestmatrix.csv 2` might return something of the following format:
```
4 6 
1 3
```
And if you wanted to include the distances `pymatrix closest --distance -f data/yourtestmatrix.csv 2`:
```
4 6 0.54311
1 3 1.34980
```

### furthest
You will need to implement this command. As you could probably guess, this command is the opposite of the `closest` command and as the help menu describes, it will "Find the N distinct pairs of rows that are the furthest distance apart and optionally display the distance as well". The behavior of the command in terms of the input and output format is the same as `closest` except the N returned rows of data are now in descending order in relation to the distance. For both `closest` and `furthest` note that the indices should again be ordered on the line as was done in `closest_to`. 

### centroids
You will need to implement this command. The help menu describes that the command will "Cluster the given data set and return the N centroids, one for each cluster". You have a lot of flexibility here to decide how you would like to best implement this command, if you want to add more options to better control the internals you may do so. The only requirements are that the command must be able to handle (at a minimum) the four data input types, provide a positional argument that will control the number of clusters to find, and then output the centroid vectors one per line. The print format of the vectors should include square brackets and the values do not have to be rounded to a given precision:
```
[1.2345, 2.2, 3.40983]
[5.6765, 9.0909, 0.001]
```

# Additional Questions
Please provide answers to some follow up questions in [QUESTIONS.txt](./QUESTIONS.txt). No need to write a novel for these questions, short and to the point will do.

# Submission
Please create a zip of this project with your name as part of the filename `pymatrix_challenge-FULL_NAME`. Do not include the egg that pip may have created, pyc files, or any large data sets you may have generated during your development. I will unzip your solution, create a fresh virtual environment, run `pip install .`, run a few tests to confirm things are working as expected, and then read through the code and question answers if all of the test cases passed. Use this form to submit your project https://goo.gl/forms/mUGQpCWwwzWo5vSv1
