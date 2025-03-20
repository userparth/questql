from sqlalchemy import create_engine, inspect

if __name__ == '__main__':
    # Replace with your actual MySQL credentials
    USER = "admin"
    PASSWORD = "h3xah3a1tH14"
    HOST = "hexa-staging-db.cqnt4cbjitmj.ap-south-1.rds.amazonaws.com"  # e.g., "localhost" or an IP
    DATABASE = "hexahealth_db"

    # Create MySQL connection string
    DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

    # Connect to MySQL
    engine = create_engine(DATABASE_URL)
    inspector = inspect(engine)

    # Get all tables
    tables = inspector.get_table_names()
    print("Tables:", tables)

    # Get columns for each table
    for table in tables:
        columns = inspector.get_columns(table)
        print(f"\nTable: {table}")
        for column in columns:
            print(f"  {column['name']} - {column['type']}")
