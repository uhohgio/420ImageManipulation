% Reads a grayscale image
image = imread("mickey.png");

% Resizes the image for processing
target_size = [50,50];
img = imresize(image, target_size);

% Reshapes the image into a one dimensional array
image_1 = reshape(img,1,[]);
% Writes this new data to 'input.txt'
dlmwrite('input.txt',image_1,'delimiter',' ');