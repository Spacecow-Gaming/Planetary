import java.util.Scanner;

public class explore{

	sector Sector = new sector();
	Scanner scan = new Scanner(System.in);
	String whereToGo;
	
	public void exploreChoice(){
		
		System.out.println("============================================================================");
		System.out.println("Postion: " + Sector.getPos());
		System.out.println(Sector.getDesc());
		System.out.println("What would you like to do?");
		
		whereToGo = scan.next();
		
		if(whereToGo.equals("move")){
			Sector.sectorX = 2;
			Sector.sectorY = 2;
                        return;
		}else{
			System.exit(0);
		}
	}
	
	
	

}
