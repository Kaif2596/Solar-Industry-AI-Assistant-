def recommend_panels(usable_area_sq_m):
    PANEL_AREA = 1.6  # m²
    PANEL_WATT = 320  # W

    panel_count = int(usable_area_sq_m // PANEL_AREA)
    total_capacity_kw = round((panel_count * PANEL_WATT) / 1000, 2)
    covered_area = panel_count * PANEL_AREA
    coverage_percent = round((covered_area / usable_area_sq_m) * 100, 2)

    return {
        "panel_type": f"{PANEL_WATT}W Monocrystalline",
        "panel_count": panel_count,
        "total_capacity_kw": total_capacity_kw,
        "panel_coverage_percent": coverage_percent
    }

def estimate_cost_and_roi(panel_count):
    COST_PER_WATT = 50  # INR
    PANEL_WATT = 320
    ELECTRICITY_COST = 8  # INR per kWh
    SUN_HOURS_PER_DAY = 5
    GOV_SUBSIDY = 0.30

    total_watt = panel_count * PANEL_WATT
    total_cost = total_watt * COST_PER_WATT

    subsidy_amount = int(total_cost * GOV_SUBSIDY)
    final_cost = int(total_cost - subsidy_amount)

    yearly_generation_kwh = (total_watt / 1000) * SUN_HOURS_PER_DAY * 365
    yearly_savings = int(yearly_generation_kwh * ELECTRICITY_COST)

    payback_period = round(final_cost / yearly_savings, 2)

    return {
        "estimated_cost_inr": int(total_cost),
        "gov_subsidy_inr": subsidy_amount,
        "final_cost_inr": final_cost,
        "estimated_yearly_savings_inr": yearly_savings,
        "payback_period_years": payback_period
    }

def analyze_solar_potential(area_m2):
    panel_data = recommend_panels(area_m2)
    roi_data = estimate_cost_and_roi(panel_data["panel_count"])

    panel_coverage = round((panel_data["panel_count"] * 1.6) / area_m2 * 100, 2)

    return {**panel_data, **roi_data}
