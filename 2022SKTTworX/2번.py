from enum import Enum


class Payment(Enum):
    OVER90 = 1
    OVER60 = 2
    OVER48 = 3
    OVER36 = 4
    DEFAULT = 0


class Period(Enum):
    OVER5 = 1
    OVER2 = 2
    DEFAULT = 0


def solution(periods, payments, estimates):
    def determine_period(period):
        if period < 24:
            return Period.DEFAULT
        elif period < 60:
            return Period.OVER2
        elif period >= 60:
            return Period.OVER5

    def determine_payment(annual_payment):
        if annual_payment < 360000:
            return Payment.DEFAULT
        elif annual_payment < 480000:
            return Payment.OVER36
        elif annual_payment < 600000:
            return Payment.OVER48
        elif annual_payment < 900000:
            return Payment.OVER60
        elif annual_payment >= 900000:
            return Payment.OVER90

    def grade_decision(period_category: Period, payment_category: Payment):
        decision_dict = {
            Payment.OVER90: {
                Period.DEFAULT: "GOLD",
                Period.OVER2: "VIP",
                Period.OVER5: "VIP",
            },
            Payment.OVER60: {
                Period.DEFAULT: "GOLD",
                Period.OVER2: "GOLD",
                Period.OVER5: "VIP",
            },
            Payment.OVER48: {
                Period.DEFAULT: "SILVER",
                Period.OVER2: "GOLD",
                Period.OVER5: "GOLD",
            },
            Payment.OVER36: {
                Period.DEFAULT: "SILVER",
                Period.OVER2: "SILVER",
                Period.OVER5: "GOLD",
            },
            Payment.DEFAULT: {
                Period.DEFAULT: "SILVER",
                Period.OVER2: "SILVER",
                Period.OVER5: "SILVER",
            },
        }
        return decision_dict[payment_category][period_category]

    rise_n = 0
    fall_n = 0

    for period, payment, estimate in zip(periods, payments, estimates):
        # current grade
        period_category = determine_period(period)
        payment_category = determine_payment(sum(payment))
        current_grade = grade_decision(period_category, payment_category)

        # next grade
        period_category = determine_period(period + 1)
        payment_category = determine_payment(sum(payment[1:], estimate))
        next_grade = grade_decision(period_category, payment_category)

        if current_grade != "VIP" and next_grade == "VIP":
            rise_n += 1
        elif current_grade == "VIP" and next_grade != "VIP":
            fall_n += 1

    return [rise_n, fall_n]
