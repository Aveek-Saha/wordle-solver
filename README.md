# Wordle Solver
A solver for the official wordle game.

# Rules
- The bot plays Wordle in hard mode, i.e. any information from a guess has to be used in the subsequent guesses.
- The bot uses the list of all valid words + the list of answers from the official wordle website, a total of about 13k words.
- The list of possible answers is not given any special treatment and is mixed with the list of valid words.

# Stats

The bot was tested on all 2309 wordles and these are the results.

## Regular
A regular test run means the result was considered a failure if the bot could not solve the puzzle in 6 or fewer tries. The average score excludes the failed puzzles.

<!-- | Score | # of games |
|:-----:|:----------:|
|   1   |      1     |
|   2   |     91     |
|   3   |     553    |
|   4   |     904    |
|   5   |     527    |
|   6   |     163    |
|   X   |     70     | -->

<table>
    <thead>
        <tr>
            <th>Score</th>
            <th># of games</th>
            <th>Graph</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>1</td>
            <td rowspan=4><img src="https://github.com/Aveek-Saha/wordle-solver/blob/master/graphs/analysis.png" width="100%"></img></td>
        </tr>
        <tr>
            <td>2</td>
            <td>91</td>
        </tr>
        <tr>
            <td >3</td>
            <td>553</td>
        </tr>
        <tr>
            <td>4</td>
            <td>904</td>
        </tr>
        <tr>
            <td>5</td>
            <td>527</td>
        </tr>
        <tr>
            <td>6</td>
            <td>163</td>
        </tr>
        <tr>
            <td>X</td>
            <td>70</td>
        </tr>
    </tbody>
</table>


## Extended
Just to see how the bot performed, it was allowed to continue playing beyond 6 tries till it found a solution. Overall the solver never takes more than 9 attempts to solve a wordle.

<img  align="left" src="https://github.com/Aveek-Saha/wordle-solver/blob/master/graphs/analysis_unlimited.png" width="50%"></img>

| Score | # of games |
|:-----:|:----------:|
|   1   |      1     |
|   2   |     91     |
|   3   |     553    |
|   4   |     904    |
|   5   |     527    |
|   6   |     163    |
|   7   |     55     |
|   8   |     16     |
|   9   |      3     |

