import java.util.Scanner;

public class task1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Temperature Conversion Program");
        System.out.print("Enter temperature value: ");
        double temperature = scanner.nextDouble();

        System.out.println("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ");
        char unit = scanner.next().charAt(0);

        switch (Character.toUpperCase(unit)) {
            case 'C':
                convertFromCelsius(temperature);
                break;
            case 'F':
                convertFromFahrenheit(temperature);
                break;
            case 'K':
                convertFromKelvin(temperature);
                break;
            default:
                System.out.println("Invalid unit. Please enter C, F, or K.");
        }

        scanner.close();
    }

    public static void convertFromCelsius(double celsius) {
        double fahrenheit = celsiusToFahrenheit(celsius);
        double kelvin = celsiusToKelvin(celsius);
        System.out.println("Temperature in Celsius: " + celsius);
        System.out.println("Temperature in Fahrenheit: " + fahrenheit);
        System.out.println("Temperature in Kelvin: " + kelvin);
    }

    public static void convertFromFahrenheit(double fahrenheit) {
        double celsius = fahrenheitToCelsius(fahrenheit);
        double kelvin = fahrenheitToKelvin(fahrenheit);
        System.out.println("Temperature in Fahrenheit: " + fahrenheit);
        System.out.println("Temperature in Celsius: " + celsius);
        System.out.println("Temperature in Kelvin: " + kelvin);
    }

    public static void convertFromKelvin(double kelvin) {
        double celsius = kelvinToCelsius(kelvin);
        double fahrenheit = kelvinToFahrenheit(kelvin);
        System.out.println("Temperature in Kelvin: " + kelvin);
        System.out.println("Temperature in Celsius: " + celsius);
        System.out.println("Temperature in Fahrenheit: " + fahrenheit);
    }

    public static double celsiusToFahrenheit(double celsius) {
        return (celsius * 9/5) + 32;
    }

    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5/9;
    }

    public static double celsiusToKelvin(double celsius) {
        return celsius + 273.15;
    }

    public static double kelvinToCelsius(double kelvin) {
        return kelvin - 273.15;
    }

    public static double fahrenheitToKelvin(double fahrenheit) {
        return (fahrenheit - 32) * 5/9 + 273.15;
    }

    public static double kelvinToFahrenheit(double kelvin) {
        return (kelvin - 273.15) * 9/5 + 32;
    }
}

