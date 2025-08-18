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
            Console.WriteLine("7. Check whether number is Positive or Negative");
            Console.WriteLine("8. Sum of numbers divisible by 3 and 5 in a range");
            Console.WriteLine("9. Find sum of digits of a number");
            Console.WriteLine("10. Reverse number and check if it is palindrome");
            Console.WriteLine("11. Read grade and display description");
            Console.WriteLine("12. Convert character into lower/upper case");
            Console.WriteLine("13. Check whether number is Perfect Number");
            Console.WriteLine("14. Check whether number is Armstrong Number");
            Console.WriteLine("15. Find length of a string");
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

       
        internal void CheckPositiveOrNegative()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());

            if (num > 0)
                Console.WriteLine($"{num} is Positive.");
            else if (num < 0)
                Console.WriteLine($"{num} is Negative.");
            else
                Console.WriteLine("Number is Zero.");
        }

        internal void SumOfMultiplesOf3And5()
        {
            Console.Write("Enter range (start): ");
            int start = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter range (end): ");
            int end = Convert.ToInt32(Console.ReadLine());

            int sum = 0;
            for (int i = start; i <= end; i++)
            {
                if (i % 3 == 0 || i % 5 == 0)
                    sum += i;
            }

            Console.WriteLine($"Sum of numbers divisible by 3 or 5 = {sum}");
        }

        internal void SumOfDigits()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());

            int sum = 0, temp = num;

            while (temp > 0)
            {
                sum += temp % 10;
                temp /= 10;
            }

            Console.WriteLine($"Sum of digits of {num} = {sum}");
        }

        internal void ReverseAndCheckPalindrome()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());

            int original = num, rev = 0;

            while (num > 0)
            {
                rev = rev * 10 + num % 10;
                num /= 10;
            }

            Console.WriteLine($"Reversed Number = {rev}");

            if (original == rev)
                Console.WriteLine("It is a Palindrome.");
            else
                Console.WriteLine("It is NOT a Palindrome.");
        }

        internal void ReadGrade()
        {
            Console.Write("Enter Grade (A/B/C/D/F): ");
            char grade = Char.ToUpper(Console.ReadKey().KeyChar);
            Console.WriteLine();

            switch (grade)
            {
                case 'A': Console.WriteLine("Excellent"); break;
                case 'B': Console.WriteLine("Good"); break;
                case 'C': Console.WriteLine("Average"); break;
                case 'D': Console.WriteLine("Poor"); break;
                case 'F': Console.WriteLine("Fail"); break;
                default: Console.WriteLine("Invalid Grade"); break;
            }
        }

        internal void ToggleCase()
        {
            Console.Write("Enter a character: ");
            char ch = Console.ReadKey().KeyChar;
            Console.WriteLine();

            if (Char.IsUpper(ch))
                Console.WriteLine($"Lowercase: {Char.ToLower(ch)}");
            else if (Char.IsLower(ch))
                Console.WriteLine($"Uppercase: {Char.ToUpper(ch)}");
            else
                Console.WriteLine("Not an alphabet character.");
        }

        internal void CheckPerfectNumber()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());

            int sum = 0;
            for (int i = 1; i <= num / 2; i++)
            {
                if (num % i == 0)
                    sum += i;
            }

            if (sum == num && num != 0)
                Console.WriteLine($"{num} is a Perfect Number.");
            else
                Console.WriteLine($"{num} is NOT a Perfect Number.");
        }

        internal void CheckArmstrong()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());

            int original = num, sum = 0;
            int digits = num.ToString().Length;

            while (num > 0)
            {
                int digit = num % 10;
                sum += (int)Math.Pow(digit, digits);
                num /= 10;
            }

            if (sum == original)
                Console.WriteLine($"{original} is an Armstrong Number.");
            else
                Console.WriteLine($"{original} is NOT an Armstrong Number.");
        }

        internal void FindStringLength()
        {
            Console.Write("Enter a string: ");
            string str = Console.ReadLine();

            Console.WriteLine($"Length of the string = {str.Length}");
        }
    }
}
