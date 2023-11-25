basket = {
    "Leather wallet": {"quant": 1, "up": 1100},
    "Cigarette": {"quant": 4, "up": 900},
    "Umbrella": {"quant": 12, "up": 200},
    "Haney": {"quant": 28, "up": 100},
}

max_gst_product = None
max_gst_amount = 0

for product, details in basket.items():
    quant = details["quant"]
    up = details["up"]
    gst_amount = 0.18 * (quant * up)  

    if gst_amount > max_gst_amount:
        max_gst_amount = gst_amount
        max_gst_product = product

total_amount = sum(details["quant"] * details["up"] for details in basket.values())

print("Product with maximum GST:", max_gst_product)
print("Maximum GST amount:", max_gst_amount)
print("Total amount to be paid:", total_amount)
