from typing import List, Dict

from pydantic import BaseModel


# 1. Define your Pydantic Model here
class Transaction(BaseModel):
    id: int
    amount: float
    category: str
    country: str


class TransactionProcessor:
    def __init__(self, high_risk_countries: List[str]):
        self.high_risk_countries = set(high_risk_countries)

    def _is_high_risk(self, tran: Transaction) -> bool:
        if tran.amount > 10000 or tran.country in self.high_risk_countries:
            return True
        return False

    def process_raw_data(self, raw_data: List[Dict]) -> Dict[str, float]:
        """
        Process raw dictionaries, validate them, and return a summary of
        high-risk totals per category.
        """
        # 2. Implement your logic here
        summary = {}
        for item in raw_data:
            tran = Transaction(**item)
            if self._is_high_risk(tran):
                summary[tran.category] = summary.get(tran.category, 0) + tran.amount

        return summary


# --- Test Data ---
raw_input = [
    {"id": 1, "amount": 12000.0, "category": "Investment", "country": "UK"},
    {"id": 2, "amount": 500.0, "category": "Transfer", "country": "Cayman Islands"},
    {"id": 3, "amount": "invalid", "category": "Gift", "country": "UK"}, # Dirty data
    {"id": 4, "amount": 15000.0, "category": "Investment", "country": "France"},
]

# High Risk Countries to check against
risk_list = ["Cayman Islands", "Panama"]

# 3. Execution
processor = TransactionProcessor(risk_list)
print(processor.process_raw_data(raw_input))