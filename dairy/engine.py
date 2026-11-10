"""Dairy Milk Procurement, Fat% & SNF% Two-Axis Rate Chart Payout Engine."""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class MilkCollectionEntry(BaseModel):
    farmer_code: str
    farmer_name: str
    shift: str          # MORNING or EVENING
    animal_type: str    # COW or BUFFALO
    quantity_liters: float
    fat_percentage: float  # e.g., 3.5% to 4.5% for Cow, 6.5% to 8.5% for Buffalo
    snf_percentage: float  # Solids-Not-Fat (e.g., 8.0% to 9.5%)


class FarmerPayoutSlip(BaseModel):
    farmer_code: str
    farmer_name: str
    shift: str
    animal_type: str
    quantity_liters: float
    fat_pct: float
    snf_pct: float
    rate_per_liter: float
    total_amount: float
    quality_grade: str  # PREMIUM, STANDARD, SUB_STANDARD_DILUTED


class DairyProcurementEngine:
    """Computes instant farmer milk payout based on fat/SNF dual-rate matrix."""

    # Base standards (Amul/NDDB model)
    # Cow Milk: Standard 3.5% Fat, 8.5% SNF -> Base ₹36.0/L
    # Buffalo Milk: Standard 6.5% Fat, 9.0% SNF -> Base ₹54.0/L

    def calculate_farmer_payout(self, entry: MilkCollectionEntry) -> FarmerPayoutSlip:
        if entry.quantity_liters <= 0:
            raise ValueError("Milk quantity must be greater than zero.")

        animal = entry.animal_type.upper()
        if animal == "COW":
            base_rate = 36.0
            std_fat = 3.5
            std_snf = 8.5
            fat_incentive_rate = 3.5  # per 1.0% fat delta
            snf_incentive_rate = 2.0  # per 1.0% SNF delta
        else:  # BUFFALO
            base_rate = 54.0
            std_fat = 6.5
            std_snf = 9.0
            fat_incentive_rate = 4.5
            snf_incentive_rate = 2.5

        # Check for water adulteration / dilution
        if entry.snf_percentage < 7.8:
            quality = "SUB_STANDARD_DILUTED"
            penalty_multiplier = 0.85
        elif (animal == "COW" and entry.fat_percentage >= 4.2) or (animal == "BUFFALO" and entry.fat_percentage >= 7.5):
            quality = "PREMIUM"
            penalty_multiplier = 1.0
        else:
            quality = "STANDARD"
            penalty_multiplier = 1.0

        # Dynamic rate calculation
        fat_diff = entry.fat_percentage - std_fat
        snf_diff = entry.snf_percentage - std_snf
        computed_rate = (base_rate + (fat_diff * fat_incentive_rate) + (snf_diff * snf_incentive_rate)) * penalty_multiplier
        final_rate = max(18.0, round(computed_rate, 2))

        total_amount = round(entry.quantity_liters * final_rate, 2)

        return FarmerPayoutSlip(
            farmer_code=entry.farmer_code,
            farmer_name=entry.farmer_name,
            shift=entry.shift.upper(),
            animal_type=animal,
            quantity_liters=round(entry.quantity_liters, 2),
            fat_pct=entry.fat_percentage,
            snf_pct=entry.snf_percentage,
            rate_per_liter=final_rate,
            total_amount=total_amount,
            quality_grade=quality
        )
