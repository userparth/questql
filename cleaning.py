import pandas as pd
import re
import spacy

# Load SpaCy English Model
nlp = spacy.load("en_core_web_sm")


# Load dataset
df = pd.read_csv("data/nlp_sql_dataset.csv")

# Function to clean text
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

# Function to tokenize text using SpaCy
def tokenize_text(text):
    doc = nlp(text)  # Process text with SpaCy
    return [token.text for token in doc]  # Return tokenized words

if __name__ == '__main__':
    # Apply cleaning and tokenization
    df["Cleaned_NL_Query"] = df["Natural_Language_Query"].apply(clean_text)
    df["Tokenized_NL_Query"] = df["Cleaned_NL_Query"].apply(tokenize_text)

    # Save cleaned dataset
    df.to_csv("data/nlp_sql_cleaned_dataset.csv", index=False)

    print("Tokenized dataset saved as 'nlp_sql_cleaned_dataset.csv'")