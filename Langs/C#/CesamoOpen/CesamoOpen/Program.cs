// See https://aka.ms/new-console-template for more information
using System.Diagnostics.Metrics;
using System.Runtime.InteropServices;

Dictionary <char,List<double>> hist = new Dictionary<char, List<double>>();

void MainMenu()
{
    Logo();
    Console.WriteLine("Type 1 to do some calc operation");
    Console.WriteLine("Type 2 to see some of the last results");
    Console.WriteLine("Type 3 to know more about our world");
    Console.WriteLine("Type 0 to exit");
    int opt = int.Parse(Console.ReadLine());
    
    switch (opt)
    {
        case 1:
            CalcOperation();
            break;
        case 2:
            ShowHist();
            break;
        case 3:
            Console.WriteLine("Working on It");
            break;
        case 0:
            Console.WriteLine("Bye\nHope see you soon!");
            break;
        default:
            Console.WriteLine("We haven't this option.\nTry again!");
            MainMenu();
            break;
    }
}

MainMenu();

void Logo()
{
    Console.WriteLine(@"
    █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
    █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄

    ");

    Console.WriteLine("Welcome to my C# Calculator");
}

void CalcOperation()
{
    Console.Clear();
    Console.WriteLine("Welcome to the Calc Environment");
    Console.WriteLine("\nANY KEY to return to the Main Menu or ENTER to continue\n");
    ConsoleKeyInfo opt = Console.ReadKey(true);
    ConsoleKeyInfo stopOpt;
    if (opt.Key == ConsoleKey.Enter)
    {
        do
        {
            Console.WriteLine("Write your operation type below!");
            char operationOpt = char.Parse(Console.ReadLine());

            Console.WriteLine("Type the numbers of your operation separated by a space ");
            string[] numbers = Console.ReadLine().Split(" ");

            double result = Operations_(operationOpt, int.Parse(numbers[0]), int.Parse(numbers[1]));

            Console.WriteLine($"Result: {result}");

            Console.WriteLine("Don't wanna do more operations?");

            Console.WriteLine("\nType ANY KEY to stop the calcs and go back to the Main Menu or ENTER to keep the calcs\n");
            stopOpt = Console.ReadKey(true);

        } while (stopOpt.Key == ConsoleKey.Enter);

        MainMenu();
        
    }
    else
    {
        MainMenu();
    }

}

double Operations_(char operationOpt, int n1, int n2)
{

    double result = 0;

    switch (operationOpt)
    {
        case '+':
            result = n1 + n2;
            break;
        case '-':
            result = n1 - n2;
            break;
        case '*':
            result = n1 * n2;
            break;
        case '/':
            result = n1 / n2;
            break;
        case '%':
            result = n1 % n2;
            break; 
        default:
            Console.WriteLine("So sorry, we haven't this operation!");
            CalcOperation();
            break;
    }

    if (hist.ContainsKey(operationOpt)) {
        hist[operationOpt].Add(result);
    }
    else {
        hist.Add(operationOpt, [result]);
    }

    return result;
};

void ShowHist()
{
    Console.Clear();
    Console.WriteLine("Last results");
    foreach (char key in hist.Keys)
    {
        Console.WriteLine($"{key} : [{hist[key]}]");
    }
    Console.WriteLine("\n");

    Console.WriteLine("Type ANY KEY to go back to the Main Menu");
    ConsoleKeyInfo opt = Console.ReadKey(true);

    MainMenu();
    Console.Clear();
    
}