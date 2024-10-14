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
    df.plot(kind="bar", x="Grade", stacked=False)
    plt.title("Students Proficiency in Writing (Bar Plot)")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig("bar_plot.png")
    plt.show()


# Pie Chart
def pie_chart(df):
    total_students = df.drop(columns=["Grade"]).sum()
    plt.pie(
        total_students, labels=total_students.index, autopct="%1.1f%%", startangle=90
    )
    plt.title("Overall Student Writing Ability Distribution (Pie Chart)")
    plt.tight_layout()
    plt.savefig("pie_chart.png")
    plt.show()


# Diverging Bar Plot
def diverging_bar_plot(df):
    df_melt = df.melt(id_vars="Grade", var_name="Category", value_name="Count")
    df_melt["Divergence"] = np.where(
        df_melt["Category"] == "Above Grade", df_melt["Count"], -df_melt["Count"]
    )
    sns.barplot(x="Divergence", y="Grade", hue="Category", data=df_melt)
    plt.title("Diverging Bar Plot of Student Writing Proficiency")
    plt.xlabel("Divergence (Positive for Proficient, Negative for Below Average)")
    plt.tight_layout()
    plt.savefig("diverging_bar_plot.png")
    plt.show()


# Area Chart
def area_chart(df):
    df.set_index("Grade").plot(kind="area", stacked=True)
    plt.title("Students Writing Proficiency by Grade (Area Chart)")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig("area_chart.png")
    plt.show()


# Proportional Pictogram (Using Icons to Represent Students)
def proportional_pictogram(df):
    img = Image.open("student_icon.jpg")  # Replace with path to a student icon image
    icon_data = np.array(img)
    fig, ax = plt.subplots()

    # Customize based on student counts
    total_students = df[
        ["Above Grade", "Below Grade", "Far Below Grade", "Not Pinpointed"]
    ].sum()
    categories = total_students.index
    counts = total_students.values

    x_offset = 0
    for i, category in enumerate(categories):
        for j in range(counts[i] // 10):  # Use icons to represent students
            x, y = x_offset + j % 10, j // 10
            ax.add_artist(AnnotationBbox(OffsetImage(icon_data, zoom=0.05), (x, -y)))

        x_offset += 12

    ax.set_xlim([-1, x_offset])
    ax.set_ylim([-(max(counts) // 10 + 1), 1])
    ax.set_aspect("equal")
    ax.axis("off")
    plt.title("Proportional Pictogram of Student Proficiency")
    plt.tight_layout()
    plt.savefig("pictogram.png")
    plt.show()


# Lollipop Chart
def lollipop_chart(df):
    fig, ax = plt.subplots()
    for i, row in df.iterrows():
        grade = row["Grade"]
        categories = row.index[1:]
        counts = row.values[1:]

        ax.vlines(
            x=categories, ymin=0, ymax=counts, color="skyblue", alpha=0.7, linewidth=2
        )
        ax.scatter(x=categories, y=counts, color="blue", alpha=0.7, s=100)

    plt.title("Lollipop Chart for Student Proficiency by Category")
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
proportional_pictogram(df)
lollipop_chart(df)
