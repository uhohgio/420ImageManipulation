% reverses all the elements in a list
reverse_list([],[]).
reverse_list([X],[X]).
reverse_list([X|Xs],Ys):- 
    reverse_list(Xs,Yys),
    append(Yys,[X],Ys).

% main function takes in an array, reverses it and then outputs a 
% formatted version of the reversed array that can be interpreted
% by the rest of the code to flip the image
main:-
	read(Input),
	reverse_list(Input,Output),
    atomic_list_concat(Output, ' ', OutputString),
    write(OutputString).