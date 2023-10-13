def calculate_charge(pages):
    if pages <= 100:
        charge = pages * 0.03
    elif pages <= 300:
        charge = 100 * 0.03 + (pages - 100) * 0.02
    else:
        charge = 100 * 0.03 + 200 * 0.02 + (pages - 300) * 0.01
    return charge

def calculate_gst(amount):
    gst = amount * 0.07
    return gst

print("Pages\tCharge(s)\tInclude GST($)")
for pages in range(0, 501, 50):
    charge = calculate_charge(pages)
    gst = calculate_gst(charge)
    total_charge = charge + gst
    print(f"{pages}\t{charge:.2f}\t\t{total_charge:.2f}")
