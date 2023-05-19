import csv
import json
import typer

app = typer.Typer()

@app.command()
def convert_csv_to_jsonl(csv_file: str = typer.Argument(..., help="Path to the CSV file"),
                         jsonl_file: str = typer.Argument(..., help="Path to the JSONL output file")):
    try:
        with open(csv_file, 'r') as csvfile, open(jsonl_file, 'w') as jsonlfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                text = row['Company']
                order_id = int(row['Order_ID'])
                data = {"text": text, "meta": {"order_id": order_id}}
                jsonlfile.write(json.dumps(data) + '\n')
        typer.echo(f"Conversion completed. JSONL file saved to: {jsonl_file}")
    except FileNotFoundError:
        typer.echo("Error: File not found.")

if __name__ == "__main__":
    app()
