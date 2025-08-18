using System;

namespace Assignment_2
{
    internal class Programs
    {
        internal void PrintMenu()
        {
            Console.WriteLine("------------------ Assignment 2 Menu -------------------");
            Console.WriteLine("Using Functions:");
            Console.WriteLine("1. Check Whether a Given Number is Even or Odd");
            Console.WriteLine("2. Check Whether a Number is Positive or Not");
            Console.WriteLine("3. Find the Largest of Three Numbers");
            Console.WriteLine("4. Swap Two Numbers");
            Console.WriteLine("5. Find the Sum of All the Multiples of 3 and 5");
            Console.WriteLine("6. Find Sum of Digits of a Number");
            Console.WriteLine("\nUsing Delegates:");
            Console.WriteLine("7. Reverse a Number and Check if it is a Palindrome");
            Console.WriteLine("8. Calculate Sum, Multiplication, Division and Subtraction of Two Numbers");
            Console.WriteLine("9. Read a Grade and Display the Equivalent Description");
            Console.WriteLine("10. Convert Lowercase Characters by Uppercase and Vice-Versa");
            Console.WriteLine("11. Check Whether a Given Number is Perfect Number");
            Console.WriteLine("12. Check Armstrong Number");
            Console.WriteLine("13. Reverse a Number");
            Console.WriteLine("14. Concatenate Two Strings");
            Console.WriteLine("15. Find the Length of a String");
            Console.WriteLine("0. Exit");
            Console.WriteLine("--------------------------------------------------------");
        }

        internal void CheckEvenOdd()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(num % 2 == 0 ? $"{num} is Even" : $"{num} is Odd");
        }

        internal void CheckPositiveOrNegative()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            if (num > 0)
                Console.WriteLine("Number is Positive.");
            else if (num < 0)
                Console.WriteLine("Number is Negative.");
            else
                Console.WriteLine("Number is Zero.");
        }

        internal void FindLargestOfThree()
        {
            Console.Write("Enter first number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter second number: ");
            int b = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter third number: ");
            int c = Convert.ToInt32(Console.ReadLine());
            int largest = (a >= b && a >= c) ? a : (b >= c ? b : c);
            Console.WriteLine("Largest number is: " + largest);
        }

        internal void SwapNumbers()
        {
            Console.Write("Enter first number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter second number: ");
            int b = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine($"Before Swap: a={a}, b={b}");
            int temp = a; a = b; b = temp;
            Console.WriteLine($"After Swap: a={a}, b={b}");
        }

        internal void SumOfMultiplesOf3And5()
        {
            Console.Write("Enter a limit: ");
            int limit = Convert.ToInt32(Console.ReadLine());
            int sum = 0;
            for (int i = 1; i <= limit; i++)
                if (i % 3 == 0 || i % 5 == 0) sum += i;
            Console.WriteLine($"Sum of multiples of 3 or 5 up to {limit} is {sum}");
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
            Console.WriteLine($"Sum of digits of {num} is {sum}");
        }

        internal void ReverseAndCheckPalindrome()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            int reversed = 0, temp = num;
            while (temp > 0)
            {
                reversed = reversed * 10 + temp % 10;
                temp /= 10;
            }
            Console.WriteLine($"Reversed number: {reversed}");
            Console.WriteLine(num == reversed ? "It is a Palindrome." : "It is NOT a Palindrome.");
        }

        internal void BasicOperations()
        {
            Console.Write("Enter first number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter second number: ");
            int b = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine($"Sum = {a + b}");
            Console.WriteLine($"Difference = {a - b}");
            Console.WriteLine($"Multiplication = {a * b}");
            Console.WriteLine(b != 0 ? $"Division = {(double)a / b}" : "Division not possible (divide by zero).");
        }

        internal void ReadGrade()
        {
            Console.Write("Enter grade (A/B/C/D/F): ");
            char grade = Char.ToUpper(Console.ReadKey().KeyChar);
            Console.WriteLine();
            switch (grade)
            {
                case 'A': Console.WriteLine("Excellent"); break;
                case 'B': Console.WriteLine("Good"); break;
                case 'C': Console.WriteLine("Average"); break;
                case 'D': Console.WriteLine("Poor"); break;
                case 'F': Console.WriteLine("Fail"); break;
                default: Console.WriteLine("Invalid grade"); break;
            }
        }

        internal void ToggleCase()
        {
            Console.Write("Enter a string: ");
            string input = Console.ReadLine();
            char[] chars = input.ToCharArray();
            for (int i = 0; i < chars.Length; i++)
                chars[i] = Char.IsUpper(chars[i]) ? Char.ToLower(chars[i]) : Char.ToUpper(chars[i]);
            Console.WriteLine("Toggled string: " + new string(chars));
        }

        internal void CheckPerfectNumber()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            int sum = 0;
            for (int i = 1; i <= num / 2; i++)
                if (num % i == 0) sum += i;
            Console.WriteLine(sum == num ? "It is a Perfect number." : "It is NOT a Perfect number.");
        }

        internal void CheckArmstrong()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            int sum = 0, temp = num, digits = num.ToString().Length;
            while (temp > 0)
            {
                int d = temp % 10;
                sum += (int)Math.Pow(d, digits);
                temp /= 10;
            }
            Console.WriteLine(sum == num ? "It is an Armstrong number." : "It is NOT an Armstrong number.");
        }

        internal void ReverseNumber()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            int reversed = 0;
            while (num > 0)
            {
                reversed = reversed * 10 + num % 10;
                num /= 10;
            }
            Console.WriteLine($"Reversed number is: {reversed}");
        }

        internal void ConcatStrings()
        {
            Console.Write("Enter first string: ");
            string str1 = Console.ReadLine();
            Console.Write("Enter second string: ");
            string str2 = Console.ReadLine();
            Console.WriteLine("Concatenated String: " + str1 + " " + str2);
        }

        internal void FindStringLength()
        {
            Console.Write("Enter a string: ");
            string str = Console.ReadLine();
            Console.WriteLine("Length of string: " + str.Length);
        }
    }
}
