import qrcode
import os

def generate_qr():
    print("\n" + "=" * 30)
    print("QR Code Generator")
    print("=" * 30)

    while True:
        url = input("Enter website URL: ").strip()

        if url != "":
            break

        print("Please enter a valid URL.")

    folder = "QR_Codes"
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, "my_website_qr.png")

    print("\nGenerating QR Code...")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)

    print("\nQR Code created successfully!")
    print("Saved at:", path)


def main():
    print("Welcome to QR Code Generator")

    while True:
        print("\n1. Generate QR Code")
        print("2. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_qr()

        elif choice == "2":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()