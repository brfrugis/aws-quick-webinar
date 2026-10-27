#!/usr/bin/env python3
"""
Generates the fictitious "Aurora Electronics" data used in the Amazon Quick demo.

- No external dependencies (standard library only).
- Deterministic (fixed seed): every participant generates exactly the same numbers.

Usage:
    python3 data/generate_data.py            # writes the CSVs to data/
    python3 data/generate_data.py --output /tmp/x

Generated files:
    products.csv  - catalog (12 products)
    sales.csv     - ~7,900 order line items from Nov/2025 to Oct/2026
    targets.csv   - monthly revenue target per region

"Stories" planted in the data for the demo:
    1. Sales peak on Black Friday (Nov) and Christmas (Dec).
    2. The Northeast region grows month over month and starts hitting its target in H2.
    3. "Pulse Bluetooth Headphones" has a return rate far above the other products
       (main reason: "Manufacturing defect").
    4. The "App" channel gains share throughout the year.
"""
import argparse
import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 2026
START = date(2025, 11, 1)
END = date(2026, 10, 31)

PRODUCTS = [
    # id, name, category, price, cost
    ("P001", "Aurora X1 Smartphone", "Smartphones", 2499.00, 1650.00),
    ("P002", "Aurora Lite Smartphone", "Smartphones", 1299.00, 880.00),
    ("P003", "Aurora Pro 14 Laptop", "Laptops", 5899.00, 4300.00),
    ("P004", "Aurora Air 13 Laptop", "Laptops", 3999.00, 2900.00),
    ("P005", "Pulse Bluetooth Headphones", "Audio", 349.00, 140.00),
    ("P006", "Boom Speaker", "Audio", 599.00, 290.00),
    ("P007", "Fit 2 Smartwatch", "Wearables", 899.00, 470.00),
    ("P008", "Fitness Band", "Wearables", 249.00, 110.00),
    ("P009", "Aurora Tab 10 Tablet", "Tablets", 1899.00, 1300.00),
    ("P010", "Turbo 65W Charger", "Accessories", 179.00, 60.00),
    ("P011", "Slim Protective Case", "Accessories", 79.00, 18.00),
    ("P012", "Glide Wireless Mouse", "Accessories", 129.00, 45.00),
]

# Relative weight of each product in the sales mix
PRODUCT_WEIGHT = [8, 12, 3, 5, 14, 7, 8, 9, 5, 12, 15, 10]

REGIONS = {
    "Southeast": ["SP", "RJ", "MG", "ES"],
    "South": ["PR", "SC", "RS"],
    "Northeast": ["BA", "PE", "CE", "MA", "RN"],
    "Central-West": ["DF", "GO", "MT", "MS"],
    "North": ["AM", "PA", "TO"],
}
BASE_REGION_WEIGHT = {"Southeast": 45, "South": 18, "Northeast": 18, "Central-West": 11, "North": 8}

# Volume multiplier per month (seasonality)
SEASONALITY = {11: 1.9, 12: 1.6, 1: 0.8, 2: 0.75, 3: 0.85, 4: 0.9,
               5: 1.05, 6: 0.95, 7: 0.95, 8: 1.0, 9: 1.0, 10: 1.1}

RETURN_REASONS = ["Changed mind", "Manufacturing defect", "Not as described",
                  "Late delivery", "Damaged in transit"]


def month_index(d: date) -> int:
    """0 for Nov/2025 ... 11 for Oct/2026."""
    return (d.year - START.year) * 12 + d.month - START.month


def region_weight(d: date) -> dict:
    weights = dict(BASE_REGION_WEIGHT)
    weights["Northeast"] += month_index(d) * 1.4  # steady Northeast growth
    return weights


def channel_weight(d: date) -> dict:
    i = month_index(d)
    return {"Website": 55 - i * 1.5, "App": 20 + i * 2.0, "Marketplace": 25 - i * 0.5}


def pick(rng: random.Random, weights: dict) -> str:
    return rng.choices(list(weights), weights=list(weights.values()))[0]


def generate(output: Path) -> None:
    rng = random.Random(SEED)
    output.mkdir(parents=True, exist_ok=True)

    with open(output / "products.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["product_id", "product", "category", "list_price", "unit_cost"])
        for p in PRODUCTS:
            w.writerow(p)

    rows = []
    revenue_month_region = {}
    order_seq = 100000
    d = START
    while d <= END:
        orders_per_day = int(rng.gauss(14, 3) * SEASONALITY[d.month])
        if d.month == 11 and 24 <= d.day <= 30:  # Black Friday week
            orders_per_day *= 3
        for _ in range(max(orders_per_day, 1)):
            order_seq += 1
            region = pick(rng, region_weight(d))
            state = rng.choice(REGIONS[region])
            channel = pick(rng, channel_weight(d))
            for _ in range(rng.choices([1, 2, 3], weights=[70, 22, 8])[0]):
                pid, name, cat, price, cost = rng.choices(PRODUCTS, weights=PRODUCT_WEIGHT)[0]
                qty = rng.choices([1, 2, 3], weights=[85, 12, 3])[0]
                discount = rng.choice([0, 0, 0, 5, 10])
                if d.month == 11 and 24 <= d.day <= 30:
                    discount = rng.choice([15, 20, 25])
                revenue = round(qty * price * (1 - discount / 100), 2)

                return_rate = 0.22 if pid == "P005" else 0.04
                draw = rng.random()
                if draw < return_rate:
                    status = "Returned"
                    reason = ("Manufacturing defect" if pid == "P005" and rng.random() < 0.7
                              else rng.choice(RETURN_REASONS))
                elif draw < return_rate + 0.03:
                    status, reason = "Canceled", ""
                else:
                    status, reason = "Delivered", ""

                if status == "Delivered":
                    base = 3.2 if pid == "P005" else 4.4
                    rating = min(5, max(1, round(rng.gauss(base, 0.7))))
                else:
                    rating = ""

                rows.append([
                    f"ORD-{order_seq}", d.isoformat(), region, state, channel, pid, name, cat,
                    qty, f"{price:.2f}", discount, f"{revenue:.2f}", f"{qty * cost:.2f}",
                    status, reason, rating,
                ])
                if status == "Delivered":
                    key = (d.strftime("%Y-%m"), region)
                    revenue_month_region[key] = revenue_month_region.get(key, 0) + revenue
        d += timedelta(days=1)

    with open(output / "sales.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["order_id", "order_date", "region", "state", "channel", "product_id", "product",
                    "category", "quantity", "unit_price", "discount_pct", "revenue",
                    "total_cost", "status", "return_reason", "rating"])
        w.writerows(rows)

    # Targets: based on actuals, with the Northeast starting above (missed in H1)
    # and the other regions with a target slightly above or below actuals.
    with open(output / "targets.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["month", "region", "revenue_target"])
        for (month, region), actual in sorted(revenue_month_region.items()):
            if region == "Northeast":
                factor = 1.15 if month < "2026-05" else 0.92
            else:
                factor = rng.uniform(0.95, 1.08)
            w.writerow([f"{month}-01", region, f"{round(actual * factor, -2):.2f}"])

    print(f"OK: {len(rows)} rows in {output / 'sales.csv'}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(Path(__file__).parent))
    generate(Path(ap.parse_args().output))
