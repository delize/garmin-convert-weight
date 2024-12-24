# Garmin Weight Conversion Script

The `garmin-convert-weight.py` script processes Garmin CSV files containing weight data and converts them into a structured, date-aligned format. I created this, mainly because I couldn't find an alternative for what I needed. Which was just a pure CSV file that I could then make graphs and data out of, without Jupyter notebook or something else. 

---

## How to Use

### Command Syntax
```bash
python3 garmin-convert-weight.py <input_file> <output_file> [--overwrite]
```

### Arguments

#### Positional Arguments
- **`<input_file>`**: Path to the input CSV file containing the raw Garmin weight data.
- **`<output_file>`**: Path to the output CSV file where the processed data will be saved.

#### Optional Arguments
- **`--overwrite`**:
  - By default, the script appends data to the output file if it exists.
  - Use `--overwrite` to overwrite the existing output file instead of appending.

---

## Examples

### 1. Append Data to an Existing File (Default Behavior)
```bash
python3 garmin-convert-weight.py input.csv output.csv
```
- Appends the processed data from `input.csv` to `output.csv`.
- If `output.csv` does not exist, it will create the file.

### 2. Overwrite the Output File
```bash
python3 garmin-convert-weight.py input.csv output.csv --overwrite
```
- Overwrites `output.csv` with the processed data from `input.csv`.

---

## Input Format

The input CSV file should contain raw Garmin weight data with the following structure (note: This works for Muscle Mass, Bone Mass, and Body Water as well, even though not shown below):

| Time          | Weight   | Change   | BMI  | Body Fat | Skeletal Muscle Mass | Bone Mass | Body Water |
|---------------|----------|----------|------|----------|-----------------------|-----------|------------|
| Dec 31, 2017  |          |          |      |          |                       |           |            |
| 01:00         | 80.4 kg  | 49.4 kg  | 25.6 | 20%      | –                     | –         | –          |
| 01:00         | 79.8 kg  | 49.3 kg  | 25.5 | 19.8%    | –                     | –         | –          |

---

## Output Format

The processed output CSV will contain the following columns, with each timestamp aligned to its associated date:

| Date       | Time  | Weight   | Change   | BMI  | Body Fat | Skeletal Muscle Mass | Bone Mass | Body Water |
|------------|-------|----------|----------|------|----------|-----------------------|-----------|------------|
| 12/31/2017 | 01:00 | 80.4 kg  | 49.4 kg  | 25.6 | 20%      | –                     | –         | –          |
| 12/31/2017 | 01:00 | 79.8 kg  | 49.3 kg  | 25.5 | 19.8%    | –                     | –         | –          |
| 12/30/2017 | 01:00 | 90.4 kg  | 49.4 kg  | 25.6 | 24%      | –                     | –         | –          |
| 12/30/2017 | 01:00 | 41.0 kg  | 49.3 kg  | 25.5 | 24.4%    | –                     | –         | –          |

---

## Common Use Cases

### 1. Merging Garmin Weight Files
- Process and append data from multiple Garmin CSV files into a single dataset.
- **Example**:
  ```bash
  python3 garmin-convert-weight.py file1.csv combined_output.csv
  python3 garmin-convert-weight.py file2.csv combined_output.csv
  ```

### 2. Data Transformation
- Convert raw Garmin data into a structured and date-aligned format for further analysis.
- **Example**:
  ```bash
  python3 garmin-convert-weight.py raw_input.csv formatted_output.csv
  ```

---

## Notes
- Ensure your input file follows the expected structure (timestamps should be below their associated dates).
- The `--overwrite` flag can be used for situations where the output file needs to be recreated instead of appended.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Let me know if you have any questions or need additional help! 🚀
