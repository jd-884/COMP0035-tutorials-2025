from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

project_root = Path(__file__).parent.parent

def describe_dataframe(df: pd.DataFrame, df_name: str = "DataFrame"):
    print(f"\nAnalysis for {df_name}:")
    print("DataFrame Info:")
    print(df.info())
    print("\nDataFrame Description:")
    print(df.describe(include='all'))
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nLast 5 Rows:")
    print(df.tail())
    print("\nMissing Values per Column:")
    missing_values = df.isna().sum()
    print(missing_values)
    print(f"\nTotal Missing Values: {missing_values.sum()}")
    print("\nUnique Values per Column:")
    print(df.nunique())
    df.hist()
    plt.show()

    #create a dataframe with missing rows only

    missing_rows=df[df.isna().any(axis=1)]
    print(f"\nRows with Missing Values ({len(missing_rows)} rows):")
    if len(missing_rows) > 0:
        print(missing_rows)
    else:
        print("No rows with missing values found.")
    
    print("\n" + "="*50 + "\n")

    #create a dataframe with missing columns only
    missing_columns=df.columns[df.isna().any()].tolist()
    print(f"\nColumns with Missing Values ({len(missing_columns)} columns):")
    if len(missing_columns) > 0:
        print(missing_columns)
    else:
        print("No columns with missing values found.")
    
    print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    csv_path= project_root / "data"/"paralympics_raw.csv"
    xslx_path = project_root / "data"/"paralympics_all_raw.xlsx"

    csv_read=pd.read_csv(csv_path)
    xslx_read_1=pd.read_excel(xslx_path,sheet_name=0)
    xslx_read_2=pd.read_excel(xslx_path,sheet_name=1)
    describe_dataframe(csv_read)
    describe_dataframe(xslx_read_1)
    describe_dataframe(xslx_read_2)

