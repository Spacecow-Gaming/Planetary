import java.util.Scanner;

public class explore{

	sector Sector = new sector();
	Scanner scan = new Scanner(System.in);
	String whereToGo;
	
	public void exploreChoice(){
		
		System.out.println("============================================================================");
		System.out.println("Postion: " + Sector.getPos());
		System.out.println("Description: " + Sector.getDesc());
		System.out.println();
		System.out.println("What would you like to do?");
		
		whereToGo = scan.next();
		
		if(whereToGo.equals("move")){
			Sector.sectorX += 1;
			Sector.sectorY += 1;
            exploreChoice();
		}else if(whereToGo.equals("bridge")){
			System.out.println("======================================================");
			return;
		}else{
			System.out.println("Sorry, you can either return to the bridge or move");
			exploreChoice();
		}
	}
}
