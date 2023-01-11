import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please Enter a City From(Chicago, New York City, Washington): ').title()
    while city not in ['Chicago', 'New York City', 'Washington']:
        print('Invalid City')
        city = input('Please Enter a City From(Chicago, New York City, Washington): ').title()
    print('You Eneterd ',city)
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please Enter a Month From January To June To Filter Data With or all For no Filter: ').title()
    while month not in ['January', 'February', 'March', 'April', 'May', 'June', 'All']:
        print('Invalid Month')
        month = input('Please Enter a Month From January To June To Filter Data With or all For no Filter: ').title()
    print('You Entered ', month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please Enter a Day Of Week or All For no Filter: ').title()
    while day not in ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'All']:
        print('Invalid day')
        day = input('Please Enter a Day Of Week or all For no Filter: ').title()
    print('You Entered ', day)


    print('-'*40)
    return city, month, day


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
    #load the csv data file for the entered city
    df = pd.read_csv(CITY_DATA[city])
    #convert start time column from str to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #make new column of months extracted from Start Time column 
    df['month'] = df['Start Time'].dt.month
    #make new column of days extracted from Start Time column 
    df['day'] = df['Start Time'].dt.day_name()
    #filter data by the chosen month
    if month != 'All':
        months = {'January': 1,
                  'February': 2,
                  'March': 3,
                  'April': 4,
                  'May': 5,
                  'June': 6
                 }
        #months = ['January', 'February', 'March', 'April', 'May', 'June']         
        month = months[month]
        #month = months.index(month) + 1
        df  = df[df['month'] == month]
    #filter data by chosen day
    if day != 'All':
        df = df[df['day'] == day]



    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print()

    # TO DO: display the most common month
    print('The Most Common Month is: ', df['month'].mode()[0])
    print()

    # TO DO: display the most common day of week
    print('The Most Common Day Of Week is: ', df['day'].mode()[0])
    print()

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The Most Common Start Hour is: ', df['hour'].mode()[0])
    print()




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The Most Common Start Station is:', df['Start Station'].mode()[0])
    print()


    # TO DO: display most commonly used end station
    print('The Most Common End Station is: ', df['End Station'].mode()[0])
    print()


    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End Station'] = df['Start Station'] + ' To ' + df['End Station']
    print('The Most Frequent Combination Of Start&End Station Trip is: ', df['Start To End Station'].mode()[0])
    print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    print('Total Travel Time is: ', datetime.timedelta(seconds = total_travel_time))
    print()
    

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time is: ', datetime.timedelta(seconds = mean_travel_time))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The Counts Of User Types is:\n', df['User Type'].value_counts())
    print()


    # TO DO: Display counts of gender
    try:
        print('The Count Of Each Gender is:\n ', df['Gender'].value_counts())
        print()
    except:
        print('Oops!, Gender Is Not Available')
        print()


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The Earliest Year Of Birth is: ', df['Birth Year'].max())
        print()
        print('The Most Recent Year Of Birth is: ', df['Birth Year'].min())
        print()
        print('The Most Common Year Of Birth is: ', df['Birth Year'].mode()[0])
        print()
    except:
        print('Oops!, Birth Year Is Not Available')
        print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    Asks the user to display raw data and display it if user prefer
    Asks the user to display more raw datav and display it if user prefer

    """
    print('Would You Like To Display Raw Data?')
    user_input = input('Please Enter Yes or No: ').title()
    while user_input not in ['Yes', 'No']:
        print('Invalid Input')
        user_input = input('Please Enter Yes or No: ').title()
    print('You Entered ', user_input)
    row_num = 0
    while user_input == 'Yes':
        raw_df = print(df[row_num : row_num + 5])
        print('Would You Like To Display More Raw DAta?')
        user_input = input('Please Enter Yes or No: ').title()
        while user_input not in ['Yes', 'No']:
            print('Invalid Input')
            user_input = input('Please Enter Yes or No: ').title()
        print('You Entered ', user_input)
        row_num += 5

    
    




    




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
