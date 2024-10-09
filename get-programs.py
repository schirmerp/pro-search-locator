from bs4 import BeautifulSoup
import pandas as pd

# Load your HTML content
with open("programs.html", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find all elements with 'aria-label' attribute
elements_with_aria_label = soup.find_all(attrs={"aria-label": True})

# Extract the values of 'aria-label'
program_names = [element['aria-label'] for element in elements_with_aria_label]

# Create a DataFrame to hold the program names
df = pd.DataFrame(program_names, columns=["Program Name"])

# Save the DataFrame to a CSV file
df.to_csv("program_names.csv", index=False)

print("Program names have been successfully saved to 'program_names.csv'.")
