module Demo
{
    interface Printer
    {
        void printString(string s);
        void printUpperCase(string s);
        string reverse(string s);
    }

    interface Calculator
    {
        int add(int a, int b);
        int subtract(int a, int b);
    }
}
