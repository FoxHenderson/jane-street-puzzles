# Some Ones, Somewhere - June 2025

The answer to this month’s puzzle – which can be seen [here](https://www.janestreet.com/static/pdfs/puzzles/june-2025-puzzle.pdf) – is a sentence.

![image](https://github.com/user-attachments/assets/2d97044a-eef4-43d7-8852-37bd141cf098)

Upon further inspection of the image, we notice that there are scrabble tiles on the sides of some of the boards, spelling "PARTRIDGE TILING" with some small rearrangements. A quick google search tells us:

"Consider a collection of square tiles, the smallest of which is 1 unit by 1 unit in size (and there is one of them) and the largest of which is N units by N units in size (and there are N of them). The total area of all the tiles would be 1x(1×1) + 2x(2×2) + … + Nx(NxN). That sum of cubes turns out to be [(N x (N+1) / 2]^2. This means that the area covered by the tiles is the same as the area of a single large square whose length and width are [N x (N+1)]/2. So wouldn’t it be cool if you could find an arrangement for all those tiles that allows them to fit inside that larger square? That’s the Partridge Puzzle." (read more [here](https://pyrigan.com/2017/02/17/the-partridge-puzzle/))

Writing a quick greedy algorithm, we can solve all the partial tilings we have been given in the inital prompt. Placing them back in the 9x9 grid yields the following

![image](https://github.com/user-attachments/assets/c4415257-d76c-4303-863a-9c0b95bb6a42)

Finally, recalling the problem title 'Some Ones, Somewhere' we turn our attention to the smallest 1x1 squares, in particular their coordinates. 

Considering each squares postion in terms of the contigious 135x135 grid, we gain 9 sets of coordinates. Taking the each number mod 26 maps each one to a letter, yeilding the following:
"SUM OF CUBES IS SQUARE". Noticing the tiles conveniently placed on the tables in image 1 and 7, we get the final answer of 

THE SUM OF CUBES IS A SQUARE
