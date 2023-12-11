# Coffee Shop Application

## Introduction

This console-based application for a coffee shop provides a menu-driven interface to manage a list of coffees. Each coffee has attributes such as name, country of origin, and price. The application allows users to perform various operations, including adding new coffees, displaying all coffees sorted by country of origin and price, and filtering coffees based on specific criteria.

## Functionality

### 1. Initialization

- At the start of the application, at least 5 coffees are hard-coded with descriptive names.

### 2. Add a Coffee

- Users can add a new coffee by entering its name, country of origin, and price.
- The application validates that the price is a float greater than 0.
  - If the price is invalid, an error message is displayed, and the coffee is not added.

### 3. Display All Coffees

- All coffees are displayed sorted alphabetically by country of origin.
- If countries are equal, the coffees are sorted increasingly by price.

### 4. Filter Coffees

- Users can filter coffees based on country of origin and price.
- Entering a country and a price will print all coffees from that country with a price smaller or equal to the given price.
- Either country or price may be missing.
  - If country is missing, all coffees matching the given price criteria are printed.
  - If price is missing, all coffees from the given country are printed.
- If no coffees match the criteria, the message "No such coffees" is displayed.

## Specifications for Non-UI Functions

1. `add_coffee(name: str, country_of_origin: str, price: float) -> None`:
   - Adds a new coffee to the list.

2. `display_all_coffees() -> None`:
   - Displays all coffees sorted as specified.

3. `filter_coffees(country: str, price: float) -> None`:
   - Filters and prints coffees based on the provided country and price criteria.

4. `validate_price(price: float) -> bool`:
   - Validates whether the price is a float greater than 0.
   - Returns True if valid, False otherwise.

## Default Behavior

- If the user does not enter both country and price during filtering, the application will print all coffees based on the available criteria.
- If no coffees match the given criteria during filtering, the message "No such coffees" will be displayed.

## Observations

- Implementations not divided into a user interface section and functions communicating via parameters and return values are graded at 50%.
- Unrequired features and validations should not be implemented.

## *In Collaboration with @Melingu