# We will utilize census data in the following problems:

# In[1]:

# Importing census and state libraries
from census import Census
from us import states

key = "some key I entered earlier"

# Initializing the object named Census to utilize its methods
c = Census(key)


# ###1. What's the code for people born in Slovakia or the Czech Republic?

# #### The code for people born in Slovakia or the Czech Repulic is B05006_032E was found in the following page:
# #### http://api.census.gov/data/2012/acs5/variables.html

# ###2. What's the total number of people born in Slovakia or the Czech Republic in the US?

# In[2]:

# Using the Sunlight Foundation's census library to take our query to utilize the Census API and convert output to a dictionary 
# Define variable as the c.acs function with an input of us for location and Czech Rep and Slovakia for the variable code)
# Variable codes here: http://api.census.gov/data/2012/acs5/variables.html
total_born_slovaks_czechs_in_us = c.acs.us(('NAME', 'B05006_032E'))
# Examine the structure of the list of dictionaries by evaluating: total_born_slovaks_czechs_in_us
print "There are " + total_born_slovaks_czechs_in_us[0]['B05006_032E'] + " people born in Slovakia or the Czech Republic in the US."


# ###3. How many people between the ages of 5 and 9 live in the ZIP code 11238?

# In[3]:

# Variable codes found at: http://api.census.gov/data/2012/acs3/variables.html
# Male 5-9 = B01001_004E, Female 5-9 = B01001_028E
output = c.acs.zipcode(('B01001_004E', 'B01001_028E'), '11238')
total = int(output[0]['B01001_004E']) + int(output[0]['B01001_028E'])
print "There are " + str(total) + " people between the ages of living in ZIP code 11238."


# ###4. Are there more Pakistani or Indian people in Queens County?

# In[4]:

# Variable codes found at: http://api.census.gov/data/2012/acs5/variables.html
# Pakistani = B02006_013E, Indian = B02006_002E
# Input into Census function with acs method
output = c.acs.state_county(('NAME', 'B02006_013E', 'B02006_002E'), states.NY.fips, ('81')) #note that the NY fips code = 36
# Checking the output and data structure
output


# In[5]:

# Use an if/else function to assign to list larger_list the larger group name and population, then output as a string.
Indian_pop = output[0]['B02006_002E']
Pakistani_pop = output[0]['B02006_013E']
if Indian_pop > Pakistani_pop:
    larger = larger[0:1] = ['Indian', Indian_pop]
else:
    larger = larger[0:1] = ['Pakistani', Pakistani_pop]
print "The larger group of people is " + larger[0] + " with " + str(larger[1]) + " people."


# ###5. What state has the most people who work in the hunting & fishing industry?

# In[6]:

# Variable codes found at: http://api.census.gov/data/2012/acs5/variables.html
# Hunting & Fishing = B24121_336E
c.acs.state(('NAME','B24121_336E'), Census.ALL)
# Data not found in that B24121_336E shows empty data

# Since data not found, checked 2012 figures in the ACS 3 Year data instead at: http://api.census.gov/data/2012/acs3/variables.html
# Found Hunting & Fishing = B08126_002E
hunt_fish_list = c.acs.state(('NAME','B08126_002E'), Census.ALL)

# Check list
hunt_fish_list

# Sort the list of state dictionaries by workers in hunting and fishing industry, the reverse to descending order, then print
hunt_fish_list = sorted(hunt_fish_list,key=lambda hunt_fish_list: int(hunt_fish_list['B08126_002E']))
hunt_fish_list.reverse()
hunt_fish_list
print "The State of " + hunt_fish_list[0]['NAME'] + " has the most people who work in the hunting and fishing industry with " + hunt_fish_list[0]['B08126_002E'] + "."


# ###6. What county in New York has the fewest people?

# In[7]:

# Assign retrieved Census population data for New York by county to a variable.
ny_county_pop_list = c.acs.state_county(('NAME', 'B01003_001E'), str(states.NY.fips), '*')
# Check to confirm output and data structure.
ny_county_pop_list
# Sort list in ascending order by population.
sorted_ny_county_pop_list = sorted(ny_county_pop_list,key=lambda sorted_ny_county_pop_list: int(sorted_ny_county_pop_list['B01003_001E']))
# Print output.
sorted_ny_county_pop_list
print "The county in New York with the fewest people is " + sorted_ny_county_pop_list[0]['NAME'] + " with " + sorted_ny_county_pop_list[0]['B01003_001E'] + " people."


# ###7. Make a list of states, ordered by the number of graduate degrees.

# In[8]:

# Variable codes found at: http://api.census.gov/data/2012/acs3/variables.html
# Bachelor's Degree = B06009_005E, Graduate or Profession Degree = B06009_006E

# Save retrieved list of Census state dictionaries to a variable 
states_degrees = c.acs.state(('NAME','B06009_005E','B06009_006E'), '*')

# If state has no value output 0 for total degrees else output integer state degrees
for state_degree in states_degrees:
    if state_degree['B06009_005E'] == None or state_degree['B06009_006E'] == None:
        state_degree['total_degrees'] = 0
    else:
        state_degree['total_degrees'] = int(state_degree['B06009_005E']) + int(state_degree['B06009_006E'])
# Print to check if the loop works correctly
    print [state_degree]
# Check list of all state degree totals
print [state_degree['total_degrees'] for state_degree in states_degrees]

# Sort the list of state dictionaries by total degrees, the reverse to descending order, then print
Degrees_list = sorted(states_degrees,key=lambda Degrees: Degrees['total_degrees'])
Degrees_list.reverse()
Degrees_list


# In[ ]:



