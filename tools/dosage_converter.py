#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中医古方度量衡古今折算参考工具（符合 L1-tcm 学术规范）
用法：python tools/dosage_converter.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# 历代汉制古方剂量与现代公制克数折算标准
CONVERSION_STANDARDS = {
    "archaeological_han": {
        "name": "考古实测汉制标准（柯雪帆/国家药监标准）",
        "description": "基于汉代度量衡出土文物实测考证：东汉 1 斤 ≈ 250g，1 斤 = 16 两",
        "liang_to_gram": 15.625,  # 1 两 ≈ 15.625g
        "zhu_to_gram": 0.651,     # 1 铢 = 1/24 两 ≈ 0.65g
    },
    "traditional_clinical": {
        "name": "近现代临床常规经验折算（折半/三分法）",
        "description": "临床安全折算习惯：汉代 1 两通常按现代 3g ~ 5g 折算",
        "liang_to_gram": 3.0,
        "zhu_to_gram": 0.125,
    },
    "ming_qing": {
        "name": "明清市制标准（李时珍/清代官秤）",
        "description": "明清 1 斤 ≈ 596.8g，1 斤 = 16 两，1 两 = 10 钱",
        "liang_to_gram": 37.3,
        "qian_to_gram": 3.73,
    }
}


def convert_han_dosage(liang: float = 0.0, zhu: float = 0.0) -> dict:
    """计算汉代方剂（如《伤寒论》《金匮要略》）中两/铢在不同考据标准下的现代克数"""
    results = {}
    for key, std in CONVERSION_STANDARDS.items():
        if "liang_to_gram" in std:
            gram_total = liang * std["liang_to_gram"] + zhu * std.get("zhu_to_gram", 0.0)
            results[key] = {
                "standard": std["name"],
                "grams": round(gram_total, 2),
                "desc": std["description"]
            }
    return results


if __name__ == "__main__":
    print("=" * 72)
    print("🌿 中医经方度量衡古今折算参考（以桂枝汤为例：桂枝三两、白芍三两、炙甘草二两）")
    print("=" * 72)

    sample_items = [("桂枝", 3.0), ("白芍", 3.0), ("炙甘草", 2.0)]
    for herb, liang in sample_items:
        print(f"\n【{herb}】 古制：{liang} 两")
        res = convert_han_dosage(liang=liang)
        for _, item in res.items():
            print(f"  • {item['standard']}：{item['grams']} g")

    print("\n" + "=" * 72)
    print("⚠️ 提示：上述折算仅供中医学术文献研读与古方用量考据参考，严禁作为临床直接配伍凭据。")
    print("=" * 72)
