import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void zad7()
    {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Czy rok jest przestepny");
        System.out.println("Podaj rok");
        int rok =scanner.nextInt();
        if(rok%4==0&&rok%100!=0||rok%400==0)
            System.out.println("Rok jest przestepny");
        else
            System.out.println("Rok nie jest przestepny");

    }
    public static void zad8()
    {
        Scanner scanner =new Scanner(System.in);
        System.out.println("Podaj liczbe");
        int liczba=scanner.nextInt();
        int wynik=0;
        while(liczba!=0){
            wynik+=liczba%10;
            liczba /= 10;
        }
        System.out.println("Suma cyfr podanej liczby wynosi "+wynik);
    }
    public static void zad9()
    {
        Scanner scanner=new Scanner(System.in);
        int[] tablica =new int[10];
        for(int i=0;i<10;i++)
            tablica[i]=i+1;

        for(int i=tablica.length-1;i>=0;i--)
        {
            System.out.println(tablica[i] + " ");
        }


    }
    public static void zad10()
    {
        Scanner scanner =new Scanner(System.in);
        System.out.println("Podaj napis");
        String napis=scanner.next();
        for(int i=0;i<napis.length();i+=2)
        {
            System.out.println(napis.charAt(i));
        }

    }
    public static void zad12()
    {
        Scanner scanner =new Scanner(System.in);
        System.out.println("Palindrom");
        int liczba=scanner.nextInt();
        int wynik=0;
        while(liczba!=0)
        {
            wynik=wynik*10 +liczba%10;
            liczba/=10;

        }
        System.out.println(wynik);
    }
    public static void main(String[] args) {

        zad12();


    }
}