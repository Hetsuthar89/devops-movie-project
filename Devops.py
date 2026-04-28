movies = {}

while True:
    print("\n--- Movie Ticket Booking System ---")
    print("1. Add Movie")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. View Movies")
    print("5. Search Movie")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ADD MOVIE
    if choice == "1":
        name = input("Enter movie name: ").strip().lower()
        total_seats = int(input("Enter total seats: "))

        if total_seats <= 0:
            print("Invalid number of seats!")
        else:
            movies[name] = {
                "total": total_seats,
                "available": total_seats
            }
            print(f"Movie '{name}' added with {total_seats} seats!")

    # BOOK TICKET
    elif choice == "2":
        name = input("Enter movie to book: ").strip().lower()

        if name in movies:
            seats = int(input("Enter number of tickets: "))

            if seats <= 0:
                print("Invalid ticket number!")
            elif seats <= movies[name]["available"]:
                movies[name]["available"] -= seats
                print("Ticket booked successfully!")
            else:
                print("Not enough seats available!")
        else:
            print("Movie not found.")

    # CANCEL TICKET
    elif choice == "3":
        name = input("Enter movie to cancel ticket for: ").strip().lower()

        if name in movies:
            seats = int(input("Enter number of tickets to cancel: "))

            if seats <= 0:
                print("Invalid number!")
            else:
                movies[name]["available"] += seats

                # safety check (available > total na thai)
                if movies[name]["available"] > movies[name]["total"]:
                    movies[name]["available"] = movies[name]["total"]

                print("Ticket cancelled successfully!")
        else:
            print("Movie not found.")

    # VIEW MOVIES
    elif choice == "4":
        print("\n--- Current Movies ---")

        if not movies:
            print("No movies available.")
        else:
            for name, data in movies.items():
                print(f"Movie: {name}")
                print(f"Total Seats: {data['total']}")
                print(f"Available Seats: {data['available']}")
                print("-------------------------")

    # SEARCH MOVIE
    elif choice == "5":
        name = input("Search for movie: ").strip().lower()

        if name in movies:
            data = movies[name]
            print(f"Movie Found: {name}")
            print(f"Available Seats: {data['available']}")
        else:
            print("Movie not found.")

    # EXIT
    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice, please try again.")