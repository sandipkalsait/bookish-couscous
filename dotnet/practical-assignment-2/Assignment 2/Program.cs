using System;

namespace Assignment_2
{
    // Custom delegate
    internal delegate void FunctionDelegate();

    internal class Program
    {
        static void Main(string[] args)
        {
            Programs programs = new Programs();
            int choice;

            do
            {
                programs.PrintMenu();
                Console.Write("Enter your choice : ");
                bool validChoice = int.TryParse(Console.ReadLine(), out choice);

                if (!validChoice)
                {
                    Console.WriteLine("Invalid input, please enter a number.");
                    continue;
                }

                // Direct function calls
                switch (choice)
                {
                    case 1: programs.CheckEvenOdd(); break;
                    case 2: programs.CheckPositiveOrNegative(); break;
                    case 3: programs.FindLargestOfThree(); break;
                    case 4: programs.SwapNumbers(); break;
                    case 5: programs.SumOfMultiplesOf3And5(); break;
                    case 6: programs.SumOfDigits(); break;

                    // Delegate-based calls (Custom delegate)
                    case 7:
                        FunctionDelegate fd1 = programs.ReverseAndCheckPalindrome;
                        fd1();
                        break;

                    case 8:
                        FunctionDelegate fd2 = programs.BasicOperations;
                        fd2();
                        break;

                    // Using built-in delegates
                    case 9:
                        Action readGrade = programs.ReadGrade;
                        readGrade();
                        break;

                    case 10:
                        Action toggleCase = programs.ToggleCase;
                        toggleCase();
                        break;

                    case 11:
                        Func<int, bool> isPerfect = programs.CheckPerfectNumber;
                        Console.Write("Enter number: ");
                        int n1 = int.Parse(Console.ReadLine());
                        Console.WriteLine(isPerfect(n1) ? "Perfect" : "Not Perfect");
                        break;

                    case 12:
                        Predicate<int> isArmstrong = programs.CheckArmstrong;
                        Console.Write("Enter number: ");
                        int n2 = int.Parse(Console.ReadLine());
                        Console.WriteLine(isArmstrong(n2) ? "Armstrong" : "Not Armstrong");
                        break;

                    case 13:
                        Func<int, int> reverse = programs.ReverseNumber;
                        Console.Write("Enter number: ");
                        int num = int.Parse(Console.ReadLine());
                        Console.WriteLine("Reversed: " + reverse(num));
                        break;

                    case 14:
                        Func<string, string, string> concat = programs.ConcatStrings;
                        Console.Write("Enter first string: ");
                        string s1 = Console.ReadLine();
                        Console.Write("Enter second string: ");
                        string s2 = Console.ReadLine();
                        Console.WriteLine("Concatenated: " + concat(s1, s2));
                        break;

                    case 15:
                        Func<string, int> strlen = programs.FindStringLength;
                        Console.Write("Enter string: ");
                        string input = Console.ReadLine();
                        Console.WriteLine("Length: " + strlen(input));
                        break;

                    case 0:
                        Console.WriteLine("Exiting... Goodbye!");
                        return;

                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }

                Console.WriteLine("\nPress Enter to continue...");
                Console.ReadLine();

            } while (true);
        }
    }
}
