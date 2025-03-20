import pandas as pd
import sqlparse

if __name__ == "__main__":
    # Load the cleaned dataset
    df = pd.read_csv("data/nlp_sql_cleaned_dataset.csv")

    # Function to normalize SQL queries
    def normalize_sql(query):
        return sqlparse.format(query, reindent=True, keyword_case='upper')

    # Apply SQL normalization
    df["Normalized_SQL_Query"] = df["SQL_Query"].apply(normalize_sql)

    # Save the final dataset
    df.to_csv("data/nlp_sql_final_dataset.csv", index=False)

    print("Final dataset saved as 'nlp_sql_final_dataset.csv'")
