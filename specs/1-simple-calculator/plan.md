# Implementation Plan: Simple Streamlit Calculator

## 1. Technical Context

This project will implement a simple calculator using Python and Streamlit. The core logic for arithmetic operations will be encapsulated in pure Python functions, and Streamlit will be used to build the interactive web-based user interface.

**Assumptions**:
- Python 3.x environment is available.
- Streamlit library is installed.

## 2. File Structure

```
.
├── .streamlit/
│   └── config.toml           # Streamlit configuration (optional, for custom themes etc.)
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore file
├── README.md                 # Project README
├── tests/
│   ├── __init__.py
│   └── test_calculator.py    # Unit tests for calculator logic
└── specs/
    └── 1-simple-calculator/
        ├── spec.md           # Feature specification
        ├── plan.md           # This implementation plan
        └── checklists/
            └── requirements.md # Specification quality checklist
```

## 3. Implementation Steps

### Phase 1: Setup and Core Logic

1.  **Initialize Project**:
    *   Create `app.py`, `requirements.txt`, `.gitignore`, `README.md`.
2.  **Define Core Calculator Functions**:
    *   Create functions for `add`, `subtract`, `multiply`, `divide` in `app.py`.
    *   Implement error handling for division by zero within the `divide` function.
3.  **Setup Streamlit Basic UI**:
    *   Import `streamlit` in `app.py`.
    *   Add a title to the Streamlit app.

### Phase 2: Build Streamlit UI

1.  **Number Inputs**:
    *   Add two `st.number_input` widgets for the first and second numbers.
2.  **Operation Dropdown**:
    *   Add an `st.selectbox` widget for selecting the operation (Add, Subtract, Multiply, Divide).
3.  **Calculate Button**:
    *   Add an `st.button` widget to trigger the calculation.
4.  **Display Result/Error**:
    *   Use `st.empty()` or `st.write()` to display the calculation result or error message based on the button click.

### Phase 3: Testing and Refinement

1.  **Write Unit Tests**:
    *   Create `tests/test_calculator.py`.
    *   Write unit tests for `add`, `subtract`, `multiply`, `divide` functions, including edge cases like division by zero.
2.  **Run Tests**:
    *   Execute tests using `pytest`.
3.  **Refine UI/UX**:
    *   Adjust Streamlit layout and styling for a cleaner appearance if necessary.
    *   Ensure error messages are clear and user-friendly.

## 4. Flow

1.  User accesses the Streamlit application via a web browser.
2.  Application displays two number input fields, an operation dropdown, and a calculate button.
3.  User enters numbers into the input fields and selects an operation.
4.  User clicks the "Calculate" button.
5.  On button click:
    *   The selected numbers and operation are retrieved.
    *   The appropriate arithmetic function is called.
    *   If division by zero occurs, a specific error message is generated.
    *   The result or error message is displayed on the Streamlit interface.

## 5. Functions

### `app.py`

-   `add(num1: float, num2: float) -> float`
-   `subtract(num1: float, num2: float) -> float`
-   `multiply(num1: float, num2: float) -> float`
-   `divide(num1: float, num2: float) -> float` (Includes `ZeroDivisionError` handling)
-   `main()`: Streamlit application entry point, handles UI and calls arithmetic functions.

### `tests/test_calculator.py`

-   `test_add()`
-   `test_subtract()`
-   `test_multiply()`
-   `test_divide_success()`
-   `test_divide_by_zero()`

## 6. Testing Plan

### Unit Testing

-   **Tool**: `pytest`
-   **Scope**: Individual arithmetic functions (`add`, `subtract`, `multiply`, `divide`).
-   **Cases**:
    -   Positive and negative number inputs.
    -   Zero inputs.
    -   Floating-point numbers.
    -   Specific test case for `divide` with a second input of zero to confirm `ZeroDivisionError` handling and error message.

### Integration Testing (Manual)

-   **Tool**: Streamlit application itself.
-   **Scope**: End-to-end flow of the UI and core logic integration.
-   **Cases**:
    -   Verify all user scenarios outlined in `spec.md` (performing each operation correctly, handling division by zero).
    -   Check UI responsiveness and clarity of result/error messages.

## 7. Risks and Mitigations

-   **Risk**: Non-numeric input from `st.number_input`.
    -   **Mitigation**: `st.number_input` inherently handles non-numeric input by providing default values or type coercion, reducing the risk of application crashes due to invalid types. We will rely on Streamlit's built-in handling.

## 8. Architectural Decisions (No ADRs suggested at this point)

-   **Decision**: Using Streamlit for the UI.
    -   **Rationale**: Simplifies UI development for a basic Python application, aligns with the "clean UI" and "simple functions" requirements.
    -   **Alternatives Considered**: Flask/Django with custom frontend (overkill for a simple calculator), Tkinter/PyQt (desktop app, not web-based).

## 9. Next Steps

-   Create the necessary project files (app.py, requirements.txt, .gitignore, README.md, tests/).
-   Implement the core arithmetic functions.
-   Develop the Streamlit UI.
-   Write and run unit tests.
-   Manually test the Streamlit application.
