# Financial transaction processing

The Scenario: At Saturn, we ingest financial data from various back-office systems. You need to write a processor that takes a list of raw transaction dictionaries and:

1. Validates the data (ensure amounts are numbers, dates are present).
2. Identifies "High-Risk" transactions based on two rules:
   - Any transaction over £10,000.
   - Any transaction involving a specific list of "High-Risk Countries."
3. Aggregates the total value of high-risk transactions per category.

Requirements:
- Use Pydantic for the data model (shows Staff-level data integrity).
- Handle "dirty" data (e.g., a dictionary missing a key or having a string instead of a float) without crashing.
- Write it in a way that is testable and modular.