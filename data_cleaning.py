import pandas as pd


def remove_empty_rows(csv_file_path, output_path=None):
    """
    Remove empty rows from a CSV file.
    
    Args:
        csv_file_path (str): Path to the input CSV file
        output_path (str, optional): Path to save the cleaned CSV file. 
                                   If None, overwrites the original file
        
    Returns:
        pd.DataFrame: DataFrame with empty rows removed
    """
    df = pd.read_csv(csv_file_path)
    cleaned_df = df.dropna(how='all')
    
    if output_path is None:
        output_path = csv_file_path
    
    cleaned_df.to_csv(output_path, index=False)
    return cleaned_df
