// Program to implement named and 
// nameless object creation


class Assignment5{
	void display(){
		System.out.println("Accessed using named Object");
	}
	void print(){
		System.out.println("Accessed using nameless Object");
	}	
	public static void main(String args[]){
		
		// Below 2 statements are named object creation and calling
		Assignment5 obj = new Assignment5();
		obj.display(); 

		// Below statement is nameless object creation and calling
		new Assignment5().print();
	}
}