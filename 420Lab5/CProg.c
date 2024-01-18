#include <stdio.h>
#include <stdlib.h>

// the main function overexposes an image to only black and white pixels
int main(int argc, char *argv[]) {
	// initialization
	int* arrayptr = NULL;
	int thresh = 170;
	// dynamically allocated memory
	arrayptr = (int*)malloc((argc-1)*sizeof(int));

	for(int i=1;i<argc;i++){
		// Read elements from command line and convert to integers
		 arrayptr[i-1] = atoi(argv[i]);
		 arrayptr[i]++;
		// if the element in the array is less than a certain threshold, it rounds down to 0
		if(arrayptr[i-1] < thresh){
			arrayptr[i-1] = 0;
		} else {
		// if the element in the array is greater than the threshold, it rounds up to 255
			arrayptr[i-1] = 255;
		}
		// print the number with a space (for interpretation)
		printf("%d ",arrayptr[i-1]);
		
	}

	// Free dynamically allocated memory
	free(arrayptr);
	return 0;
}