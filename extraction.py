import pymysql
import random
from sqlalchemy import create_engine, inspect
import pandas as pd

# MySQL Connection Details
USER = "admin"
PASSWORD = "h3xah3a1tH14"
HOST = "hexa-staging-db.cqnt4cbjitmj.ap-south-1.rds.amazonaws.com"  # e.g., "localhost" or an IP
DATABASE = "hexahealth_db"

if __name__ == '__main__':
    # Connect to MySQL
    engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")
    inspector = inspect(engine)

    # Fetch all tables
    tables = inspector.get_table_names()

    # Generate Training Data
    dataset = []

    # Define query templates
    query_templates = [
        ("List all records from {table}", "SELECT * FROM {table};"),
        ("Count the number of records in {table}", "SELECT COUNT(*) FROM {table};"),
        ("Find all {column} in {table}", "SELECT {column} FROM {table};"),
        ("Show {column} where {column} is {value} in {table}", "SELECT * FROM {table} WHERE {column} = '{value}';")
    ]

    # Extract schema and generate queries
    for table in tables:
        columns = inspector.get_columns(table)
        column_names = [col['name'] for col in columns]

        for template in query_templates:
            nl_template, sql_template = template
            column = random.choice(column_names) if column_names else "id"  # Select a random column
            value = "example_value"  # Placeholder for WHERE condition

            # Format queries
            nl_query = nl_template.format(table=table, column=column, value=value)
            sql_query = sql_template.format(table=table, column=column, value=value)

            dataset.append((nl_query, sql_query))

    # Save dataset to CSV
    df = pd.DataFrame(dataset, columns=["Natural_Language_Query", "SQL_Query"])
    df.to_csv("data/nlp_sql_dataset.csv", index=False)

    print("Dataset created and saved as 'nlp_sql_dataset.csv'")
