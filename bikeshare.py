import time
import sys
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
          city = input("Which city would you like to filter by? new york, chicago or washington?\n").lower() 
          
          if city not in ("new york", "chicago", "washington"):
            print("Sorry, I didn't catch that. Try again.")
            continue
          else:
            break

    while True:
          month = input("Which month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n").lower()
          if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Sorry, I didn't catch that. Try again.")
            continue
          else:
            break

        
    while True:
          day = input("Are you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n").lower()
          if day not in ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"):
            print("Sorry, I didn't catch that. Try again.")
            continue
          else:
            break

    
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month =  month.index(month) + 1
        df = df[ df['month'] == month ]
    elif day != 'all':
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('most common month is :  ',df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('most common day of week is : ',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('most common hour of day is : ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most common start station\n',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('most common End station\n',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['common_trip'] = df['Start Station']+df['End Station']
    print('most common trip \n',df['common_trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is : ',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('average travel time : ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of each user type.\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns :
        print('counts of each gender\n',df['Gender'].value_counts())
        print('most common year of birth\n',int(df['Birth Year'].mode()[0]))
        print('most recent year of birth\n',int(df['Birth Year'].max()))
        print('earliest year of birth\n',int(df['Birth Year'].min()))
    else:
        print(" No Gender in Washungton Dataset")
        
    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    keep_asking = True
    if view_data == 'yes':
        while (keep_asking):
            print(df.iloc[start_loc : start_loc + 5])
            start_loc += 5
            view_display = input("Do you wish to continue? (yes or no): ").lower()
            if view_display == "no": 
                keep_asking = False
    elif view_data == 'no' :
        keep_asking = False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)   
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        while True:
            restart = True
            restart = input('\nWould you like to restart? Enter yes if you need to restart or no if you need to exit.\n')
            if restart.lower() == 'yes':
                return main()
            elif restart.lower() == 'no':
                sys.exit()

if __name__ == "__main__":
	main()

	
