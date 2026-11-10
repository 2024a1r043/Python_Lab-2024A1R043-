
from donation import FoodDonation
from rescue_utils import (
    display_donations,
    sort_donations,
    summarize_donations
)


def main():

    donations = []

    print("=" * 50)
    print("FOOD RESCUE SYSTEM - MILESTONE 4")
    print("=" * 50)

    donation_id = 1

    while True:

        donor_name = input("\nEnter donor name (DONE to finish): ")

        if donor_name.strip().upper() == "DONE":
            break

        food_category = input("Enter food category: ").strip().upper()

        try:

            quantity = float(input("Enter quantity (kg): "))
            hours = int(input("Enter remaining hours: "))

            if quantity <= 0 or hours <= 0:
                print("Invalid values! Enter positive numbers.")
                continue

            donation = FoodDonation(
                donation_id,
                donor_name.strip().title(),
                food_category,
                quantity,
                hours
            )

            donations.append(donation)

            print("\nDonation Accepted!")
            print(donation)

            donation_id += 1

        except ValueError:
            print("Invalid input! Enter numeric values.")

    if donations:

        display_donations(donations)

        sorted_list = sort_donations(donations)

        print("\n========== SORTED DONATIONS ==========")
        display_donations(sorted_list)

        summarize_donations(donations)

    else:
        print("\nNo donations recorded.")

    print("\nThank you for using Food Rescue System!")


if __name__ == "__main__":
    main()
