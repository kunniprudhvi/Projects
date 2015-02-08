//
//  project_os.c
//
//
//  Created by Shedimbi Prudhvi Rao on 12/5/14.
//
//


#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#define MAX_LINE 80 /* The maximum length command */

int main(void)
{
    char *args[MAX_LINE/2 + 1]; /* command line arguments */
    char temp[50];
    int i=0, j=0, k=0;
    int should_run = 1; /* flag to determine when to exit program */
    char *tok;
    pid_t pid, status;
    int num_cmd;
    char commands1[40][40];
    char commands2[40][40];
    char commands3[40][40];
    FILE * f;
    char max[50];
    char *args2[MAX_LINE/2 + 1];
    char *args3[MAX_LINE/2 + 1];

    while (should_run) {
        i =0;
        p:
	args[1] = NULL;
 	args2[1] = NULL;
 	args3[1] = NULL;
	printf("osh>");
        gets(temp);
	if(strcmp(temp,"")==0)
	{
		goto p;
	}
	else if(strcmp(temp, "history") == 0)
	{
		
		f = fopen("hist.txt", "r");
		int g =0;
		while (fscanf(f, "%s", max) != EOF)
		{

			strcpy(commands1[g],max);	
			g++;	

		}
		fclose(f);
		
		if(g==0)
		{
			printf("Nothing in command history \n");
			goto p;
		}

		for(int d=0; d<10; d++)
		{
			if(g>0)
			{
				printf("%d %s \n", g, commands1[g-1]);
					g--;
			}	

		}
	}
	else if (strcmp(temp, "!!")==0)
	{
		f = fopen("hist.txt", "r");
                int k =0;
                while (fscanf(f, "%s", max) != EOF)
                {

                        strcpy(commands2[k],max);
                        k++;

                }
                fclose(f);
		pid = fork();
		if(pid == 0)
		{

            
			strcpy(args2[0],commands2[k-1]);
			execvp(args2[0], args2);
			exit(1);

                }
                else if (pid > 0)
                {
			goto p;
                }
		
	
        }
        else if(temp[0]=='!' && temp[1] != '!')
        {	
		
		int y = temp[1] - '0';
		int u = temp[2] - '0';
		int q;
		if(u>=1 && u <=9)
		{
			q = y * 10 + u;
		}
		else
		{
			q = y;
		}

		f = fopen("hist.txt", "r");
                int l =0;
                while (fscanf(f, "%s", max) != EOF)
                {
			
                        strcpy(commands3[l],max);
                        l++;

                }
                fclose(f);
		
		if(q>l)
		{
			printf("Command not found. Please enter a valid command. \n");
			goto p;
		
		}

		pid = fork();
		if(pid == 0)
		{

			strcpy(args3[0],commands3[q-1]);
			execvp(args3[0], args3);
			exit(1);

		}
		else if (pid > 0)
		{
			goto p;
		}

	}
	else
	{


            tok = strtok (temp, " ");
            
            while(tok != NULL)
            {
                args[i] = tok;
                tok = strtok(NULL, " ");
                i++;
            }
      
            if(args[i-1][0] == '&')
            {
		args[i-1] = NULL;
                pid = fork();
                if(pid == 0)
                {
                    execvp(args[0], args);
                    exit(1);
                }
                
                else if (pid > 0)
                {
                    goto p;
                    
                }
                
            }
            else
            {
                f = fopen("hist.txt", "a");
		fprintf(f, "%s \n", args[0]);
		fclose(f);
		pid = fork();
                if(pid == 0)
                {
                    
                    execvp(args[0], args);
                    sleep(100);
                    exit(1);
                    
                }
                else if (pid > 0)
                {
                    // parent should keep running
			wait(NULL);
                    
                }

            }
          
            
        }
    }
}


