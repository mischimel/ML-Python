# Load and open the JSON-file via Python. Via iteration
# extract the content of the file and plot (using the library matplotlib)
# the name and salary of the employees. Don't forget to add a title and the
# legends for the two axis X and Y and to set the bar color as blue.
# Finally convert the matplotlib graphics to a PNG graphics entitled salary.png
# and store it on the same location as the Python program and the JSON-file.

import json
import matplotlib.pyplot as plt

def main():
    # Load and open the JSON file
    with open('salary.json', 'r') as json_file:
        data = json.load(json_file)

    # Extract employee names and salaries
    employee_data = data['employee']
    employee_names = [entry['name'] for entry in employee_data]
    employee_salaries = [entry['salary'] for entry in employee_data]

    # Create a bar chart
    plt.bar(employee_names, employee_salaries, color='blue')

    # Set title and labels for the X and Y axes
    plt.title('Employee Salaries')
    plt.xlabel('Employee Names')
    plt.ylabel('Salary')

    # Rotate X-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Save the plot as a PNG image
    plt.savefig('salary.png', bbox_inches='tight')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
