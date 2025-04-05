import pandas as pd

def CountUniquePlayers(filepath='part3/player_logged_in.csv'):
    df = pd.read_csv(filepath)
    
    login_events = df[df['EventName'] == 'player_logged_in']
    
    unique_players = login_events['pid'].nunique()
    
    print(f"Total unique players who logged in: {unique_players}")
    return unique_players
