# Wordle Solver

A solver for the [official Wordle game](https://www.nytimes.com/games/wordle/index.html). The daily Wordle solved below by the bot is updated automatically every day at 00:00 UTC.

## Today's Wordle

Wordle 262 4/6

⬛⬛🟨⬛⬛ <br>
⬛🟨⬛🟩⬛ <br>
🟩⬛🟨🟩🟨 <br>
🟩🟩🟩🟩🟩 <br>

<details>
<summary>Solution [Spoilers]</summary>

Answer: `HOARD`
<pre>
FIRST
WHERE
HYDRO
HOARD
</pre>

</details>

# Rules

-   The bot plays Wordle in hard mode, i.e. any information from a guess has to be used in the subsequent guesses.
-   The bot uses the list of all valid words + the list of answers from the official wordle website, a total of about 13k words.
-   The list of possible answers is not given any special treatment and is mixed with the list of valid words.

# Stats

The bot was tested on all 2309 Wordle answer words and these are the results.

## Regular

A regular test run means the result was considered a failure if the bot could not solve the puzzle in 6 or fewer tries. The average score excludes the failed puzzles.

**Average:** 4.051

<table>
    <thead>
        <tr>
            <th>Score</th>
            <th># of games</th>
            <th>Graph</th>
        </tr>
    </thead>
    <tbody style="object-fit: contain">
        <tr>
            <td>1</td>
            <td>1</td>
            <td rowspan=7 align="center"><img src="https://github.com/Aveek-Saha/wordle-solver/blob/master/graphs/analysis.png" width="60%"></img></td>
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

**Average:** 4.148

<table>
    <thead>
        <tr>
            <th>Score</th>
            <th># of games</th>
            <th>Graph</th>
        </tr>
    </thead>
    <tbody style="object-fit: contain">
        <tr>
            <td>1</td>
            <td>1</td>
            <td rowspan=9 align="center"><img src="https://github.com/Aveek-Saha/wordle-solver/blob/master/graphs/analysis_unlimited.png" width="70%"></img></td>
        </tr>
        <tr>
            <td>2</td>
            <td>91</td>
        </tr>
        <tr>
            <td >3</td>
            <td>556</td>
        </tr>
        <tr>
            <td>4</td>
            <td>902</td>
        </tr>
        <tr>
            <td>5</td>
            <td>531</td>
        </tr>
        <tr>
            <td>6</td>
            <td>154</td>
        </tr>
        <tr>
            <td>7</td>
            <td>55</td>
        </tr>
        <tr>
            <td>8</td>
            <td>16</td>
        </tr>
        <tr>
            <td>9</td>
            <td>3</td>
        </tr>
    </tbody>
</table>
