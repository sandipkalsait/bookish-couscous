using System;

namespace Assignment_2
{
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

                    // Delegate-based calls
                    case 7: new FunctionDelegate(programs.ReverseAndCheckPalindrome)(); break;
                    case 8: new FunctionDelegate(programs.BasicOperations)(); break;
                    case 9: new FunctionDelegate(programs.ReadGrade)(); break;
                    case 10: new FunctionDelegate(programs.ToggleCase)(); break;
                    case 11: new FunctionDelegate(programs.CheckPerfectNumber)(); break;
                    case 12: new FunctionDelegate(programs.CheckArmstrong)(); break;
                    case 13: new FunctionDelegate(programs.ReverseNumber)(); break;
                    case 14: new FunctionDelegate(programs.ConcatStrings)(); break;
                    case 15: new FunctionDelegate(programs.FindStringLength)(); break;

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
