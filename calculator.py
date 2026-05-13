def calculate_projection(current_age, retirement_age, current_balance, annual_contribution, growth_rate_pct):
    results = []
    balance = float(current_balance)
    rate = float(growth_rate_pct) / 100

    for age in range(current_age, retirement_age + 1):
        year = age - current_age
        contribution = float(annual_contribution) if age > current_age else 0
        balance = (balance + contribution) * (1 + rate)
        total_contributed = float(current_balance) + (float(annual_contribution) * year)
        growth = balance - total_contributed

        results.append(
            {
                "age": age,
                "year": year,
                "contribution": round(contribution, 2),
                "balance": round(balance, 2),
                "total_contributed": round(total_contributed, 2),
                "growth": round(growth, 2),
            }
        )

    return results


def summarise(results, currency_symbol):
    last = results[-1]
    return {
        "final_balance": last["balance"],
        "total_contributed": last["total_contributed"],
        "total_growth": last["growth"],
        "years_invested": last["year"],
        "currency": currency_symbol,
    }
