
# coding: utf-8

# #Homework
# 
# You can find the complete dogs.csv at http://jonathansoma.com/lede/dogs.csv. Using a new IPython notebook, find out...
# 
# How many dogs are registered in New York City? Hint: if you check out the IPython notebook above, it talks about how to convert the csv.reader variable into a list, which might give you an easy way to do it.
# 
# - How many dogs are registered in Brooklyn? Staten Island? Queens? Manhattan? Bronx?
# - How many dogs are named Max in the Lower East Side?
# - How many dogs are named Max in Bed Stuy?
# - How many dogs have the color brindle as their first or second color?
# - Ask the user for their name (you're gonna have to Google how to get user input in python!). Then find out how many dogs in New York have that name.
# - Remember to add in comments about where you found answers and what you're trying to do during each step!
# 
# When you've done what you can (...everything, right?), save the IPython notebook by going to File > Download as... and click IPython Notebook. A .ipynb will be downloaded to your computer. E-mail that file as an attachment to jonathan.soma@gmail.com.

# In[13]:

#Import libraries
import urllib
import csv

#Retrieve file, open, delimit and assign to a variable, then assign to a list
urllib.urlretrieve("http://jonathansoma.com/lede/dogs.csv", "dogs.csv")
dogs = open("dogs.csv", "rb")
dogs_csv = csv.reader(dogs, delimiter = ',')
dogs_list = list(dogs_csv)


# In[14]:

# Count number of dogs using a count of rows in our dogs list.
len(dogs_list) - 1


# #####How many dogs are registered in Brooklyn? Staten Island? Queens? Manhattan? Bronx?

# In[15]:

# Call count variables 
brooklyn_count = 0 
si_count = 0 
queens_count = 0 
manhattan_count = 0 
bronx_count = 0 

# For loop that looks at the 10th column for Borough, then adds to the count if it matches the borough.
for dog in dogs_list:
    if dog[9] == "Brooklyn":
        brooklyn_count = brooklyn_count + 1
    elif dog[9] == "Staten Island":
        si_count = si_count + 1
    elif dog[9] == "Queens":
        queens_count = queens_count + 1
    elif dog[9] == "Manhattan":
        manhattan_count = manhattan_count + 1
    elif dog[9] == "Bronx":
        bronx_count = bronx_count + 1

# Printing our results
print "The numbers of dogs registered in Brooklyn, Staten Island, Queens, Manhattan, and the Bronx are as follows: "
print " Brooklyn = " + str(brooklyn_count)
print " Staten Island = " + str(si_count)
print " Queens = " + str(queens_count)
print " Manhattan = " + str(manhattan_count)
print " Bronx = " + str(bronx_count)


# #####How many dogs are named Max in the Lower East Side?

# In[16]:

# List of LES zip codes
les_zip_list = ["10002", "10003", "10009"]

count = 0
# For loop that counts if first column and last column in each dog row within the list of dogs has Max and a LES zip code, then prints the results.
for dog in dogs_list:
    if dog[0] == "Max" and (dog[-1] in les_zip_list):
        count = count + 1
print "There are " + str(count) + " dogs named Max in the LES."


# #####How many dogs are named Max in Bed-Stuy?

# In[17]:

# List of Bed-Stuy zip codes
bed_stuy_zip_list = ["11205", "11206", "11216", "11221", "11233", "11238"]

count = 0

# For loop that counts if first column and last column in each dog row within the list of dogs has Max and a Bed-Stuy zip code, then prints the results.
for dog in dogs_list:
    if dog[0] == "Max" and (dog[-1] in bed_stuy_zip_list):
        count = count + 1

print "There are " + str(count) + " dogs named Max in Bed-Stuy."


# #####How many dogs have the color brindle as their first or second color?

# In[18]:

count = 0

# For loop that counts if the 5th and 6th columns in each dog row within the list of dogs has BRINDLE, then prints the results.
for dog in dogs_list:
    if dog[4] == "BRINDLE" or dog[5] == "BRINDLE":
        count = count + 1

print "There are " + str(count) + " dogs named Brindle as their first or second color."


# #####Ask the user for their name (you're gonna have to Google how to get user input in python!). Then find out how many dogs in New York have that name.

# In[21]:

# Asks user for name, then a list comprehension that collects the dog row information into a list called matching_dogs if the user name matches, then prints the results.
# Found documentation on raw_input here: http://stackoverflow.com/questions/5563089/raw-input-function-in-python
user_name = raw_input("What is your name? ") 
matching_dogs = [dog for dog in dogs_list if dog[0] == user_name]
print "There are " + str(len(matching_dogs)) + " dogs named " + user_name + " in New York."


# In[ ]:



