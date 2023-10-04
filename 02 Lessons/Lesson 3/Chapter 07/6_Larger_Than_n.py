# Main function
def main():
    my_list = [2, 3, 4, 5, 6, 7, 8]
    threshold = 4

    print_values(threshold,my_list)
    print_val(threshold,my_list)

# Printing the values larger than the threshold
def print_values(threshold, my_list):
    for val in my_list:
        if val > threshold:
            print(val)

def print_val(threshold, my_list):
    values = [var for var in my_list if var > threshold]
    print(values)



# Calling the main function
if __name__ == "__main__":
    main()
