import pandas as pd                  #importing pandas
import numpy as np                   #importing numpy
##from PIL import Image
##import NANI.jpg                    #importing a meme
import time                          #importing time functions

#Data files for the cities, list of cities  
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    ## TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #I used this sourcecode for reference, because my code was not working                
    #previously: https://knowledge.udacity.com/questions/244964
    #input function https://docs.python.org/3/tutorial/inputoutput.html
    
    ## I wanted to try a little gimmick with a meme as an output. I tried to make it work but it didn´t. I left it commented here       for further attempts. 
    ##while True:
    ##    doubting_intention = input('Would you like to see data for some major cities in the US?: ').lower()      
    ##    if doubting_intention == 'yes':
    ##        print('Well done, you can continue')
    ##    elif doubting_intention == 'no':
    ##        img_PIL = Image.open('NANI.jpg')
    ##        img_PIL.show()
    ##    else:
    ##        print('Once again please. My code is not accomodating your needs.')
   
    #selecting a city
    ##https://www.w3schools.com/python/ref_dictionary_keys.asp for reference
    
    #I added some explanations regarding the possible options as mentioned in the review. 
    while True:
        city = input('Would you like to see data for New York City, Chicago or Washington?: ').lower()
        if city not in CITY_DATA.keys():
            print("Sorry bro. That's not possibro. Please select either New York City, Chicago or Washington.")
        else:
            break
 
    #defining months
    #using the while loop
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while True:
        month = input("Which month would you like to look at? You can select either 'all' or a month from January till June ").lower()
        if month not in months:
            print("Sorry bro. That's not possibro. Please select 'all' or one month from January till June.")
        else:
            break

    #defining day
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Which day would you like to look at? You can either select one day or you can select 'all' days.").lower()
        if day not in days:
            print("Sorry bro. That's not possibro. Please select 'all' or just one day of the week.")
        else:
            break

    print('-'*40)
    return city, month, day

#Script should prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.
def raw_data(df):
    raw = input('Would you like to see some rawr bea.., I mean 5 lines of raw data?')
    raw_start = 0
    if raw.lower() == 'yes':
        while True:
            print(df.iloc[raw_start:raw_start +5])
            raw_start += 5
            rawr = input('Would you like to see another 5 rawrs? Yes or No?')
            if rawr.lower() != 'yes':
                break
    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #I compared my code with the following code snippet https://knowledge.udacity.com/questions/317358.
    ##load data file
    df = pd.read_csv(CITY_DATA[city])
    
    ##converting of the Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    ##extraction of month and day
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    
    ##filter month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    ##filter day
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    ## TO DO: display the most common month
    #using mode https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html
    most_common_month = df['month'].mode()[0]
    print(f'The Most Common Month: ', most_common_month)
    
     
    # TO DO: display the most common day of week
    #same structure as in month
    most_common_day = df['day'].mode()[0]
    print(f'The Most Common Day: ', most_common_day)

    # TO DO: display the most common start hour
    #same structure as above
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    
    print(f'The Most Common Start Hour: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print(f'The Most Commonly Used Start Station Is: {most_commonly_used_start_station}')

    # TO DO: display most commonly used end station
    #same structure as above
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print(f'The Most Commonly Used End Station Is: {most_commonly_used_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df['Start Station'] + ' to ' + df['End Station']
    print(f'The Most Frequent Combination Is: from {most_frequent_combination.mode()[0]}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # it should print out seconds, minutes, hours and days
     
    total_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    seconds = total_travel_time.seconds % (60*60) % 60
    minutes = total_travel_time.seconds % (60*60) // 60
    hours = total_travel_time.seconds // (60*60)
    days = total_travel_time.days
    
    # TO DO: display mean travel time
    # same structure as above
    
    mean_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    seconds = mean_travel_time.seconds % (60*60) % 60
    minutes = mean_travel_time.seconds % (60*60) // 60
    hours = mean_travel_time.seconds // (60*60)
    days = mean_travel_time.days
                
    #personal note: don´t forget to put in f    
    print(f'Mean Travel Time: {days} days {hours} hours {minutes} minutes {seconds} seconds')             

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html for         reference
    print(df['User Type'].value_counts())
    print('\n\n')

    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
        print (df['Gender'].value_counts())
        print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    # https://knowledge.udacity.com/questions/544049
        print('Birth Year Data:')
    
        earliest_year_of_birth = df['Birth Year'].min()
        print('\n Earliest Year Of Birth:\n',earliest_year_of_birth)
    
        most_recent_year_of_birth = df['Birth Year'].max()
        print('\n Most Recent Year Of Birth:\n', most_recent_year_of_birth)
    
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('\n Most Common Year Of Birth:\n', most_common_year_of_birth)
    
    
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
