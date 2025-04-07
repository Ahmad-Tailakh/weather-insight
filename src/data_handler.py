import pandas as pd
from .logger import logger

# In your save_to_csv function, add a step to clean the data:
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df = df.dropna()  # Drops rows with missing data
    df.to_csv(filename, index=False)
    logger.info(f"Saved data to {filename}")
