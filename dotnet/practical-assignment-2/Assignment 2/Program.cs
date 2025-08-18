using System;

namespace Assignment_2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Programs programs = new Programs();
            do
            {
                programs.PrintMenu();
                Console.Write("Enter your choice : ");
                int choice;
                bool validChoice = int.TryParse(Console.ReadLine(), out choice);

                if (!validChoice)
                {
                    Console.WriteLine("Invalid input, please enter a number.");
                    continue;
                }

                switch (choice)
                {
                    case 1:
                        programs.CheckEvenOdd();
                        break;

                    case 2:
                        programs.CheckPositiveOrNegative();
                        break;

                    case 3:
                        programs.FindLargestOfThree();
                        break;

                    case 4:
                        programs.SwapNumbers();
                        break;

                    case 5:
                        programs.SumOfMultiplesOf3And5();
                        break;

                    case 6:
                        programs.SumOfDigits();
                        break;

                    case 7:
                        programs.ReverseAndCheckPalindrome();
                        break;

                    case 8:
                        programs.BasicOperations();
                        break;

                    case 9:
                        programs.ReadGrade();
                        break;

                    case 10:
                        programs.ToggleCase();
                        break;

                    case 11:
                        programs.CheckPerfectNumber();
                        break;

                    case 12:
                        programs.CheckArmstrong();
                        break;

                    case 13:
                        programs.ReverseNumber();
                        break;

                    case 14:
                        programs.ConcatStrings();
                        break;

                    case 15:
                        programs.FindStringLength();
                        break;

                    case 0:
                        Console.WriteLine("Exiting... Goodbye!");
                        return;

                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            } while (true);
        }
    }
}
