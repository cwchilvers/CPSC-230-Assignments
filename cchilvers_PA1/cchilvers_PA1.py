# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Population Estimation

import math

# Define initial population and print

population_2018 = (323100000)
print("The current US population is", population_2018)


# Define birth and death rates per second

birth_rate_second = 1/7
death_rate_second = 1/13


# Convert 2018 birth and death rates from per second to per (calendar
# common) year

seconds_year = 31536000
birth_rate = birth_rate_second * seconds_year / population_2018
death_rate = death_rate_second * seconds_year / population_2018

    
# Calculate poulation growth when 2018 birth & death rates stay constant and
# print results

population_2019 = population_2018 * math.e ** ((birth_rate - death_rate) * 1)
print("2019:", int(population_2019))

population_2020 = population_2018 * math.e ** ((birth_rate - death_rate) * 2)
print("2020:", int(population_2020))

