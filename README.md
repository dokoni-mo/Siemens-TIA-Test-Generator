# TIA Portal V19 Autotest Generator

This Python script is designed to **automatically generate test cases** for the **TIA Portal V19 test suite by Siemens**. It simplifies the process of creating test cases by automating the generation of test steps, actions, and expected outcomes based on predefined logic and configurations.

The script is flexible and can be adapted to various test scenarios. The provided **valve control logic test cases** are just an example of how the script can be used to generate test cases for a specific application.

---

## Overview
The **TIA Portal V19 Autotest Generator** is a Python script that automates the creation of test cases for Siemens' TIA Portal V19. It is particularly useful for engineers and developers who need to generate large sets of test cases for PLC (Programmable Logic Controller) programs or other automation systems.

The script takes input configurations (e.g., test scenarios, variables, and actions) and generates structured test cases in a format compatible with TIA Portal V19(.TAT). This saves time and reduces the risk of human error when creating test cases manually.

---

## Features
- **Automated Test Case Generation**: Generates test cases based on predefined logic and configurations.
- **Flexible Input**: Allows customization of test scenarios, actions, and variables.
- **Compatible with TIA Portal V19**: Outputs test cases in a format(.TAT) that can be imported into Siemens' TIA Portal V19.
- **Example Provided**: Includes an example of valve control logic test cases to demonstrate how the script works.

---

## How It Works
1. **Input Configuration**: The script reads input configurations (e.g., test scenarios, actions, and variables) from a structured file (e.g., Excel, JSON, or CSV).
2. **Test Case Generation**: Based on the input, the script generates test cases with steps, actions, and expected outcomes.
3. **Output**: The generated test cases are saved in a format(.TAT) compatible with TIA Portal V19, ready for import and execution.

---

## Usage
Prepare Input Configuration:
Define your test scenarios, actions, and variables in a structured file (e.g., Excel, JSON, or CSV).
Refer to the provided test_cases.xlsx file for an example.

The generated test cases will be saved in a compatible format (.TAT).

Import the file into TIA Portal V19 to execute the tests.
