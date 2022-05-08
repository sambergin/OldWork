/*
dispatcher.c

Student Name : Sam Bergin
Student ID # : 170670850

Dispatch Algorithm : srt
*/

#include <string.h>
#include <stddef.h>
#include <stdio.h>

#define MAX_LINE_LENGTH 100


#include "llist.h"
#include "queue.h"
#include "process.h"




void dispatcher(FILE *fd, int harddrive){
    /*
        Your code here.
        You may edit the following code
    */
printf("%3d",1);
    char line_buffer[MAX_LINE_LENGTH];
    int start_time, run_time, process_id, num_exchanges, exchange_time;
    char *token;

	QUEUE *new_queue = NULL;

	QUEUE *ready_queue = NULL;
	QUEUE *blocked_queue = NULL;
	QUEUE *exit_queue = NULL;
	QNODE *sel = NULL;
	QNODE *temp = NULL;
	QNODE *temp2 = NULL;
	
	int block = 0;

printf("%3d",1);
    
    //Process simulation input line by line
    while (fgets(line_buffer, MAX_LINE_LENGTH, fd) != NULL && line_buffer[0] != '\n'){
        token = strtok(line_buffer, " ");
        sscanf(token, "%d",&start_time);
       
        token = strtok(NULL, " ");
        sscanf(token, "%d",&process_id);
        
        token = strtok(NULL, " ");
        sscanf(token, "%d",&run_time);
        
        num_exchanges = 0;
        token = strtok(NULL, " ");
        while ( token != NULL ){
            num_exchanges += sscanf(token, "%d",&exchange_time);
            token = strtok(NULL, " ");
printf("%3d",2);
        }
	PROCESS new = new_process(start_time, process_id, run_time, num_exchanges, exchange_time);
printf("%3d",3);
	
	enqueue(new_queue, new);
       printf("Process %3d wants to start at %6dms and run for %6dms and has %3d hard drive exchanges\n",  process_id, start_time, run_time, num_exchanges); 
   
    }
printf("%3d",4);
int time = 0;
while(new_queue->front != NULL) {
	if (new_queue->rear->process.start == time) {
		QNODE p = dequeue(new_queue);
		enqueue(ready_queue, p.process);
		if (p.process.exchanges != 0) {
			ready_queue->rear->process.exchanges = p.process.exchanges;
			

}

		
}
	if (ready_queue->front != NULL) { 
		sel = ready_queue->front;
		temp = ready_queue->front;
		while (temp != NULL) {
			if (temp->process.run < sel->process.run) {
				sel = temp;
			}
			temp = temp->next;
		}
		
	}
	time += 100;
	sel->process.run -= 100;
	
	if (sel->process.run == time) {
		enqueue(blocked_queue, sel->process);
		blocked_queue->rear->process.run = sel->process.run;
		*temp2 = dequeue(ready_queue);
		enqueue(exit_queue, temp2->process);
	}
	else if (sel->process.run > 0) {
		enqueue(ready_queue, sel->process);
		ready_queue->rear->process.run = sel->process.run;
	}
	if (blocked_queue->front != NULL) {
		block += 100;
		if (block == harddrive) {
			*temp = dequeue(blocked_queue);
			block = 0;
			enqueue(ready_queue, temp->process);
			ready_queue->rear->process.run = temp->process.run;
		}
	}
	

}
while (temp->next != NULL) {
temp = exit_queue->front;
if (temp->process.pid == 0) {
	printf("%3d  %6d", temp->process.pid, temp->process.run);
}
else {
	printf("%3d %6d %6d %3d", temp->process.pid, temp->process.run, temp->process.wait, temp->process.blocked); 
}
temp = temp->next;
}

}
