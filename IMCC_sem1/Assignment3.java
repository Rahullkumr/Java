
// Assignment on Constructors

class Assignment3{
    //Default Constructor
    Assignment3(){
        this(100);//constructor calling another constructor
        System.out.println("Default Constructor");
    }
    
    //Parameterised Constructor
    Assignment3(int x){
        System.out.println("Parameterised Constructor called from default constructor");        
    }

    public static void main(String []args){
        Assignment3 obj = new Assignment3();//default constructor called
    }
}