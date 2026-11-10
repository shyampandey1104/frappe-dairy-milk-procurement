import unittest
from dairy.engine import DairyProcurementEngine, MilkCollectionEntry


class TestDairyProcurement(unittest.TestCase):
    def setUp(self):
        self.engine = DairyProcurementEngine()

    def test_cow_milk_payout(self):
        entry = MilkCollectionEntry(
            farmer_code="FARM-440",
            farmer_name="Sukhwinder Gill",
            shift="MORNING",
            animal_type="COW",
            quantity_liters=18.5,
            fat_percentage=4.0,  # +0.5 over 3.5
            snf_percentage=8.8   # +0.3 over 8.5
        )
        slip = self.engine.calculate_farmer_payout(entry)
        self.assertGreater(slip.rate_per_liter, 36.0)
        self.assertEqual(slip.quality_grade, "STANDARD")
        self.assertGreater(slip.total_amount, 650.0)

    def test_water_diluted_penalty(self):
        entry = MilkCollectionEntry(
            farmer_code="FARM-441",
            farmer_name="Devendra Yadav",
            shift="EVENING",
            animal_type="BUFFALO",
            quantity_liters=25.0,
            fat_percentage=5.0,
            snf_percentage=7.2  # low SNF indicating dilution
        )
        slip = self.engine.calculate_farmer_payout(entry)
        self.assertEqual(slip.quality_grade, "SUB_STANDARD_DILUTED")


if __name__ == "__main__":
    unittest.main()
