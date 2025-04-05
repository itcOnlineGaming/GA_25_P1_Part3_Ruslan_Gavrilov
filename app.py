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
    import pandas as pd

    df = pd.read_csv(filepath)

    df['Time'] = pd.to_datetime(df['Time'])

    df['Month'] = df['Time'].dt.to_period('M')

    login_events = df[df['EventName'] == 'player_logged_in']

    monthly_unique = login_events.groupby('Month')['pid'].nunique()

    print(monthly_unique)
    return monthly_unique
