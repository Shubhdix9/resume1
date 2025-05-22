import pandas as pd
import matplotlib.pyplot as plt
import sys # Import sys for a cleaner exit

def display_menu(menu_options):
    """Displays a menu of options to the user."""
    print("\n-------------------- Menu --------------------")
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    print("----------------------------------------------")

def get_user_choice(prompt, valid_choices):
    """Gets validated integer input from the user."""
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def load_csv(filename):
    """Loads a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(filename)
        print(f"\n'{filename}' loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Please make sure the file exists in the same directory as the script.")
        return None
    except Exception as e:
        print(f"An error occurred while loading '{filename}': {e}")
        return None

def main():
    """Main function to run the IP project."""
    print("-------------- Namaskar Aapka Swagat Hai --------------")
    print("-------------- IP Project --------------")

    # Load the primary CSV file provided by the user
    df = load_csv("dataa1 (1).csv")
    if df is None:
        sys.exit(1) # Exit if the initial CSV can't be loaded

    while True:
        main_menu_options = {
            1: "Load Data",
            2: "Manipulate Data",
            3: "Analyze Data",
            4: "Visualize Data",
            5: "Exit"
        }
        display_menu(main_menu_options)
        choice = get_user_choice("Enter your choice: ", main_menu_options.keys())

        if choice == 1:
            data_load_options = {
                1: "Load 'dataa1 (1).csv' (Current Data)",
                2: "Load 'dataa.csv' (Another file, if exists)" # Placeholder for a different file if needed
            }
            display_menu(data_load_options)
            ch1 = get_user_choice("Enter your choice: ", data_load_options.keys())
            if ch1 == 1:
                df = load_csv("dataa1 (1).csv")
                if df is not None:
                    print("\nCurrently loaded Data:")
                    print(df)
            elif ch1 == 2:
                # This option is a placeholder. If 'dataa.csv' doesn't exist, it will show an error.
                df_temp = load_csv("dataa.csv")
                if df_temp is not None:
                    df = df_temp # Update the main dataframe if the new file loads successfully
                    print("\nNew Data Loaded:")
                    print(df)
                else:
                    print("\nCould not load 'dataa.csv'. Keeping current data.")

        elif choice == 2:
            manipulation_options = {
                1: "Add Row",
                2: "Add Column",
                3: "Delete Row",
                4: "Delete Column"
            }
            display_menu(manipulation_options)
            ch1 = get_user_choice("Enter your choice: ", manipulation_options.keys())

            if ch1 == 1:
                print("\nEnter values for the new row:")
                new_row_values = []
                for col in df.columns:
                    val = input(f"Enter value for '{col}': ")
                    new_row_values.append(val)
                try:
                    # Create a new DataFrame for the row and concatenate
                    new_row_df = pd.DataFrame([new_row_values], columns=df.columns)
                    df = pd.concat([df, new_row_df], ignore_index=True)
                    print("\nRow added successfully:")
                    print(df)
                except ValueError as e:
                    print(f"Error adding row: {e}. Make sure the number of values matches the number of columns.")

            elif ch1 == 2:
                col_name = input("Enter the name of the new column: ")
                if col_name in df.columns:
                    print(f"Column '{col_name}' already exists. Please choose a different name.")
                    continue
                new_col_values = []
                print(f"Enter values for the new column '{col_name}' (press Enter after each value):")
                if len(df) == 0:
                    print("DataFrame is empty. Cannot add column values without rows.")
                    continue
                for i in range(len(df)):
                    val = input(f"Value for row {i}: ")
                    new_col_values.append(val)
                try:
                    if len(new_col_values) == len(df):
                        df[col_name] = new_col_values
                        print(f"\nColumn '{col_name}' added successfully:")
                        print(df)
                    else:
                        print("Error: Number of values entered does not match the number of rows.")
                except Exception as e:
                    print(f"An error occurred while adding the column: {e}")

            elif ch1 == 3:
                if df.empty:
                    print("DataFrame is empty. No rows to delete.")
                    continue
                try:
                    row_index = int(input(f"Enter the index of the row to delete (0 to {len(df) - 1}): "))
                    if 0 <= row_index < len(df):
                        df = df.drop(row_index, axis=0).reset_index(drop=True) # Reset index after dropping
                        print(f"\nRow at index {row_index} deleted successfully:")
                        print(df)
                    else:
                        print("Invalid row index.")
                except ValueError:
                    print("Invalid input. Please enter a number for the index.")

            elif ch1 == 4:
                if df.empty:
                    print("DataFrame is empty. No columns to delete.")
                    continue
                print("\nAvailable columns:")
                for i, col in enumerate(df.columns):
                    print(f"{i}. {col}")
                try:
                    col_index = int(input(f"Enter the index of the column to delete (0 to {len(df.columns) - 1}): "))
                    if 0 <= col_index < len(df.columns):
                        col_name = df.columns[col_index]
                        df = df.drop(columns=[col_name])
                        print(f"\nColumn '{col_name}' deleted successfully:")
                        print(df)
                    else:
                        print("Invalid column index.")
                except ValueError:
                    print("Invalid input. Please enter a number for the index.")
                except IndexError:
                    print("Invalid column index.")


        elif choice == 3:
            analysis_options = {
                1: "Display First Five Rows",
                2: "Display Column Information (df.info())",
                3: "Display Last Five Rows",
                4: "Display Data Size and Shape",
                5: "Display Descriptive Statistics"
            }
            display_menu(analysis_options)
            ch3 = get_user_choice("Enter your choice: ", analysis_options.keys())

            if ch3 == 1:
                print("\nFirst Five Rows:")
                print(df.head())
            elif ch3 == 2:
                print("\nColumn Information (Non-null counts, Dtype, etc.):")
                df.info() # df.info() prints directly
            elif ch3 == 3:
                print("\nLast Five Rows:")
                print(df.tail())
            elif ch3 == 4:
                print(f"\nSize of Data: {df.size}")
                print(f"Shape of Data: {df.shape}")
            elif ch3 == 5:
                print("\nDescriptive Statistics (for numeric columns, or all with 'include='all'):")
                print(df.describe(include='all'))

        elif choice == 4:
            chart_options = {
                1: "Bar Chart",
                2: "Line Chart",
                3: "Histogram",
                4: "Pie Chart"
            }
            display_menu(chart_options)
            ch4 = get_user_choice("Enter your choice: ", chart_options.keys())

            if df.empty:
                print("DataFrame is empty. Cannot create charts.")
                continue

            if ch4 == 1:
                print("\nAvailable columns for Bar Chart (numeric or categorical counts):")
                plottable_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col]) or df[col].nunique() < 20]
                if not plottable_cols:
                    print("No suitable columns for a bar chart.")
                    continue
                for i, col in enumerate(plottable_cols):
                    print(f"{i}. {col}")
                try:
                    col_index = int(input("Enter the index of the column to plot: "))
                    if 0 <= col_index < len(plottable_cols):
                        column_to_plot = plottable_cols[col_index]
                        if pd.api.types.is_numeric_dtype(df[column_to_plot]):
                            df[column_to_plot].value_counts().sort_index().plot(kind="bar", figsize=(10, 6))
                        else:
                            df[column_to_plot].value_counts().plot(kind="bar", figsize=(10, 6))
                        plt.title(f"Bar Chart of {column_to_plot}")
                        plt.xlabel(column_to_plot)
                        plt.ylabel("Count")
                        plt.grid(axis='y', linestyle='--', alpha=0.7)
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("Invalid column index.")
                except ValueError:
                    print("Invalid input. Please enter a number for the index.")

            elif ch4 == 2:
                print("\nAvailable numeric columns for Line Chart:")
                numeric_cols = df.select_dtypes(include=['number']).columns
                if numeric_cols.empty:
                    print("No numeric columns available for a line chart.")
                    continue
                for i, col in enumerate(numeric_cols):
                    print(f"{i}. {col}")
                try:
                    col_index = int(input("Enter the index of the numeric column to plot: "))
                    if 0 <= col_index < len(numeric_cols):
                        column_to_plot = numeric_cols[col_index]
                        df[column_to_plot].plot(kind="line", figsize=(10, 6))
                        plt.title(f"Line Chart of {column_to_plot}")
                        plt.xlabel("Index")
                        plt.ylabel(column_to_plot)
                        plt.grid(True, linestyle='--', alpha=0.7)
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("Invalid column index.")
                except ValueError:
                    print("Invalid input. Please enter a number for the index.")

            elif ch4 == 3:
                print("\nAvailable numeric columns for Histogram:")
                numeric_cols = df.select_dtypes(include=['number']).columns
                if numeric_cols.empty:
                    print("No numeric columns available for a histogram.")
                    continue
                for i, col in enumerate(numeric_cols):
                    print(f"{i}. {col}")
                try:
                    col_index = int(input("Enter the index of the numeric column to plot: "))
                    if 0 <= col_index < len(numeric_cols):
                        column_to_plot = numeric_cols[col_index]
                        df[column_to_plot].plot(kind="hist", figsize=(10, 6), bins=10, edgecolor='black')
                        plt.title(f"Histogram of {column_to_plot}")
                        plt.xlabel(column_to_plot)
                        plt.ylabel("Frequency")
                        plt.grid(axis='y', linestyle='--', alpha=0.7)
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("Invalid column index.")
                except ValueError:
                    print("Invalid input. Please enter a number for the index.")

            elif ch4 == 4:
                print("\nAvailable columns for Pie Chart (suitable for categorical data with limited unique values):")
                # Suggest columns with fewer than a certain number of unique values for pie chart
                suitable_cols = [col for col in df.columns if df[col].nunique() < 15 and (df[col].dtype == 'object' or pd.api.types.is_categorical_dtype(df[col]))]
                if not suitable_cols:
                    print("No suitable categorical columns found for a pie chart. Consider columns with limited unique string/categorical values.")
                    continue
                for i, col in enumerate(suitable_cols):
                    print(f"{i}. {col}")
                try:
                    col_index = int(input("Enter the index of the column to plot: "))
                    if 0 <= col_index < len(suitable_cols):
                        column_to_plot = suitable_cols[col_index]
                        value_counts = df[column_to_plot].value_counts()
                        # Handle potential empty value_counts if the column itself is empty or has only NaNs
                        if not value_counts.empty:
                            value_counts.plot(kind="pie", autopct='%1.1f%%', startangle=90, figsize=(8, 8))
                            plt.title(f"Pie Chart of {column_to_plot}")
                            plt.ylabel('') # Hide the default y-label
                            plt.tight_layout()
                            plt.show()
                        else:
                            print(f"Column '{column_to_plot}' has no data to plot a pie chart.")
                    else:
                        print("Invalid column index.")
                except ValueError:
                    print("Invalid input. Please enter a number for the index.")

        elif choice == 5:
            print("Thank you for using the IP project. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()