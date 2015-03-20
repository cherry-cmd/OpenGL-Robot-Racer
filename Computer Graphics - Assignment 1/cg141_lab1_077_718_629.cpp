/**
 * This program provides the implementaton of the midpoint 
 * method for scan converting the function
 * y = x^2/20 in the range -20 <= x <= 20.
 * @version 9/9/2014
 * @authors Siddhant Tuli, Shalaka Somani, Ronil Pancholia
 */
#include <GL/glut.h>

void init(void) {
	glClearColor(1.0, 1.0, 1.0, 0.0);        // Set display-window color to white.
	glMatrixMode(GL_PROJECTION);	         // Set projection parameters
	glLoadIdentity();
	gluOrtho2D(-50.0, 50.0, -50.0, 50.0);    // World Coordinate Limits
}

void drawAxes() {
/**
 * This function is used to draw X and Y axes
 * on the window
 * @param void This function takes no parameters
 * @return void This funcion does not return anything
 */

	glClear (GL_COLOR_BUFFER_BIT); 			 // Clear display window.
	glColor3f (1.0, 0.0, 0.0); 			     // Set axes color to red.
	
	glBegin(GL_LINES);
		glVertex2i(0, -20);					 // Drawing Y axis
		glVertex2i(0, 60);
	glEnd();

	
	glBegin(GL_LINES);
		glVertex2i(-60, 0);					 // Drawing X axis
		glVertex2i(60, 0);
	glEnd();
	
	glColor3f (0.0, 0.0, 0.0);				 // Set color to black.
    glPointSize(2);							 // Setting Point Size to 2

	GLint i;
	
	for (i=-15; i<60; i=i+5) {
		glBegin(GL_LINES);
			glVertex2i(-1, i);	             // Marking the points on Y axis by	
			glVertex2i(1, i);	             // drawing small line segments  
		glEnd();
	}	

	for (i=-60; i<60; i=i+5) {
		glBegin(GL_LINES);
			glVertex2i(i, -1);				 // Marking the points on X axis by
			glVertex2i(i, 1);				 // drawing small line segments
		glEnd();
	}
}


 void drawPoints(GLint x, GLint y) {
/**
 * This function plots the point passed to it
 * on the window. It uses the symmetry about
 * x = 0 (y-axis) and plots two points at a 
 * time by taking both +x and -x.
 * @param x The value of x-coordinate of the point
 *		     be plotted
 * @param y The value of y-coordinate of the point
 *		     be plotted
 * @return void This function does not return anything
 */	
	glBegin(GL_POINTS);
		glVertex2i(x, y);
		glVertex2i(-x, y);
	glEnd();
}

void parabola() {
/**
 * This fuction implements scan converts the curve
 * y = x^2/a, where a = 20, in the range -20 <= x <= 20.
 * The scan conversion is done in two steps,
 * 1. Along x-axis (Till the slope is < 1) and,
 * 2. Along y-axis (For slope > 1)
 * @param void This function takes no parameters
 * @return void This function does not return anything
 */
	
	glClear (GL_COLOR_BUFFER_BIT);			 // Clear display window.

	drawAxes();								 // Draw X and Y axes

	glColor3f (0.0, 0.0, 1.0);				 // Set parabola points color to Blue

	GLint x1 = 0, y1 = 0, a1 = 20, d1 = -9;	 // d = (2-a)/2
	
	drawPoints(x1, y1);						 // Plotting starting point

	/* SLOPE < 1 : Scan Converting along X-axis */
	while (x1 < a1/2 && y1 < a1/4) {		 // Begin while loop

		if (d1 < 0) {						 // select East Pixel
			d1 += 2*x1 + 3;					 
		}
		else {							 	 // select North East Pixel
			d1 += 2*x1 + 3 - a1;
			y1++;
		}
		x1++;
		drawPoints(x1, y1);					// Plot points calculated by scan conversion
		
	}										// End while loop

	// x = a/2 and y = a/4 : x = 10, y = 5; 
	x1 = a1/2, y1 = a1/4;			
	// d = ((a/2 + 1)^2)/a - (a/4 + 1) : d = -9.75;
	d1 = ((a1/2 + 1)^2)/a1 - (a1/4 + 1);

	/* SLOPE > 1 : Scan Converting along Y-axis */
	while (x1 < 20) {						// range -20 <= x <= 20
											// Begin while loop
		if (d1 < 0) {						// select North East Pixel
			d1 += 2*x1 + 2 - a1;
			x1++;
		}
		else {								// select North Pixel
			d1 += - a1;			
		}
		y1++;
		drawPoints(x1, y1);					// Plot points calculated by scan conversion
	}										// End while loop

	glFlush ();								// Process all OpenGL routines as quickly as possible
}


void main(int argc, char** argv) {
/**
 * This is the main function where the function to
 * draw the required parabola is called.
 * @param argc Number of command line arguments
 * @param argv Array containing the command line arguments
 * @return void This function does not return anything
 */
	glutInit(&argc, argv);					// Initialize GLUT.
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB); // Set Display Mode

	glutInitWindowPosition(50, 100);		// Set Top-Left Display Window Position
	glutInitWindowSize (800, 400);			// Set Display Window Width and Height
	glutCreateWindow ("Parabola y = x^2/20"); // Create Display Window

	init();									// Execute initialization procedure
	drawAxes();								// Draw X and Y axes for reference
	glutDisplayFunc (parabola);				// Send graphics to display window
	glutMainLoop();							// Display everything and wait
}