import java.util.Scanner;

public class game{
	
	String moveChoice;
	String helptext = "Official Starship Manual Vol I\n"
                                + "mine - do some mining\n"
                                + "explore - find exciting things\n"
                                + "build - make a space castle\n"
                                + "shop - buy things\n"
                                + "help - look at this text\n";
								
	int tut = 0;
	
	Scanner scan = new Scanner(System.in);
	build build = new build();
	explore explore = new explore();
	shop shop = new shop();
	mine mine = new mine();

	
	
	public void startGame(){
		
		System.out.println("Anti-lock is set to 70%");
		System.out.println("Engines at 56%");
		System.out.println("Core at 34%");
		System.out.println("(rumble rumble)");
		System.out.println("Wow, we are in space!");
		
		System.out.println("============================================");
		
		System.out.println("Captain our engine co-ordinaters are online, we have full control of the ship, what shall we do?");
		
		if(tut == 0){
				System.out.println("You can go to mine, explore, build, shop, or type help.");
				tut = 1;
				choice();
		}else{
			choice();
		}
	}
	
	public void choice(){
		
		System.out.println("You are currently on the bridge");
		System.out.println("What would you like to do Captain?");
		
		moveChoice = scan.next();
		
		if(moveChoice.equals("mine")){
			mine.mine();
		}else if(moveChoice.equals("explore")){
			explore.exploreChoice();
			choice();
		}else if(moveChoice.equals("build")){
			build.build();
		}else if(moveChoice.equals("shop")){
			shop.shop();
		}else if(moveChoice.equals("help")){
			System.out.println(helptext);
            choice();
		}else if(moveChoice.equals("exit")){
			System.exit(0);
		}else{
			System.out.println("Sorry Captain, did you want to mine, explore, build or shop?");
			choice();
		}
	}
}
