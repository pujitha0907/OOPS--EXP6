##SmartDeviceStore

code:
import java.util.Scanner;
abstract class Device {
    int deviceId;
    String brand;
    double price;
    Device(int deviceId, String brand, double price) {
        this.deviceId = deviceId;
        this.brand = brand;
        this.price = price;
    }
    abstract void displayDetails();
}
interface Discountable {
    void applyDiscount(double percentage);
}
class Smartphone extends Device implements Discountable {
    double discountedPrice;
    Smartphone(int deviceId, String brand, double price) {
        super(deviceId, brand, price);
        discountedPrice = price; 
    }
    public void displayDetails() {
        System.out.println("ID: " + deviceId +
                           ", Brand: " + brand +
                           ", Original Price: " + price +
                           ", Final Price: " + discountedPrice);
    }
    public void applyDiscount(double percentage) {
        discountedPrice = price - (price * percentage / 100);
    }
}
public class SmartDeviceStore {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Smartphone phone = null;
        int choice;
        System.out.println("URK24CS6006 - PUJITHA\n");
        do {
            System.out.println("___Menu___");
            System.out.println("1. Add Smartphone");
            System.out.println("2. Apply Discount");
            System.out.println("3. View Details");
            System.out.println("4. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter ID: ");
                    int id = sc.nextInt();
                    sc.nextLine(); 
                    System.out.print("Enter Brand: ");
                    String brand = sc.nextLine();
                    System.out.print("Enter Price: ");
                    double price = sc.nextDouble();
                    phone = new Smartphone(id, brand, price);
                    System.out.println("Smartphone added!");
                    break;
                case 2:
                    if (phone == null) {
                        System.out.println("Add a smartphone first!");
                    } else {
                        System.out.print("Enter discount %: ");
                        double d = sc.nextDouble();
                        phone.applyDiscount(d);
                        System.out.println("Discount applied!");
                    }
                    break;
                case 3:
                    if (phone == null) {
                        System.out.println("Add a smartphone first!");
                    } else {
                        phone.displayDetails();
                    }
                    break;
                case 4:
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("Invalid choice!");
            }
        } while (choice != 4);
        sc.close();
    }
}

