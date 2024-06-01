import tkinter as tk
from tkinter import scrolledtext  # Import scrolledtext for creating a scrollable text area
import csv
import configparser
import subprocess

def save_login_info(username, password):
    # Save username and password to a properties file
    config = configparser.ConfigParser()
    config['Credentials'] = {'Username': username,
                             'Password': password}
    with open('credentials.ini', 'w') as configfile:
        config.write(configfile)

    # Close the login window
    login_window.destroy()

def open_login_window():
    global login_window  # Declare login_window as global so it can be accessed outside the function
    login_window = tk.Toplevel(root)
    login_window.title("Log in into Gmail")

    # Add labels and entry fields for username and password
    username_label = tk.Label(login_window, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=5)

    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(login_window, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)

    password_entry = tk.Entry(login_window, show="*")  # Show asterisks for password input
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    # Add button to close the window and save values
    enter_button = tk.Button(login_window, text="Enter", command=lambda: save_login_info(username_entry.get(), password_entry.get()))
    enter_button.grid(row=2, columnspan=2, padx=10, pady=10)



# Function to read and print contents of the "combined_text" column from a CSV file
def read_csv(filename, print_area, column_name=None):
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            email_counter = 1  # Initialize email counter
            for row in reader:
                content = row[column_name] if column_name else row['combined_text']
                print_to_area(content, print_area, email_counter)
                email_counter += 1  # Increment email counter
    except FileNotFoundError:
        print_to_area("File not found.", print_area)


def read_csv_print_area2(filename, print_area):
    # Define the lists containing strings based on the value read
    list_one = ["[ALERT] This email looks fishy, just like a phishing attempt!",
    "[ALERT] Caution! This might be a phishing email trying to lure you.",
    "[ALERT] Beware! The waters of this email seem phishy. It might be a scam.",
    "[ALERT] Uh-oh! This email smells like a phish. Exercise caution!",
    "[ALERT] Alert! This email could be bait for a phishing scam. Stay vigilant!"]  

    list_zero = ["Great news! This email seems safe and legitimate.",
    "No red flags here! This email appears to be from a trusted source.",
    "Looks good! You can proceed confidently with this email.",
    "Safe and sound! This email doesn't raise any security concerns.",
    "All clear! This email passes the safety check with flying colors."] 
    
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            email_counter = 1  # Initialize email counter
            for row in reader:
                value = row['label']  # Assuming 'label' is the column name in the CSV file
                
                # Check the value and select the appropriate string from the respective list
                if value == '1':
                    string_to_print = list_one[email_counter % len(list_one)]  # Select string from list_one
                elif value == '0':
                    string_to_print = list_zero[email_counter % len(list_zero)]  # Select string from list_zero
                else:
                    string_to_print = "Invalid value"  # Handle invalid values
                
                # Print the string with "Email #" before it
                print_to_area(f"Email #{email_counter}: {string_to_print}", print_area)
                
                email_counter += 1  # Increment email counter
    except FileNotFoundError:
        print_to_area("File not found.", print_area)

# Function to print to the print area
def print_to_area(message, print_area, email_counter=None):
    if email_counter is not None:
        print_area.insert(tk.END, f"Email #{email_counter}: {message}\n")  # Insert the message with Email # at the end of the print area
    else:
        print_area.insert(tk.END, message + "\n")  # Insert the message at the end of the print area
    print_area.see(tk.END)  # Scroll to the end to show the latest message


# Create the main window
root = tk.Tk()
root.title("Email Defense Task Force")
root.geometry("1600x800")
root.configure(bg="#f0f0f0")  # Set background color

# Create a frame for the header bar
header_frame = tk.Frame(root, bg="#333333", height=100)
header_frame.pack(fill="x")

# Add a label for the title to the header bar
header_label = tk.Label(header_frame, text="Email Defense Task Force!", fg="white", bg="#333333", font=("Arial", 24, "bold"))
header_label.pack(pady=30, side="left", padx=30) # Add padding to the top and bottom of the label

# Common button style
button_style = {"fg": "white", "font": ("Arial", 14, "bold"), "bd": 0}

# Add a subtle separator line below the header bar
separator_line = tk.Frame(root, height=1, bg="#aaaaaa")
separator_line.pack(fill="x")

# START BUTTON
def start_script():
    try:
        # Execute the main script
        subprocess.run(["python", "D:/THESIS PROJECT/UI/mainframe.py"])
        print("Script execution completed successfully.")
    except Exception as e:
        print(f"An error occurred while executing the script: {e}")




# REFRESH BUTTON
def refresh_window():

    try:
        # Execute the main script
        subprocess.run(["python", "D:/THESIS PROJECT/UI/mainframe.py"])
        print("Script execution completed successfully.")
    except Exception as e:
        print(f"An error occurred while executing the script: {e}")

    global root  # Declare root as a global variable
    root.destroy()  # Destroy the current window

    # Recreate the main window with all its components
    root = tk.Tk()
    root.title("Email Defense Task Force")
    root.geometry("1600x800")
    root.configure(bg="#f0f0f0")  # Set background color

    # Create a frame for the header bar
    header_frame = tk.Frame(root, bg="#333333", height=100)
    header_frame.pack(fill="x")

     #Add a label for the title to the header bar
    header_label = tk.Label(header_frame, text="Email Defense Task Force!", fg="white", bg="#333333", font=("Arial", 24, "bold"))
    header_label.pack(pady=30, side="left", padx=30) # Add padding to the top and bottom of the label

    # Add a button for login to the header bar
    login_button = tk.Button(header_frame, text="Log In", fg="white", bg="#333333", font=("Arial", 14, "bold"), bd=0, command=open_login_window)
    login_button.pack(side="right", padx=30)

    #  Add a subtle separator line below the header bar
    separator_line = tk.Frame(root, height=1, bg="#aaaaaa")
    separator_line.pack(fill="x")

#################################################
    # Add a button for refreshing the print areas
    refresh_button = tk.Button(header_frame, text="Refresh", bg="#333333", command=refresh_window, **button_style)
    refresh_button.pack(side="right", padx=10, pady=10)

    # Create a frame for the first print area
    print_frame1 = tk.Frame(root, bg="#ffffff", bd=1, relief="solid", width=550, height=400)
    print_frame1.pack(pady=20, padx=20, side="left")

    # Add a label to indicate the first print area
    print_label1 = tk.Label(print_frame1, text="Emails Fetched", font=("Arial", 16, "bold"), fg="black", bg="#ffffff")
    print_label1.pack(pady=(20, 10))

    # Create a scrolled text widget for the first print area
    print_area1 = scrolledtext.ScrolledText(print_frame1, wrap=tk.WORD, width=80, height=50, bg="#ffffff", font=("Arial", 12))
    print_area1.pack(pady=(0, 20), padx=20)

    # Example usage: Read and print contents of the "combined_text" column from a CSV file
    read_csv("new_data.csv", print_area1)

    # Create a frame for the second print area
    print_frame2 = tk.Frame(root, bg="#ffffff", bd=1, relief="solid", width=550, height=400)
    print_frame2.pack(pady=20, padx=20, side="left")

    # Add a label to indicate the second print area
    print_label2 = tk.Label(print_frame2, text="Email Security Scan Results", font=("Arial", 16, "bold"), fg="black", bg="#ffffff")
    print_label2.pack(pady=(20, 10))

    # Create a scrolled text widget for the second print area
    print_area2 = scrolledtext.ScrolledText(print_frame2, wrap=tk.WORD, width=80, height=50, bg="#ffffff", font=("Arial", 12))
    print_area2.pack(pady=(0, 20), padx=20)

    # Example usage: Read and print contents of the "label" column from another CSV file to the second print area
    read_csv_print_area2("predicted_new_data.csv", print_area2)

    root.mainloop()  # Start the event loop for the new window

# Login Button
login_button = tk.Button(header_frame, text="Log In", bg="#333333", command=open_login_window, **button_style)
login_button.pack(side="right", padx=30, pady=10)

#Start Button
start_button = tk.Button(header_frame, text="Start", bg="#333333", command=start_script, **button_style)
start_button.pack(side="right", padx=10, pady=10)

#Refresh Button
refresh_button = tk.Button(header_frame, text="Refresh", bg="#333333", command=refresh_window, **button_style)
refresh_button.pack(side="right", padx=10, pady=10)

############### PRINT AREA ######################
# Create a frame for the first print area
print_frame1 = tk.Frame(root, bg="#ffffff", bd=1, relief="solid", width=550, height=400)
print_frame1.pack(pady=20, padx=20, side="left")

# Add a label to indicate the first print area
print_label1 = tk.Label(print_frame1, text="Emails Fetched", font=("Arial", 16, "bold"), fg="black", bg="#ffffff")
print_label1.pack(pady=(20, 10))

# Create a scrolled text widget for the first print area
print_area1 = scrolledtext.ScrolledText(print_frame1, wrap=tk.WORD, width=80, height=50, bg="#ffffff", font=("Arial", 12))
print_area1.pack(pady=(0, 20), padx=20)

# Example usage: Read and print contents of the "combined_text" column from a CSV file
read_csv("new_data.csv", print_area1)

# Create a frame for the second print area
print_frame2 = tk.Frame(root, bg="#ffffff", bd=1, relief="solid", width=550, height=400)
print_frame2.pack(pady=20, padx=20, side="left")

# Add a label to indicate the second print area
print_label2 = tk.Label(print_frame2, text="Email Security Scan Results", font=("Arial", 16, "bold"), fg="black", bg="#ffffff")
print_label2.pack(pady=(20, 10))

# Create a scrolled text widget for the second print area
print_area2 = scrolledtext.ScrolledText(print_frame2, wrap=tk.WORD, width=80, height=50, bg="#ffffff", font=("Arial", 12))
print_area2.pack(pady=(0, 20), padx=20)

# Example usage: Read and print contents of the "label" column from another CSV file to the second print area
read_csv_print_area2("predicted_new_data.csv", print_area2)


# Start the Tkinter event loop
root.mainloop()
