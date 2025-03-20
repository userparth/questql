from transformers import T5Tokenizer, T5ForConditionalGeneration


def load_model():
    # Load trained model and tokenizer
    model = T5ForConditionalGeneration.from_pretrained("t5_sql_custom_model")
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    return model, tokenizer


def generate_sql(model, tokenizer, user_query):
    # Tokenize input query
    input_ids = tokenizer(user_query, return_tensors="pt").input_ids

    # Generate SQL query
    output = model.generate(input_ids)
    sql_query = tokenizer.decode(output[0], skip_special_tokens=True)
    return sql_query


if __name__ == "__main__":
    model, tokenizer = load_model()

    while True:
        user_query = input("Enter a natural language query (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break

        sql_query = generate_sql(model, tokenizer, user_query)
        print("Generated SQL Query:", sql_query)
