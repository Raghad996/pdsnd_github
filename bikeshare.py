import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Here is the month list and day list
month_list=['january', 'february', 'march', 'april', 'may', 'june','all']
day_list=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
#Here will check user inputs
def check_user_input(user_input,i_type):
    while True:
            i_u=input(user_input).lower()
            try:
                if i_u in ['chicago','new york city','washington'] and i_type == 'c':
                    break
                elif i_u in month_list and i_type == 'm':
                    break
                elif i_u in day_list and i_type == 'd':
                    break
                else:
                    if i_type == 'c':
                        print("Invalid Input!")
                    if i_type == 'm':
                        print("Invalid Input!")
                    if i_type == 'd':
                        print("Invalid Input!")
            except ValueError:
                print("Sorry, wrong input")
    return i_u

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

     # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = check_user_input("Kindly, select a city you want to analyze:\n{chicago}\n{new york city} \n{washington}\n",'c')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = check_user_input("Kindly, select a month between {January to June} if you need to view data for all months,select 'all': \n", 'm')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_user_input("Kindly, select a day between {sunday, monday, tuesday, wednesday, thursday, friday, saturday} if you need to view data for all days,select 'all':\n", 'd')

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
    # we will load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Now we need to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # now we need filter by month
        df = df[df['month'] == month]

    if day != 'all':
        # now we need filter by day of week
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    m_c_m = df['month'].mode()[0]
    print('Most Common Month is: ', m_c_m)

    # TO DO: display the most common day of week
    m_c_d = df['day_of_week'].mode()[0]
    print('Most Common Day Of Week is: ', m_c_d)

    # TO DO: display the most common start hour
    m_c_h = df['hour'].mode()[0]
    print('Most Common Start Hour Of Day is: ', m_c_h)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commo_s_station = df['Start Station'].mode()[0]
    print('Most Common Start Station is: ', most_commo_s_station)

    # TO DO: display most commonly used end station
    most_common_e_station = df['End Station'].mode()[0]
    print('Most Common End Station is: ', most_common_e_station)

     # TO DO: display most frequent combination of start station and end station trip
    combination_g=df.groupby(['Start Station','End Station'])
    most_frequent_combination_station = combination_g.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip is: ', most_frequent_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time is: ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Types in Data are: ',df['User Type'].value_counts())

    # will ensure that the city is not washington
    if city != 'washington':

         # TO DO: Display counts of gender
        print('Counts Of Gender: ',df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('Earliest Year is: ',earliest_year)

        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year is: ',most_recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year is: ',most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Here we will display raw data to the user
<<<<<<< HEAD
def show_row_data(df):
=======
#if yes we will display and if no will break
def display_row_data(df):
>>>>>>> documentation
    row=0
    while True:
        show_row_data = input("Do you want to see raw data? if Yes enter (y) and if No enter (n).\n").lower()

        if show_row_data == "y":
            print(df.iloc[row : row + 6])
            row += 6
        elif show_row_data == "n":
            break
        else:
<<<<<<< HEAD
            print("INVALID INPUT!")
=======
            print("try Again!")
>>>>>>> documentation

def main():
  while True:
        city,month,day = get_filters()
        df = load_data(city,month,day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_row_data(df)
        restart = input('\nWould you like to restart? Enter "y" for yes or "n" for no.\n').lower()
        if restart.lower() != 'y':
            break

if __name__ == "__main__":
	main()
