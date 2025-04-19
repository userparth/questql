# NLP-to-SQL Model -:local

## Project Description
This project builds a **Natural Language to SQL (NLP-to-SQL) model** using **T5 transformers** to convert user queries into SQL statements. It enables database searches through conversational input.

## Features
- Train a custom NLP-to-SQL model using MySQL schema
- Tokenize and normalize text queries
- Fine-tune a transformer model (T5)
- Generate SQL queries from user input
- Supports query execution on MySQL databases

## Installation
```bash
# Clone the repository
git clone https://github.com/your-repo/nlp-to-sql.git
cd nlp-to-sql

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
### Train the Model
```bash
python train.py
```

### Test the Model
```bash
python test_model.py
```

### Example Query
```
Enter a natural language query: Show all orders where status is pending
Generated SQL Query: SELECT * FROM orders WHERE status = 'pending';
```

## Future Improvements
- Fine-tune with more complex queries (`JOIN`, `GROUP BY`, `ORDER BY`)
- Deploy as an API with **FastAPI** or **Flask**
- Optimize SQL query generation accuracy
