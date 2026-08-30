# Cinema Ticket Pre-Sale Program
# This program sells up to 20 cinema tickets.
# Each buyer can purchase a maximum of 4 tickets.


# This function asks a buyer how many tickets they want.
def get_tickets(remaining_tickets):
    tickets = int(input("How many tickets would you like to buy? "))

    # Make sure the buyer chooses between 1 and 4 tickets.
    if tickets < 1 or tickets > 4:
        print("You can only buy 1 to 4 tickets.")
        return 0

    # Make sure enough tickets are still available.
    if tickets > remaining_tickets:
        print("There are only", remaining_tickets, "tickets remaining.")
        return 0

    return tickets


# Main function controls the ticket sales.
def main():
    total_tickets = 20
    tickets_sold = 0
    buyers = 0

    # Continue selling tickets until all 20 are sold.
    while tickets_sold < total_tickets:
        remaining_tickets = total_tickets - tickets_sold

        print()
        print("Tickets remaining:", remaining_tickets)

        tickets = get_tickets(remaining_tickets)

        # Only count the purchase if the number is valid.
        if tickets > 0:
            tickets_sold = tickets_sold + tickets
            buyers = buyers + 1

            remaining_tickets = total_tickets - tickets_sold
            print("Tickets remaining after purchase:", remaining_tickets)

    # Display the final number of buyers.
    print()
    print("All tickets have been sold.")
    print("Total number of buyers:", buyers)


# Start the program.
main()
