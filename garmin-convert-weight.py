import pandas as pd
import os
import argparse


def load_file(file_path):
    """
    Load the Garmin CSV file.
    """
    print(f"Loading file: {file_path}")
    try:
        data = pd.read_csv(file_path, header=None)
        print(f"File loaded with shape: {data.shape}")
        print("\nRaw data (first 5 rows):")
        print(data.head())
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def process_data(data):
    """
    Process the Garmin CSV file into a new DataFrame with the correct format.
    """
    print("\nProcessing data...")
    try:
        new_data = []
        current_date = None
        expected_columns = 8  # Number of columns excluding the added 'Date'

        # Iterate through rows
        for index, row in data.iterrows():
            raw_value = str(row[0]).strip()  # Strip leading/trailing spaces
            print(f"Row {index}: {raw_value}")  # Debugging row content

            # Detect and handle date rows
            if pd.to_datetime(raw_value, errors='coerce', format='%b %d, %Y') is not pd.NaT:
                current_date = pd.to_datetime(raw_value).strftime('%m/%d/%Y')
                print(f"Detected date: {raw_value} -> Reformatted: {current_date}")

            # Handle time/data rows
            elif current_date and pd.notna(row[0]):
                # Ensure the row has the expected number of columns
                row_data = row.tolist()
                row_data = row_data[:expected_columns]  # Trim extra columns if any
                while len(row_data) < expected_columns:
                    row_data.append("")  # Add empty strings if missing columns

                # Add the current date as the first column
                new_data.append([current_date] + row_data)

        # Create a DataFrame from the processed data
        new_df = pd.DataFrame(new_data, columns=[
            'Date', 'Time', 'Weight', 'Change', 'BMI', 'Body Fat',
            'Skeletal Muscle Mass', 'Bone Mass', 'Body Water'
        ])

        print("\nProcessed data (first 5 rows):")
        print(new_df.head())
        return new_df
    except Exception as e:
        print(f"Error processing data: {e}")
        return None


def save_file(data, output_path, append=True):
    """
    Save the processed data to a CSV file. Append by default, overwrite if specified.
    """
    print(f"\nSaving processed data to: {output_path}")
    try:
        if append and os.path.exists(output_path):
            # Append without writing the header again
            data.to_csv(output_path, mode='a', header=False, index=False)
            print("Data appended successfully!")
        else:
            # Write the file with headers if not appending
            data.to_csv(output_path, index=False)
            print("Data saved successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and save Garmin weight data.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("output_file", help="Path to the output CSV file.")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the output file if it exists. Default is to append."
    )

    args = parser.parse_args()

    # Load the raw data
    raw_data = load_file(args.input_file)
    if raw_data is not None:
        # Process the data into the desired format
        cleaned_data = process_data(raw_data)
        if cleaned_data is not None:
            # Save the processed data, defaulting to append unless overwrite is specified
            save_file(cleaned_data, args.output_file, append=not args.overwrite)