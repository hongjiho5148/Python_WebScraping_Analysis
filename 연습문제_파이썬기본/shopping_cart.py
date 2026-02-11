cart = {
    "사과": {"개수": 2, "가격": 1000},
    "바나나": {"개수": 3, "가격": 800},
    "오렌지": {"개수": 1, "가격": 1500}
}

total_price = 0

print("쇼핑 카트:")
for item, info in cart.items():
    subtotal = info["개수"] * info["가격"]
    total_price += subtotal
    print(f"{item}: {info['개수']}개 (개당 {info['가격']}원) = {subtotal}원")

print(f"총 가격: {total_price}원")