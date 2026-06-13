# TEMU E2E AUTOMATION TESTING

*Description*
=

This project contains an end-to-end
automated test scenario for the TEMU 
web application using Selenium 
WebDriver. The test automates the 
complete user journey, starting from 
user login and ending with the 
generation of a purchase order for 
payment at OXXO. The objective is to
validate critical business flows, ensure
application stability, and verify that 
the checkout process functions 
correctly from start to finish.

## Main Files:

- `main.py` - Contains all automated test 
cases that execute the end-to-end purchasing 
workflow, including login, product selection,
cart management, checkout, and purchase order 
generation.


- `locators.py` - Stores all web element locators 
used throughout the automation framework, 
improving maintainability and readability.


- `data.py` - Contains test data, user credentials,
product information, and configuration values
required for test execution.

## Technologies and Testing Techniques Used

### Programming Language:

- Python:  
Primary language used for developing 
automated test scripts.

### Automation Frameworks and Tools:

- Selenium WebDriver:  
Used to automate browser interactions 
and validate user actions across the application.


- WebDriverWait:  
Implements explicit waits to handle dynamic
web elements and improve test reliability.

### Testing Approaches

- End-to-End (E2E) Testing:  
Validates the complete purchasing workflow 
from login to payment order generation.


- Functional Testing:  
Verifies that each feature behaves 
according to business requirements.


- Regression Testing:  
Ensures existing functionality 
remains stable after changes or updates.


- UI Automation Testing:  
Automates user interface interactions 
to validate critical user journeys.

````
### Locator Strategies:

- Multiple locator types are used to ensure
robust and maintainable test automation: 

  + ID
  + Class Name
  + XPath
  + CSS Selectors
  + Name
  + Tag Name 

### Automated Test Flow
- The automated scenario includes:
  * User Login
  * Product Search
  * Product Selection
  * Add Product to Cart
  * Shopping Cart Validation
  * Checkout Process
  * Shipping Information Validation
  * Payment Method Selection
  * OXXO Payment Option Selection
  * Purchase Order Generation
  * Final Confirmation Validation

### Interaction Techniques

- Form Handling:
  - Text field completion
  - Dropdown selection
  - Checkbox and radio button interaction


- Navigation Actions:
  - Button clicks
  - Page navigation
  - Checkout workflow execution


- Dynamic Element Handling:
  - Explicit waits
  - Element visibility validation
  - Synchronization management

### Best Practices Implemented
- Clear Test Structure:  
Well-organized and maintainable 
code architecture.


- Descriptive Naming Convention:  
Meaningful variable, function, and test names.


- Reusable Components:  
Common actions and locators are 
separated to improve maintainability.


- Explicit Waits:  
Proper use of WebDriverWait for
stable and reliable test execution.


- Readable and Scalable Code:  
Framework designed to support future
test case expansion and maintenance.
````