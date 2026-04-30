import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def choice():
    choiceStuff = input("1) Assignee by Total Hours\n2) Errors by Severity\nPLEASE make choice\n(or type Q to exit)\n:")
    if choiceStuff == "1":
        report = df.groupby("assignee").agg(
            assHours=("hours_to_fix", "sum")
        ).reset_index()
        
        report.plot(
            x="assignee", y="assHours",
            kind="bar", title="Assignee Hours",
            legend=False, color="#065A82")
        
        plt.tight_layout()
        plt.savefig("barchart.png")
    
    elif choiceStuff =="2":
        report = df.groupby("severity").agg(
            total_bugs=("bug_id", "count")
        ).reset_index()
        
        minalabels = ["critical", "high", "low", "medium"]
        
        report.plot(
            x="severity", y="total_bugs",
            kind="pie", title="Bugs by Severity",
            legend=False, color="#065A82", labels = minalabels)
        
        plt.tight_layout()
        plt.savefig("piechart.png")
    else:
        exit()

df = pd.read_csv("bugs.csv")

choice()


