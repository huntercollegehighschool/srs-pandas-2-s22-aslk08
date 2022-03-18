"""
We'll be using the pandas (short for panels of data) module to analyze a large dataset.
"""

"""
1. The conventional way to import the pandas module is below. Note that the "as pd" part is optional (but widely used). You may want to run your code after importing pandas to let replit install it.
import pandas as pd
"""
import pandas as pd

"""
2. This folder contains a large .csv (spreadsheet) file named ign.csv. Import the data stored in the csv as a dataframe to Python and store it in a variable. The indices should be the names of the games, not the integers starting from 0 (you'll have to look at the .csv file to see which column the game titles are.)
<variable> = pd.read_csv('<filename/url>', index_col = <column number>)
"""
df = pd.read_csv("ign.csv", index_col = 2)

"""
3. Recall how you can index dataframe columns by their column name. For example, reviews['release_year'] would return a dataframe containing only the index (game title) and the year that game was released.

The code framework below allows pandas to identify the unique values in a column. Use that to find all the different score phrases that are used. Print the result.
<var> = <dataframe column>.unique()
"""
uni = df['release_year'].unique()
print(uni)



"""
4. It'd be nice to now how many games were described as great, awful, painful, and so on. Use the .value_counts() function to find that, and print the result.
<var> = <dataframe column>.value_counts()
"""
rating = df["score_phrase"].value_counts()
print(rating)


"""
5. I don't know about you, but I'm not sure which is worse, unbearable or painful. We can loop through each unique score phrase, create a dataframe containing games with that score phrase, and find those average scores. This will involve a for loop, Boolean indexing, and the .mean() function. Some helpful code is below.
<dataframe>[<dataframe>["<column name>"]==<string>]["<column name>"].mean()
"""

for rate in df["score_phrase"].unique():
  print(rate, df[df["score_phrase"]==rate]["score"].mean())
  

"""
for phrase in phrases:
  print(phrase, reviews[reviews["score_phrase"]==phrase]["score"].mean())
"""


"""
6. Use the .value_counts() function to determine which year in the dataset had the most game releases.
"""

years = df['release_year'].value_counts()
print(years)


"""
7. Use the .value_counts() function to determine in which month most games are released.
"""
months = df['release_month'].value_counts()

"""
8. Let's analyze platforms. Use the .unique() function to find all the different platforms that are in the dataset, and then loop (like you did in #5) to find the average score given to games on each platform.
"""

plat = df["platform"].unique()
for pl in plat:
  print(pl, df[df["platform"]==pl]["score"].mean())

"""
9. Use the .describe() function to get some summary statistics on the dataset.
<var> = <dataframe>.describe()

If you try to print to the console, it will be hard to see. Save the information to a .csv file.
<dataframe>.to_csv('<filename>.csv')
"""

des = df.describe()
des.to_csv("description.csv")

"""
10. Moving forward, it may be easier to work with a more concise dataframe containing only certain columns. reviews[['release_month', 'release_day']] would return a dataframe containing only the index(game title), release month and release day. (Note the double brackets.)

Create a dataframe containing only the index, score, and platform.
<var> = <dataframe>[[<column name>, <column name>]]
"""

isp = df[["score", "platform"]]

"""
11. On the new concise dataframe you created in #10, run the .sort_index() function. What does it look like it does?
<dataframe> = <dataframe>.sort_index()
"""

s_isp = isp.sort_index()


"""
12. Let's create two new dataframes, one containing only Pokemon games, and one containing only Zelda games. The code below will help you with that. Print both dataframes.
<var> = <dataframe>[<dataframe>.index.str.contains(<string>)]
"""

poke = df[df.index.str.contains("Pokemon")]
zel = df[df.index.str.contains("Zelda")]

"""
13. Let's sort the Pokemon games from highest rated to lowest rated. The code below will help you with that.
<var> = <dataframe.sort_values(by = [<column name>], ascending = False)>
"""

high = poke.sort_values(by = ["score"], ascending = False)
