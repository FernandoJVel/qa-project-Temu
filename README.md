# TEMU E2E AUTOMATION TESTING

*Description*
=

This project was developed to automate and
validate a critical end-to-end purchasing workflow 
within the TEMU web application using Selenium WebDriver 
and Python.

The objective was to simulate a real customer 
journey, starting from account access and continuing
through product selection, cart management, checkout,
and purchase order generation. The automation was designed 
to verify the stability, functionality, and user 
experience of the purchasing process while applying 
industry-standard UI automation practices.

Although the complete workflow could not be executed 
due to TEMU's anti-bot protection mechanisms, the project 
demonstrates the design and implementation of a robust 
automation framework capable of handling complex user 
interactions and dynamic web elements.
---
## Test Objective
The automated test was designed to validate the following 
business flow:
1. User authentication.
2. Product search and selection.
3. Shopping cart validation.
4. Checkout process execution.
5. Shipping information verification.
6. Payment method selection.
7. OXXO payment option selection.
8. Purchase order generation.
9. Final confirmation validation.

The goal was to verify that users could 
successfully complete the purchasing process 
from beginning to end while ensuring that all 
critical business requirements were met.
---
## Main Files:

- `main.py` - Contains the automated test scenario 
that executes the purchasing workflow and validates 
each step of the process.

- `locators.py` - Stores all web element locators used 
throughout the automation project, improving 
maintainability and readability.


- `data.py` - Contains test data, user credentials, 
product information, and configuration values required 
for test execution.
---
## Technologies Used

### Programming Language:

- Python:  
Primary language used to develop the automation framework.

### Automation Tools:

- Selenium WebDriver:  
Used to automate browser interactions and simulate real user actions.


- WebDriverWait:  
Used to implement explicit waits and improve test reliability when
interacting with dynamic web elements.
---
## Testing Techniques Applied

- End-to-End Testing (E2E):  
Validation of the complete purchasing 
workflow across multiple application screens.

+ UI Automation Testing:  
Automated interaction with web interface components.

* Functional Testing:  
Verification of business requirements
and expected application behavior.

- Regression Testing:  
Validation that existing 
functionality remains stable and operational.
---
## Locator Strategies:

- The project uses multiple locator types
to improve automation stability and maintainability:
  + ID
  + Class Name
  + XPath
  + CSS Selectors
---
## Why the Test Could Not Be Fully Executed
During execution, TEMU's anti-bot protection system detected
the automated browser session and blocked further progression 
in the workflow.

The automation successfully interacted with multiple
pages and elements; however, after entering the email
address and attempting to continue to the next step, 
the platform prevented the automated session from proceeding.

This behavior is common in large e-commerce platforms 
that implement advanced bot-detection mechanisms to 
protect against automated traffic, scraping, and 
fraudulent activity.

As a result, the final checkout and purchase 
order generation steps could not be completed 
through automation.
---
## Key Learnings
This project provided valuable experience in:

- __Selenium Framework Design__  
Building a maintainable automation structure
using separated locators, test data, and test logic.

* __Dynamic Element Handling__  
Working with explicit waits and synchronization
techniques for modern web applications.

+ __Locator Strategy Selection__  
Using multiple locator types to improve 
test robustness and maintainability.

- __End-to-End Test Design__  
Designing automated scenarios that replicate real 
customer journeys and business workflows.

* __Real-World Automation Challenges__  
Understanding how anti-bot protection systems can 
impact UI automation efforts in production environments.

+ __Test Analysis and Troubleshooting__  
Investigating automation limitations and identifying 
external factors that affect test execution.
---
## Best Practices Implemented
- Clear Test Structure:  
Well-organized and maintainable automation architecture.

+ Reusable Components:  
Separation of locators, test data, and business 
logic to improve maintainability.

* Descriptive Naming Conventions:  
Meaningful variable, function, and test names.

- Explicit Wait Strategy:  
Proper use of WebDriverWait to increase test 
stability and reliability.

+ Readable and Scalable Code:  
Framework designed to support future enhancements 
and additional test scenarios.
---
## Project Outcome
Although the complete workflow could not 
be finalized due to TEMU's anti-bot protection 
mechanisms, the project successfully 
demonstrates practical experience in: 

- Selenium WebDriver
- Python Automation
- UI Testing
- End-to-End Test Design
- Functional Testing
- Regression Testing
- Test Architecture
- Locator Strategies
- Dynamic Element Handling
- Test Analysis and Troubleshooting
- Software Quality Assurance

This project reflects the challenges that 
QA Engineers may encounter when automating 
real-world applications and highlights the 
importance of designing reliable, 
maintainable, and scalable test automation solutions.