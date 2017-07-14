using System;
namespace Collatz
{
    class euler
    {
        int collatz(int n)
        {
            int terms = 0;
            while (n != 1)
            {
                if (n % 2 == 0)
                    n /= 2;
                else n = 3 * n + 1;
                terms++;
            }
            return terms;


        }
        public static void main()
        {
            int max = 0;
            int largestTerm;
            for (int i = 1; i < 1000000; i++)
            {
                Console.WriteLine(i);
                if (collatz(i) > max)
                {
                    max = collatz(i);
                    largestTerm = i;
                }
            }
            Console.WriteLine("The seed value with the largest sequence is " + largestTerm);

             

        }



    }




}
