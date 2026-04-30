import pandas as pd
df = pd.read_csv("bugs.csv")

byPerson = df.groupby("assignee")[
    "bug_id"].count().reset_index()
byPerson.columns = [
    "asignee", "bug_content"]
print(byPerson)