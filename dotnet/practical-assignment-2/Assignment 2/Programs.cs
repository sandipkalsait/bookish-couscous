using System;

namespace Assignment_2
{
    // Declare delegate
    internal delegate void FunctionDelegate();

    internal class Programs
    {
        internal void PrintMenu()
        {
            Console.WriteLine("\n------------------ Assignment 2 Menu -------------------");
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
            int original = num, rev = 0;
            while (num > 0)
            {
                rev = rev * 10 + num % 10;
                num /= 10;
            }
            Console.WriteLine($"Reversed: {rev}");
            Console.WriteLine(rev == original ? "Palindrome" : "Not Palindrome");
        }

        internal void BasicOperations()
        {
            Console.Write("Enter first number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter second number: ");
            int b = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine($"Sum = {a + b}");
            Console.WriteLine($"Subtraction = {a - b}");
            Console.WriteLine($"Multiplication = {a * b}");
            if (b != 0)
                Console.WriteLine($"Division = {(double)a / b}");
            else
                Console.WriteLine("Division not possible (denominator = 0)");
        }

        internal void ReadGrade()
        {
            Console.Write("Enter grade (A/B/C/D/F): ");
            char grade = Char.ToUpper(Convert.ToChar(Console.ReadLine()));

            switch (grade)
            {
                case 'A': Console.WriteLine("Excellent"); break;
                case 'B': Console.WriteLine("Good"); break;
                case 'C': Console.WriteLine("Average"); break;
                case 'D': Console.WriteLine("Below Average"); break;
                case 'F': Console.WriteLine("Fail"); break;
                default: Console.WriteLine("Invalid Grade"); break;
            }
        }

        internal void ToggleCase()
        {
            Console.Write("Enter a string: ");
            string input = Console.ReadLine();
            char[] chars = input.ToCharArray();
            for (int i = 0; i < chars.Length; i++)
            {
                if (Char.IsLower(chars[i])) chars[i] = Char.ToUpper(chars[i]);
                else if (Char.IsUpper(chars[i])) chars[i] = Char.ToLower(chars[i]);
            }
            Console.WriteLine("Toggled string: " + new string(chars));
        }

        internal void CheckPerfectNumber()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            int sum = 0;
            for (int i = 1; i <= num / 2; i++)
                if (num % i == 0) sum += i;
            Console.WriteLine(sum == num ? "Perfect Number" : "Not Perfect Number");
        }

        internal void CheckArmstrong()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            int original = num, sum = 0, digits = num.ToString().Length;

            while (num > 0)
            {
                int d = num % 10;
                sum += (int)Math.Pow(d, digits);
                num /= 10;
            }
            Console.WriteLine(sum == original ? "Armstrong Number" : "Not Armstrong Number");
        }

        internal void ReverseNumber()
        {
            Console.Write("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            int rev = 0;
            while (num > 0)
            {
                rev = rev * 10 + num % 10;
                num /= 10;
            }
            Console.WriteLine($"Reversed number: {rev}");
        }

        internal void ConcatStrings()
        {
            Console.Write("Enter first string: ");
            string s1 = Console.ReadLine();
            Console.Write("Enter second string: ");
            string s2 = Console.ReadLine();
            Console.WriteLine("Concatenated: " + s1 + s2);
        }

        internal void FindStringLength()
        {
            Console.Write("Enter a string: ");
            string s = Console.ReadLine();
            Console.WriteLine("Length: " + s.Length);
        }
    }
}
