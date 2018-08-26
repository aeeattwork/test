# test

v 1.0.0
- "--" sign is treated as punctuation.
- All words are converted to lowercase: lowercase and uppercase words are not being distinquished.
- Possible ways of extending the program:
  -- New file extensions could be added with very little change in the code. The following has to be changed:
    --- Possibly new function is required to process content of a file with a new extension
    --- Controller has to be modified to select above mentioned new function for processing content of file with new extension
    --- input function has to be modified to accept new extension
  -- New files could be added for processing their content:
    --- All functions are designed to process as many files as the user wishes. Currently, you can add new files to the code into the             input function. For processing mass amount of files at once, you only need to change the input function accordingly.

unittest_of_unique_values
- Testing whether there is any duplicate in the total of the three sets of unique values from the three different files.
- Requires input from user: path of input files.
