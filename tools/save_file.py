from datetime import datetime


def save_file(output: str):
    date = datetime.today()

    file = f"{date}.md"

    with open(file, "w") as f:
        f.write(output.result())

    print("Saved newsletter.")
