using System;

namespace Assignment_1
{
    internal class Programs
    {
        internal void PrintMenu()
        {
            Console.WriteLine("------------------ Assignment 1 Menu -------------------");
            Console.WriteLine("1. Check if age is valid for election in India");
            Console.WriteLine("2. Check whether a number is even or odd");
            Console.WriteLine("3. Swap two numbers");
            Console.WriteLine("4. Concatenate two strings");
            Console.WriteLine("5. Find the largest number among 3 numbers");
            Console.WriteLine("6. Perform Sum, Subtraction, Multiplication, Division");
            Console.WriteLine("0. Exit");
            Console.WriteLine("--------------------------------------------------------");
        }

        internal void CheckElectionEligibility()
        {
            Console.Write("Enter your age: ");
            int age = Convert.ToInt32(Console.ReadLine());

            if (age >= 18)
                Console.WriteLine("You are eligible to vote in India.");
            else
                Console.WriteLine("You are NOT eligible to vote in India.");
        }

        internal void CheckEvenOdd()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());

            if (num % 2 == 0)
                Console.WriteLine($"{num} is Even");
            else
                Console.WriteLine($"{num} is Odd");
        }

        internal void SwapNumbers()
        {
            Console.Write("Enter first number: ");
            int a = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter second number: ");
            int b = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine($"Before Swap: a={a}, b={b}");

            int temp = a;
            a = b;
            b = temp;

            Console.WriteLine($"After Swap: a={a}, b={b}");
        }

        internal void ConcatStrings()
        {
            Console.Write("Enter first string: ");
            string str1 = Console.ReadLine();

            Console.Write("Enter second string: ");
            string str2 = Console.ReadLine();

            string result = str1 + " " + str2;
            Console.WriteLine("Concatenated String: " + result);
        }

        internal void FindLargestOfThree()
        {
            Console.Write("Enter first number: ");
            int a = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter second number: ");
            int b = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter third number: ");
            int c = Convert.ToInt32(Console.ReadLine());

            int largest;

            if (a >= b && a >= c)
                largest = a;
            else if (b >= a && b >= c)
                largest = b;
            else
                largest = c;

            Console.WriteLine("Largest number is: " + largest);
        }

        internal void BasicOperations()
        {
            int choice;
            do
            {
                Console.WriteLine("\n--- Arithmetic Operations Menu ---");
                Console.WriteLine("1. Addition");
                Console.WriteLine("2. Subtraction");
                Console.WriteLine("3. Multiplication");
                Console.WriteLine("4. Division");
                Console.WriteLine("0. Back to Main Menu");
                Console.Write("Enter your choice: ");
                choice = Convert.ToInt32(Console.ReadLine());

                if (choice == 0) break;

                Console.Write("Enter first number: ");
                int a = Convert.ToInt32(Console.ReadLine());

                Console.Write("Enter second number: ");
                int b = Convert.ToInt32(Console.ReadLine());

                switch (choice)
                {
                    case 1:
                        Console.WriteLine($"Sum = {a + b}");
                        break;
                    case 2:
                        Console.WriteLine($"Difference = {a - b}");
                        break;
                    case 3:
                        Console.WriteLine($"Multiplication = {a * b}");
                        break;
                    case 4:
                        if (b != 0)
                            Console.WriteLine($"Division = {(double)a / b}");
                        else
                            Console.WriteLine("Division not possible (divide by zero).");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Try again.");
                        break;
                }

            } while (choice != 0);
        }
    }
}
