
// Assignment on Instance Variables


class Assignment1{

    // declare 2 instance variables
    int x = 10;
    int y = 50;

    static void method1(){
        Assignment1 obj1 = new Assignment1();

        // print two variables
        System.out.println(obj1.x);
        System.out.println(obj1.y);
    }
    static void method2(){
        Assignment1 obj2 = new Assignment1();

        // print two variables
        System.out.println(obj2.x);
        System.out.println(obj2.y);
    }
    public static void main(String []args){
        Assignment1 obj = new Assignment1();

        //call method1()
        obj.method1();

        //call method2()       
        obj.method2();
    }
}