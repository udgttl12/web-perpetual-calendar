from __future__ import annotations

from datetime import datetime

import sxtwl

HEAVENLY_STEMS = "甲乙丙丁戊己庚辛壬癸"
EARTHLY_BRANCHES = "子丑寅卯辰巳午未申酉戌亥"


def pillars_from_datetime(dt: datetime) -> dict[str, str]:
    """Calculate Four Pillars from a timezone-aware datetime."""
    lunar = sxtwl.fromSolar(dt.year, dt.month, dt.day)
    ygz = lunar.getYearGZ()
    mgz = lunar.getMonthGZ()
    dgz = lunar.getDayGZ()
    tgz = sxtwl.getShiGz(dgz.tg, dt.hour)
    return {
        "year": HEAVENLY_STEMS[ygz.tg] + EARTHLY_BRANCHES[ygz.dz],
        "month": HEAVENLY_STEMS[mgz.tg] + EARTHLY_BRANCHES[mgz.dz],
        "day": HEAVENLY_STEMS[dgz.tg] + EARTHLY_BRANCHES[dgz.dz],
        "time": HEAVENLY_STEMS[tgz.tg] + EARTHLY_BRANCHES[tgz.dz],
    }
