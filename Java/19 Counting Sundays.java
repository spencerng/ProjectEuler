class Date{
	
	static final int SUN=0, MON=1, TUES=2, WED=3, THUR=4, FRI=5, SAT=6;
	static final int JAN = 1, FEB =2, MAR=3, APR=4, MAY = 5,JUN=6,JUL=7,AUG=8,
	SEP=9,OCT=10,NOV=11,DEC=12;
	int dayWeek;
	int day;
	int mon;
	int year;
	
	public Date(int y, int m, int d, int wd){
		year = y;
		mon = m;
		day = d;
		dayWeek = wd;
	}
	
	public void incDay(){
		dayWeek++;
		day++;
		if(dayWeek > SAT){
			dayWeek = SUN;
			
		}
		if((mon==SEP||mon==APR||mon==JUN||mon==NOV)&&day>30){
			incMonth();
			day=1;
		}
		else if(mon==FEB && year%4==0 && !(year%100==0 && year%400!=0) && day>29){
			incMonth();
			day=1;
		}
		else if(mon==FEB && (year%4!=0 || (year%100==0 && year%400==0)  && day > 28)){
			incMonth();
			day=1;
		}
		else if(day > 31){
			incMonth();
			day = 1;
		}
		
	}
	
	public void incMonth(){
		mon++;
		if(mon > DEC){
			mon = JAN;
			year++;
		}
		
	}
	
	public static void main(String[] args){
		int total = 0;
		Date current = new Date(1900, JAN, 1, MON);
		while(current.year!=1901)
			current.incDay();
		while(current.year<=2000){
			
			if(current.day==1 && current.dayWeek==SUN)
				total++;
			current.incDay();
			
			
		}
		System.out.println(total);
		
		
		
	}
	
	
	
	
	
}