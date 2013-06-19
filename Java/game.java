import java.util.Scanner;

public class game{
	
	public String playerName;
	public String shipName;
	public String moveChoice;
	public int tut = 0;
	Scanner scan = new Scanner(System.in);
	build build = new build();
	explore explore = new explore();
	shop shop = new shop();
	mine mine = new mine();

	
	
	public void startGame(){
		
		System.out.println("Aha, Captain, you have arrived. Your starship awaits. Not long until departure, Captain, errr...");
		System.out.println("Sorry, what was your name again? ");
		
		
		playerName = scan.next();
		
		System.out.println("Ahhh, that's right, now I remember, your Captain " + playerName);
		System.out.println("And what was the name of your ship? ");
		
		shipName = scan.next();
		
		System.out.println("I am so excited to travel with you Captain " + playerName + " on board the " + shipName);
		System.out.println("----------------------");
		
		System.out.println("Anti-lock is set to 70%");
		System.out.println("Engines at 56%");
		System.out.println("Core at 34%");
		System.out.println("(rumble rumble)");
		System.out.println("Wow, we are in space!");
		
		System.out.println("Lieutenant Jones: Captain our engine co-ordinaters are online, we have full control of the ship, what shall we do?");
		
		if(tut == 0){
				System.out.println("You can go to mine, explore, build or shop");
				tut = 1;
				choice();
		}else{
			choice();
		}
	}
	
	public void choice(){
		System.out.println("What would you like to do Captain?");
		
		moveChoice = scan.next();
		
		if(moveChoice.equals("mine")){
			mine.mine();
		}else if(moveChoice.equals("explore")){
			explore.explore();
		}else if(moveChoice.equals("build")){
			build.build();
		}else if(moveChoice.equals("shop")){
			shop.shop();
		}else{
			System.out.println("Sorry Captain, did you want to mine, explore, build or shop?");
			choice();
		}
	}
	
	
	

}