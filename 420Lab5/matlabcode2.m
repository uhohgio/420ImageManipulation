string0 = fileread('input.txt');
out0 = uint8(str2num(string0));
output0 = reshape(out0,50,50);

string1 = fileread('c_output.txt');
out1 = uint8(str2num(string1));
output1 = reshape(out1,50,50);

string2 = fileread('hs_output.txt');
out2 = uint8(str2num(string2));
output2 = reshape(out2,50,50);

string3 = fileread('pl_output.txt');
out3 = uint8(str2num(string3));
output3 = reshape(out3,50,50);

subplot(2,2,1), imshow(output0), title('Original Black and White Image');
subplot(2,2,2), imshow(output1), title('Black and White Image from C');
subplot(2,2,3), imshow(output2), title('Black and White Image from Haskell');
subplot(2,2,4), imshow(output3), title('Black and White Image from Prolog');