# Navigation and UI Test Cases

## TC-NAV-001: Homepage loads successfully
Feature: Navigation
  Scenario: Homepage renders without errors
    Given the user opens the application URL
    Then the homepage loads within 3 seconds
    And the page title is visible
    And the main navigation menu is displayed

## TC-NAV-002: Unauthenticated user redirected to login
Feature: Navigation
  Scenario: Protected page redirects to login when not authenticated
    Given the user is not logged in
    When the user navigates directly to a protected URL
    Then the user is redirected to the login page
    And an appropriate message is displayed

## TC-NAV-003: Navigation between main sections
Feature: Navigation
  Scenario: User navigates between application sections
    Given the user is logged in
    When the user clicks on "Accounts Overview" in the navigation
    Then the Accounts Overview page is displayed
    When the user clicks on "Transfer Funds"
    Then the Transfer Funds page is displayed

## TC-NAV-004: 404 page shown for invalid URL
Feature: Navigation
  Scenario: Non-existent page returns an appropriate error
    Given the user is logged in
    When the user navigates to a URL that does not exist
    Then a 404 or error page is displayed
    And the user can navigate back to a valid page

## TC-NAV-005: Back button preserves application state
Feature: Navigation
  Scenario: Browser back button returns user to previous page
    Given the user has navigated from the dashboard to the accounts page
    When the user clicks the browser back button
    Then the user is returned to the dashboard
    And the dashboard content is displayed correctly

## TC-NAV-006: Page renders correctly after refresh
Feature: Navigation
  Scenario: Page state is maintained or correctly reset after refresh
    Given the user is on the accounts overview page
    When the user refreshes the browser
    Then the page reloads without errors
    And the user remains logged in
    And the accounts data is displayed