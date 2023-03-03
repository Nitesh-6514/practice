class armstrong3
{
	public static void main(String args[])
	{
		int n,n1,sum=0;
		n=Integer.parseInt(args[0]);
		n1=n;
		while(n>0)
		{
			int a=n%10;
			n=n/10;
			sum=sum+(a*a*a);
		}
		if (n1==sum)
		{
			System.out.println(n1+" is a armstrong number.");
		}
		else
		{
			System.out.println(n1+" is a not armstrong number.");
		}
	}
}