import java.util.*;

public class mainMenu{

	Scanner scan = new Scanner(System.in);
	int mainMenuChoice;
	
	void menu(){
		System.out.println("Welcome, do you want to:");
		System.out.println("1) Start a new game?");
		System.out.println("2) Load a saved game?");
		System.out.println("3) Exit");
		
		mainMenuChoice = scan.nextInt();
		
		if(mainMenuChoice == 1){
			System.out.println("There is no game yet...");
			menu();
		}else if(mainMenuChoice == 2){
			System.out.println("You have no saved games...");
			menu();
		}else if(mainMenuChoice == 3){
			System.out.println("Good Bye");
			System.exit(0);
		}else{
			System.out.println("Please pick one of the numbers from the list above.");
			menu();
		}
	}
}