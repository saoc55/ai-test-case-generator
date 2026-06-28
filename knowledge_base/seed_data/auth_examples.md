# Authentication Test Cases

## TC-AUTH-001: Valid login with correct credentials
Feature: User Authentication
  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters a valid email "john@example.com"
    And the user enters a valid password "demo"
    And the user clicks the Login button
    Then the user is redirected to the dashboard
    And a welcome message is displayed

## TC-AUTH-002: Login fails with invalid password
Feature: User Authentication
  Scenario: Login rejected with incorrect password
    Given the user is on the login page
    When the user enters a valid email "john@example.com"
    And the user enters an incorrect password "wrongpass"
    And the user clicks the Login button
    Then an error message "Invalid credentials" is displayed
    And the user remains on the login page

## TC-AUTH-003: Login fails with unregistered email
Feature: User Authentication
  Scenario: Login rejected with unknown email
    Given the user is on the login page
    When the user enters an unregistered email "unknown@example.com"
    And the user enters any password "anypass"
    And the user clicks the Login button
    Then an error message "Invalid credentials" is displayed
    And the user remains on the login page

## TC-AUTH-004: Login fails with empty fields
Feature: User Authentication
  Scenario: Login blocked when fields are empty
    Given the user is on the login page
    When the user leaves the email field empty
    And the user leaves the password field empty
    And the user clicks the Login button
    Then a validation error is displayed
    And the form is not submitted

## TC-AUTH-005: Successful logout
Feature: User Authentication
  Scenario: User logs out successfully
    Given the user is logged in
    When the user clicks the Logout button
    Then the user is redirected to the login page
    And the session is terminated
    And accessing a protected page redirects back to login

## TC-AUTH-006: Valid user registration
Feature: User Registration
  Scenario: New user registers with valid data
    Given the user is on the registration page
    When the user fills in all required fields with valid data
    And the user submits the registration form
    Then the account is created successfully
    And the user is redirected to the login page

## TC-AUTH-007: Registration rejected with duplicate email
Feature: User Registration
  Scenario: Registration blocked for existing email
    Given the user is on the registration page
    When the user enters an email that is already registered
    And the user fills in the remaining fields
    And the user submits the registration form
    Then an error message "Email already in use" is displayed
    And no new account is created

## TC-AUTH-008: Registration fails with invalid email format
Feature: User Registration
  Scenario: Registration blocked with malformed email
    Given the user is on the registration page
    When the user enters an invalid email format "notanemail"
    And the user fills in the remaining fields
    And the user submits the registration form
    Then a validation error "Please enter a valid email" is displayed

## TC-AUTH-009: Password reset with valid email
Feature: Password Reset
  Scenario: Password reset email sent for valid account
    Given the user is on the forgot password page
    When the user enters a registered email "john@example.com"
    And the user clicks Send Reset Link
    Then a confirmation message is displayed
    And a password reset email is sent to the address

## TC-AUTH-010: Password reset with unregistered email
Feature: Password Reset
  Scenario: Password reset blocked for unknown email
    Given the user is on the forgot password page
    When the user enters an unregistered email "nobody@example.com"
    And the user clicks Send Reset Link
    Then an error message "Email not found" is displayed
    And no reset email is sent

## TC-AUTH-011: Password reset with expired token
Feature: Password Reset
  Scenario: Password reset rejected with expired link
    Given the user has received a password reset email
    And the reset link has expired
    When the user clicks the reset link
    Then an error message "This link has expired" is displayed
    And the user is prompted to request a new reset link

## TC-AUTH-012: Session expires after inactivity
Feature: Session Management
  Scenario: User session times out after inactivity
    Given the user is logged in
    When the user is inactive for the session timeout period
    Then the session is automatically terminated
    And the user is redirected to the login page
    And a message "Your session has expired" is displayed