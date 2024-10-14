import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.graph_objects as go
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# Read the CSV file
df = pd.read_csv("grammar_and_mechanics.csv")


# Bar Plot
def bar_plot(df):
    df.plot(kind="bar", x="Grade Level", stacked=False)
    plt.title("Proficiency in Grammar and Mechanics")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig("bar_plot.png")
    plt.show()


# Pie Chart
def pie_chart(df):
    total_students = df.drop(columns=["Grade Level"]).sum()
    plt.pie(
        total_students, labels=total_students.index, autopct="%1.1f%%", startangle=90
    )
    plt.title("Overall Proficiency in Grammar and Mechanics")
    plt.tight_layout()
    plt.savefig("pie_chart.png")
    plt.show()


# Diverging Bar Plot
def diverging_bar_plot(df):
    df_melt = df.melt(id_vars="Grade Level", var_name="Category", value_name="Count")
    df_melt["Divergence"] = np.where(
        df_melt["Category"] == "On Grade", df_melt["Count"], -df_melt["Count"]
    )
    sns.barplot(x="Divergence", y="Grade Level", hue="Category", data=df_melt)
    plt.title("Proficiency in Grammar and Mechanics")
    plt.xlabel("Divergence (Positive for Proficient, Negative for Below Average)")
    plt.tight_layout()
    plt.savefig("diverging_bar_plot.png")
    plt.show()


# Area Chart
def area_chart(df):
    df.set_index("Grade Level").plot(kind="area", stacked=True)
    plt.title("Proficiency in Grammar and Mechanics")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig("area_chart.png")
    plt.show()


# Lollipop Chart
def lollipop_chart(df):
    fig, ax = plt.subplots()
    for i, row in df.iterrows():
        grade = row["Grade Level"]
        categories = row.index[1:]
        counts = row.values[1:]

        ax.vlines(
            x=categories, ymin=0, ymax=counts, color="skyblue", alpha=0.7, linewidth=2
        )
        ax.scatter(x=categories, y=counts, color="blue", alpha=0.7, s=100)

    plt.title("Proficiency in Grammar and Mechanics")
    plt.xlabel("Category")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig("lollipop_chart.png")
    plt.show()


# Generate all plots
bar_plot(df)
pie_chart(df)
diverging_bar_plot(df)
area_chart(df)
lollipop_chart(df)
