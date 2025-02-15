# TIA Portal V19 Autotest Generator

The TIA Portal V19 Autotest Generator is a Python script that automates the creation of test cases for Siemens' TIA Portal V19. It is particularly useful for engineers and developers who need to generate large sets of test cases for PLC (Programmable Logic Controller) programs or other automation systems.

The script takes input configurations (e.g., test scenarios, variables, and actions) and generates structured test cases in a format compatible with TIA Portal V19 (`.TAT`). This saves time and reduces the risk of human error when creating test cases manually.

---

## Features

- **Automated Test Case Generation**: Generates test cases based on predefined logic and configurations.
- **Flexible Input**: Allows customization of test scenarios, actions, and variables.
- **Compatible with TIA Portal V19**: Outputs test cases in a format (`.TAT`) that can be imported into Siemens' TIA Portal V19.
- **Example Provided**: Includes an example of valve control logic test cases to demonstrate how the script works.

---

## How It Works

1. **Input CSV Files**: The script reads CSV files from the current directory. Each CSV file should contain test case data with specific columns that must meet the requirements listed below.
2. **Variable Extraction**: The script extracts variables from the `Variable` column, which can include assignments (e.g., `cmdon`, `cmOpen`, `resetError`) or simple variable names.
3. **Test Step Generation**: For each row in the CSV, the script generates test steps, including actions (e.g., setting variables) and assertions (e.g., checking output values).
4. **Output `.TAT` Files**: The script generates a `.TAT` file for each CSV file, containing the test scenarios, variables, and test steps in a structured format.

---

## Usage

### Step 1: Prepare Input CSV Files

Create a CSV file, which should be same name with your block in TIA portal, with the required columns:

- **Test scenario**: The name of the test scenario (e.g., "Valve Control").
- **Test case**: The name of the test case (e.g., "Open Valve").
- **Action**: The boolean value to be applied to the variables.
- **Variable**: The variables to be set or checked. Use `var_name = value` for assignments or just `var_name` for boolean actions (e.g., `cmdon`, `cmOpen`, `resetError`).
- **Duration (ms)**: The duration of the test step in milliseconds. If not specified, the script defaults to `100ms`.
- **Output Columns**: These are the columns between `Duration (ms)` and `Comment` in the CSV file, representing the expected output values (e.g., `open`, `openUpSeat`, `openLoSeat`, `error`).
- **Comment**: A comment or description for the test case (optional).

### Step 2: Run the Script

1. Open a terminal or command prompt.
2. Navigate to the directory where the script (`generator.py`) and your CSV files are located.
3. Run the script using Python:
   ```bash
   python generator.py

### Step 3: Check the Output
The script will generate .TAT files in the same directory, named after the CSV files.
Each .TAT file contains the test scenarios, variables, and test steps in a structured format compatible with TIA Portal V19.
Example .TAT output:
   ```bash
TEST_CASE "ValveControl, Valve Control"
VAR
  cmdon:"ValveControl".cmdon;
  cmOpen:"ValveControl".cmOpen;
END_VAR

STEP: "Open Valve"
  cmdon := TRUE;
  RUN (Time := T#50ms);
  ASSERT.Equal(Output1, TRUE);
  ASSERT.Equal(Output2, FALSE);
END_STEP

STEP: "Close Valve"
  cmOpen := FALSE;
  RUN (Time := T#100ms);
  ASSERT.Equal(Output1, FALSE);
  ASSERT.Equal(Output2, TRUE);
END_STEP

END_TEST_CASE
   ```
### Step 4: Import into TIA Portal V19
1. Open Siemens TIA Portal V19.
2. Install [Test Suit](https://support.industry.siemens.com/cs/us/en/view/109821411) module for TIA Portal V19
3. Import the generated .TAT files into your project to use the test cases.
   
![image](https://github.com/user-attachments/assets/4673c86b-0297-4fcb-b3d1-f941e9189aa3)

5. Run tests


## Contributors
- [Evgenii-Zinner](https://github.com/Evgenii-Zinner) - Co-creator
- [Azamat Choorov](https://github.com/dokoni-mo) - Co-creator
