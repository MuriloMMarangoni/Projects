import java.util.ArrayList; // modern arrays
import java.util.Collections; // ?
import java.util.Scanner; // inputs
import java.time.LocalDate; // Horário ou data
import java.time.format.DateTimeFormatter; // formatação do tempo
public class Java{ // main class,this class need to have the name of the file
    public static void main() { // main method, always executed
        // public; visible everywhere
        // static; doesn't need to be instantiated
        // void; doesn't return a value
// --Data types--------------------------------------
        String s;            // Declare string
        s = "";              // Assign a value
        String ss = "";      // Initialize a string
        double d  = 1.1;     // Double
        float f   = 1.123f;  // Float
        int in    = 1;       // Int
        char c    = 'a';     // char
        boolean b = true;    // bool
        int arr[] = {1,2,3}; // array
        arr[0] = 0;          // access
// --Operations-------------------------------------
        in = in + 1; // increment
        in++; // increment
        in--; // decrement
        double exponentiation = Math.pow(10, 2); // same as 10 to the 2 power
        String ternary = in > 0 ? "if true":"if false"; // ternary operator
        int conditions; // temp var0
        int first = 0; // temp var1
        int second = 0; // temp var2
        conditions = first > second ? 1 : 2; // greater 
        conditions = first < second ? 1 : 2; // less
        conditions = first == second ? 1 : 2; // equal
        conditions = first != second ? 1 : 2; // different
        conditions = first > second && first == second ? 1 : 2; // and
        conditions = first > second || first == second ? 1 : 2; // or
        conditions = ! (first > second) ? 1 : 2; // not
// --Functions---------------------------------------
        System.out.println("teste");                          // print + next line
        System.out.print("teste2");                           // print
        System.out.print("\n");                               // next line
        System.out.printf("%s%f%f%d%c%b",ss,d,f,in,c,b); // values printed
// --Structures--------------------------------------
        if (in == 0){                             // if, else if, else 
            System.out.println("its zero");
        }
        else if (in < 0){
            System.out.println("its negative");
        }
        else {
            System.out.println("its positive");
        }
        while(in != 0){                          // while loop
            System.out.printf("%d\n",in);
            in--;
        }
        for (int i = 0;i<10;i++) {               // for loop
            System.out.println(i);
        }
// --Imports-----------------------------------------
        //Scanner
        Scanner teclado = new Scanner(System.in); // object that takes input
        in = teclado.nextInt();                   // int input
        f = teclado.nextFloat();                  // float input
        s = teclado.next();                       // string input
        teclado.close();                          // scanner stops taking memory
        //ArrayList
        ArrayList<String> list = new ArrayList<String>();
        list.add("name"); // adiciona algo a lista
        list.add("name2");
        int size = list.size(); // pega o tamanho da lista
        String item = list.get(0); // pega um index
        System.out.println(list);// mostra a lista
        //Collections
        Collections.reverse(list);// inverte lista original
        //LocalDate
        LocalDate hoje = LocalDate.now(); // data atual
        DateTimeFormatter formatador = DateTimeFormatter.ofPattern("dd/MM/yyyy");//dia mes ano
        System.out.println(hoje.format(formatador)); // tempo formatado
// --OOP------------------------------------------------
        Pacote instancia = new Pacote(); // instancia um objeto sem parâmetros
        Pacote instanciaP = new Pacote(19,"M"); // chama o construtor da classe com parâmetros
        System.out.printf("instanciaP: %d,%s",instanciaP.valor,instanciaP.nome);
        instancia.atributo1 = 1; // acessa um atributo da instância manualmente
        instancia.mostrar(); // usa método do pacote
        System.out.println(instancia.at1x2(instancia.atributo1)); // usa método com return
        System.out.println(Pacote.existe); // atributo estático
        Pacote.mostrarNome(); // método estático
        
    }
}