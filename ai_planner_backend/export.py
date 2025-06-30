import pandas as pd

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    
def save_trip_plan(text, filename):
    
    with open(filename, "w") as f:
        f.write(text)