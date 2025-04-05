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

    print(daily_unique)
    return daily_unique
