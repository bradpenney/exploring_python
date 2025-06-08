# colours = ["red", "green", "blue", "orange"]

# for colour in colours:
#     if colour == "orange":
#         print("Ugh, orange again? Let's pretend we didn't see that.")
#         continue
#     print(f"Ooooh, I totally dig the colour {colour}!")


# balance = 200
# withdrawals = [10, 23, 12, 16, 43, 19, 4, 5]

# for withdrawal in withdrawals:
#     print(f"📤 Request to withdraw ${withdrawal}...")

#     if (balance - withdrawal) < 0:
#         print("🚨 Uh-oh! You're broke. No more money magic today.")
#         break

#     balance -= withdrawal
#     print(f"✅ Success! You withdrew ${withdrawal}. Remaining balance: ${balance}")


balance = 200
withdrawals = [10, 23, 12, 16, 43, 19, 4, 5]

print("💸 Time for a little shopping adventure!")

for withdrawal in withdrawals:
    print(f"🛒 You spot something for ${withdrawal}...")

    if (balance - withdrawal) < 0:
        print("😱 Your wallet gasps in horror — not enough cash!")
        print("💀 The spree ends here, friend.")
        break

    balance -= withdrawal
    print(f"🎉 Purchase successful! You’ve got ${balance} left in your treasure chest.")
else:
    print("🎊 You made it through your spree without going broke!")