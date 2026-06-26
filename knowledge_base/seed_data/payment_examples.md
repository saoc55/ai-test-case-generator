# Payment and Transfer Test Cases

## TC-PAY-001: Valid fund transfer between accounts
Feature: Fund Transfer
  Scenario: User transfers funds between own accounts
    Given the user is logged in
    And the user has at least two accounts with sufficient balance
    When the user navigates to the Transfer Funds page
    And selects a source account
    And selects a destination account
    And enters a valid transfer amount "100"
    And clicks the Transfer button
    Then the transfer is completed successfully
    And the source account balance is reduced by 100
    And the destination account balance is increased by 100

## TC-PAY-002: Transfer rejected with insufficient funds
Feature: Fund Transfer
  Scenario: Transfer blocked when balance is too low
    Given the user is logged in
    And the source account has a balance of 50
    When the user attempts to transfer 200
    And clicks the Transfer button
    Then an error message "Insufficient funds" is displayed
    And no transfer is executed
    And both account balances remain unchanged

## TC-PAY-003: Transfer rejected with zero amount
Feature: Fund Transfer
  Scenario: Transfer blocked for zero amount
    Given the user is logged in
    When the user enters 0 as the transfer amount
    And clicks the Transfer button
    Then a validation error "Amount must be greater than zero" is displayed
    And no transfer is executed

## TC-PAY-004: Transfer rejected with negative amount
Feature: Fund Transfer
  Scenario: Transfer blocked for negative amount
    Given the user is logged in
    When the user enters -50 as the transfer amount
    And clicks the Transfer button
    Then a validation error is displayed
    And no transfer is executed

## TC-PAY-005: Transfer rejected to same account
Feature: Fund Transfer
  Scenario: Transfer blocked when source and destination are the same
    Given the user is logged in
    When the user selects the same account as both source and destination
    And enters a valid amount
    And clicks the Transfer button
    Then an error message "Source and destination accounts must differ" is displayed
    And no transfer is executed

## TC-PAY-006: Transfer amount appears in transaction history
Feature: Fund Transfer
  Scenario: Completed transfer is recorded in transaction history
    Given the user has completed a transfer of 75
    When the user navigates to the transaction history for the source account
    Then a debit transaction of 75 is listed
    And the transaction type is "Debit"
    And the transaction date matches today's date

## TC-PAY-007: Loan request submitted successfully
Feature: Loan Request
  Scenario: User requests a loan with valid data
    Given the user is logged in
    When the user navigates to the loan request page
    And enters a valid loan amount and down payment
    And selects a valid account
    And submits the loan request
    Then a loan approval decision is displayed
    And the result is either approved or denied with a reason

## TC-PAY-008: Loan request rejected with missing fields
Feature: Loan Request
  Scenario: Loan request blocked when required fields are empty
    Given the user is on the loan request page
    When the user leaves the loan amount empty
    And submits the form
    Then a validation error is displayed
    And no loan request is submitted