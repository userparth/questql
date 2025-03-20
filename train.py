import pandas as pd
from datasets import Dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration, TrainingArguments, Trainer, DataCollatorForSeq2Seq

def load_and_prepare_data():
    # Load dataset
    df = pd.read_csv("data/nlp_sql_final_dataset.csv")
    df = df[["Cleaned_NL_Query", "Normalized_SQL_Query"]]

    # Convert to Hugging Face Dataset
    dataset = Dataset.from_pandas(df)

    # Load tokenizer
    tokenizer = T5Tokenizer.from_pretrained("t5-small")

    # Tokenization function
    def tokenize_data(batch):
        inputs = tokenizer(batch["Cleaned_NL_Query"], padding="max_length", truncation=True, max_length=128)
        targets = tokenizer(batch["Normalized_SQL_Query"], padding="max_length", truncation=True, max_length=128)

        inputs["labels"] = targets["input_ids"]  # Ensure labels are properly set
        return inputs

    # Apply tokenization
    dataset = dataset.map(tokenize_data, batched=True, remove_columns=["Cleaned_NL_Query", "Normalized_SQL_Query"])

    # Split into train and test sets
    dataset = dataset.train_test_split(test_size=0.2)
    return dataset["train"], dataset["test"], tokenizer


def train_model(train_data, test_data, tokenizer):
    # Load T5 model
    model = T5ForConditionalGeneration.from_pretrained("t5-small")

    # Training arguments
    training_args = TrainingArguments(
        output_dir="./t5_sql_model",
        evaluation_strategy="epoch",
        learning_rate=3e-4,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=5,
        weight_decay=0.01,
        save_strategy="epoch"
    )

    data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_data,
        eval_dataset=test_data,
        tokenizer=tokenizer,
        data_collator=data_collator,  # Ensure correct formatting
    )

    # Train model
    trainer.train()

    # Save trained model
    model.save_pretrained("t5_sql_custom_model")
    tokenizer.save_pretrained("t5_sql_custom_model")
    print("Model training complete and saved!")


if __name__ == "__main__":
    train_data, test_data, tokenizer = load_and_prepare_data()
    train_model(train_data, test_data, tokenizer)
