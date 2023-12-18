// See https://aka.ms/new-console-template for more information
using System.Runtime.InteropServices;

List<double> hist = new List<double>();  

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
    Console.WriteLine("\nType 0 to return to the Main Menu\n");
    Console.WriteLine("Write your operation type below!");
    string opt = Console.ReadLine();
    if (opt != null)
    {
        while (!opt.Equals("0"))
        {
            if (opt.Equals("0"))
            {
                Console.WriteLine("Backing to the Main Menu");
                MainMenu();
            }
            else
            {
                Console.WriteLine("Type the numbers of your operation separated by a space ");
                string[] numbers = Console.ReadLine().Split(" ");

                double result = Operations_(opt, int.Parse(numbers[0]), int.Parse(numbers[1]));

                Console.WriteLine($"Result: {result}");

                Console.WriteLine("Don't wanna do more operations?");

                Console.WriteLine("\nType 0 to return to the Main Menu\n");
            }
        }
    }
    else
    {
        Console.WriteLine("I can't do anything with null values\nSorry!");
    }

}

double Operations_(string opt,int n1, int n2)
{

    double result = 0;

    switch (opt)
    {
        case "+":
            result = n1 + n2;
            break;
        case "-":
            result = n1 - n2;
            break;
        case "*":
            result = n1 * n2;
            break;
        case "/":
            result = n1 / n2;
            break;
        case "%":
            result = n1 % n2;
            break; 
        default:
            Console.WriteLine("So sorry, we haven't this operation!");
            break;
    }

    hist.Add(result);

    return result;
};

void ShowHist()
{
    Console.Clear();
    Console.WriteLine("Last results");
    for (int i = 0; i < hist.Count; i++)
    {
        Console.WriteLine($"{hist[i]}");
    }
    Console.WriteLine("\n");
    MainMenu();
}