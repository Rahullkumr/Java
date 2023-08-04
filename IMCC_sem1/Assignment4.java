    
// Assignment on Inner Classes

class Assignment4{
    int a = 10;
    int b = 20;

    void outerMethod()
    {
        System.out.println("outer method");
    }

    class innerclass{
        int a = 100;
        int b = 200;
        
        void innerMethod(int a, int b)
        {
            System.out.println(Assignment4.this.a + Assignment4.this.b);
        }
    }


    public static void main(String []args){

        // Accessing outer class members through inner class object
        new Assignment4().new innerclass().innerMethod(5,10);

    }
}