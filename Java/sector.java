import java.util.Random;

public class sector{

	Random random = new Random();
	int sectorX = 1;
	int sectorY = 1;
	int desc;
	

	public String getDesc(){
		
		desc = random.nextInt(10);
		
		if(desc/2 == 0){
			return("There is nothing here");
		}else if(desc == 3){
			return("There are pirates here, be cautious!");
		}else if(desc == 5){
			return("There is a moon here that you can land on!");
		}else if(desc == 7){
			return("There is a planet to explore!");
		}else{
			return("There is nothing here");            
		}	
		
	}
	
	public String getPos(){
		return(sectorX + "," + sectorY);
	}


}