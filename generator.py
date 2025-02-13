import pandas as pd
import os

# Constants
DEFAULT_DURATION = 100
START_COL = "Duration (ms)"
END_COL = "Comment"

# Helper function: Extract variables from the "Variable" column
def extract_variables(variable_column):
    variables = set()
    for row in variable_column.dropna():
        for entry in row.split(", "):
            if "=" in entry:
                var_name = entry.split("=")[0].strip()
            else:
                var_name = entry.strip()
            variables.add(var_name)
    return variables

# Helper function: Generate test step actions
def generate_actions(row):
    actions = []
    if pd.notna(row["Variable"]):
        for entry in row["Variable"].split(", "):
            if "=" in entry:
                var_name, var_value = map(str.strip, entry.split("=", 1))
                actions.append(f"{var_name} := {var_value};")
            else:
                action_value = "TRUE" if row['Action'] == 'Turn on' else "FALSE"
                actions.append(f"{entry.strip()} := {action_value};")
    return actions

# Helper function: Generate assertions
def generate_assertions(row, output_columns):
    assertions = []
    for output_col in output_columns:
        if pd.notna(row[output_col]):
            value = (
                "TRUE" if isinstance(row[output_col], bool) and row[output_col]
                else "FALSE" if isinstance(row[output_col], bool)
                else str(int(row[output_col])) if isinstance(row[output_col], (int, float))
                else row[output_col]
            )
            assertions.append(f"  ASSERT.Equal({output_col}, {value});")
    return assertions

# Helper function: Generate a single test step
def generate_test_step(row, output_columns):
    step_desc = f'STEP: "{row["Test steps"]} {row["Test case"]}"'
    actions = "\n  ".join(generate_actions(row))
    duration = int(row["Duration (ms)"]) if pd.notna(row["Duration (ms)"]) else DEFAULT_DURATION
    assertions = "\n".join(generate_assertions(row, output_columns))

    return (
        f"{step_desc}\n"
        f"  {actions}\n"
        f"  RUN (Time := T#{duration}ms);\n"
        f"{assertions}\n"
        f"END_STEP\n"
    )

# Helper function: Generate VAR block
def generate_var_block(logic_block_name, inputs, outputs):
    return (
        "VAR\n"
        + "\n".join(f"  {var}:\"{logic_block_name}\".{var};" for var in sorted(inputs.union(outputs)))
        + "\nEND_VAR\n\n"
    )

# Process all CSV files in the current directory
def process_csv_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path)
            df[['Test scenario', 'Test case']] = df[['Test scenario', 'Test case']].ffill()

            # Extract logic block name
            logic_block_name = os.path.splitext(filename)[0]

            # Extract unique variables and output columns
            all_variables = extract_variables(df["Variable"])
            output_columns = df.columns[df.columns.get_loc(START_COL) + 1 : df.columns.get_loc(END_COL)]

            # Generate all test cases grouped by Test Scenario
            output_file = logic_block_name + ".TAT"
            with open(output_file, "w") as file:
                for scenario_name, group in df.groupby("Test scenario"):
                    inputs = extract_variables(group["Variable"])
                    outputs = set(output_columns)

                    # Write TEST_CASE header and VAR block for the scenario
                    file.write(f'TEST_CASE "{logic_block_name}, {scenario_name}"\n')
                    file.write(generate_var_block(logic_block_name, inputs, outputs))

                    # Write test steps
                    test_steps = "\n".join(group.apply(generate_test_step, axis=1, output_columns=output_columns))
                    file.write(test_steps)
                    file.write("\nEND_TEST_CASE\n\n")

            print(f"Test scenarios saved to: {output_file}")

# Run the script for the current directory
process_csv_files(os.getcwd())