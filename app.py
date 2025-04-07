import pandas as pd

def CountUniquePlayers(filepath='part3/player_logged_in.csv'):
    df = pd.read_csv(filepath)
    
    login_events = df[df['EventName'] == 'player_logged_in']
    
    unique_players = login_events['pid'].nunique()
    
    print(f"Total unique players who logged in: {unique_players}")
    return unique_players

def DailyUniquePlayers(filepath='part3/player_logged_in.csv'):
    df = pd.read_csv(filepath)

    df['Time'] = pd.to_datetime(df['Time'])

    df['Date'] = df['Time'].dt.date

    login_events = df[df['EventName'] == 'player_logged_in']

    daily_unique = login_events.groupby('Date')['pid'].nunique()

    daily_unique.index = pd.to_datetime(daily_unique.index)

    print(daily_unique)
    return daily_unique


def MonthlyUniquePlayers(filepath='part3/player_logged_in.csv'):
    df = pd.read_csv(filepath)

    df['Time'] = pd.to_datetime(df['Time'])

    df['Month'] = df['Time'].dt.to_period('M')

    login_events = df[df['EventName'] == 'player_logged_in']

    monthly_unique = login_events.groupby('Month')['pid'].nunique()

    monthly_unique.index = monthly_unique.index.to_timestamp()

    print(monthly_unique)
    return monthly_unique

def Sessions(filepath='part3/exited_game.csv'):
    df = pd.read_csv(filepath)
    df['Time'] = pd.to_datetime(df['Time'])

    sessions = df[df['EventName'] == 'exited_game']

    return sessions


def ProgressData(filepath='part3/exited_game.csv'):
    import pandas as pd
import pandas as pd

def ProgressData(filepath='part3/exited_game.csv'):
    logIn = pd.read_csv('part3/player_logged_in.csv')
    logIn['Time'] = pd.to_datetime(logIn['Time'])

    logOut = pd.read_csv(filepath)
    logOut['Time'] = pd.to_datetime(logOut['Time'])

    logIn = logIn[logIn['EventName'] == 'player_logged_in']
    logOut = logOut[logOut['EventName'] == 'exited_game']

    logIn.sort_values(by=['pid', 'Time'], inplace=True)
    logOut.sort_values(by=['pid', 'Time'], inplace=True)

    logIn = logIn.reset_index(drop=True)
    logOut = logOut.reset_index(drop=True)

    df = logOut.copy()
    df['LoginTime'] = logIn['Time']
    
    df['SessionDuration'] = (logOut['CurrentSessionLength'])

    df['ProgressAmount'] = df['LevelProgressionAmount']

    return df

def NumberOfCompletedTasks(filepath='part3/job_completed.csv'):
    JobsStarted = pd.read_csv('part3/job_started.csv')
    JobsStarted['Time'] = pd.to_datetime(JobsStarted['Time'])
    JobsStarted.sort_values(by=['pid', 'Time'], inplace=True)

    JobComplete = pd.read_csv(filepath)
    JobComplete['Time'] = pd.to_datetime(JobComplete['Time'])

    df = JobsStarted.copy()
    df['job_started'] = JobsStarted['Time']
    
    df['job_completed'] = (JobComplete['Time'])

    df['ProgressAmount'] = JobComplete['CampaignProgressionAmount']

    return df

