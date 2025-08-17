using System;

namespace Assignment_1
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
                        programs.CheckElectionEligibility();
                        break;

                    case 2:
                        programs.CheckEvenOdd();
                        break;

                    case 3:
                        programs.SwapNumbers();
                        break;

                    case 4:
                        programs.ConcatStrings();
                        break;

                    case 5:
                        programs.FindLargestOfThree();
                        break;

                    case 6:
                        programs.BasicOperations();
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
