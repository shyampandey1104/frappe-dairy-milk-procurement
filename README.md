# Frappe Dairy Milk Procurement & Payout Engine 🥛🐄

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Frappe](https://img.shields.io/badge/Frappe-v14%20%7C%20v15-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)

An automated Village Dairy Cooperative Society (VDCS) milk collection, ultrasonic milk analyzer fat/SNF dual-rate chart calculation, and direct farmer bank payout engine for **Frappe Framework & ERPNext Dairy Cooperatives** (Amul, Mother Dairy, Nandini cooperative model).

---

## 🚀 Key Features

- **Morning & Evening Shift Collection**: Real-time batch recording of Cow and Buffalo milk liters.
- **Dual Axis Fat% & SNF% Rate Chart**: Computes scientific price per liter according to fat purity and solids-not-fat deltas.
- **Adulteration & Dilution Penalty**: Automatically flags watered-down batches with SNF < 7.8% and applies quality adjustment penalties.
- **Direct Payout Slips & Passbooks**: Instant printing of payment vouchers and integration with ERPNext `Farmer Accounts Payable`.

---

## 📦 Installation & Setup

```bash
git clone https://github.com/shyampandey1104/frappe-dairy-milk-procurement.git
cd frappe-dairy-milk-procurement
pip install -r requirements.txt
```

---

## 🛠️ Usage Example

```python
from dairy.engine import DairyProcurementEngine, MilkCollectionEntry

engine = DairyProcurementEngine()

entry = MilkCollectionEntry(
    farmer_code="F-882",
    farmer_name="Gurmeet Singh",
    shift="MORNING",
    animal_type="COW",
    quantity_liters=22.0,
    fat_percentage=4.1,
    snf_percentage=8.7
)

slip = engine.calculate_farmer_payout(entry)
print(f"Rate: ₹{slip.rate_per_liter}/L | Total Payout: ₹{slip.total_amount}")
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📄 License
MIT License. Created with ❤️ by [Shyam Pandey](https://github.com/shyampandey1104).
