
// Assignment on Instance and Static Variables

class Assignment2{

    // declare 2 instance variables
    int x = 100;
    int y = 200;

    // declare 2 static variables
    static int statvar1 = 1;
    static int statvar2 = 2;

    void method1()
	{
        Assignment2 obj1 = new Assignment2();

        // print 4 variables

        System.out.println(obj1.x);// printing instance variable
        System.out.println(obj1.y);// printing instance variable
        System.out.println(Assignment2.statvar1);// printing static variable
        System.out.println(Assignment2.statvar2);// printing static variable
	}

    static void method2()
    {
        Assignment2 obj2 = new Assignment2();

        // print 4 variables

        System.out.println(obj2.x);// printing instance variable
        System.out.println(obj2.y);// printing instance variable
        System.out.println(Assignment2.statvar1);// printing static variable
        System.out.println(Assignment2.statvar2);// printing static variable		
	}

    public static void main(String []args){
        Assignment2 obj = new Assignment2();

        // call method1()
        obj.method1();// calling instance method

        // call method2()
        Assignment2.method2();// calling static method
    }
}