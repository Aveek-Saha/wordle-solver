# Wordle Solver

A solver for the [official Wordle game](https://www.nytimes.com/games/wordle/index.html) in hard mode. The daily Wordle solved below by the bot is updated automatically every day at 00:00 UTC.

## Today's Wordle

Wordle 263 4/6*

⬛⬛⬛⬛🟨 <br>
⬛⬛⬛🟩🟩 <br>
⬛🟩⬛🟩🟩 <br>
🟩🟩🟩🟩🟩 <br>

<details>
<summary>Solution [Spoilers]</summary>

Answer: `MONTH`
<pre>
FIRST
DEATH
YOUTH
MONTH
</pre>



</details>

# Rules

-   The bot plays Wordle in hard mode, i.e. any information from a guess has to be used in the subsequent guesses.
-   The bot uses the list of all valid words + the list of answers from the official wordle website, a total of about 13k words.
-   The list of possible answers is not given any special treatment and is mixed with the list of valid words.

# Method used

The method used for this bot is inspired from a [video](https://www.youtube.com/watch?v=v68zYyaEmEA) made by [3b1b](https://github.com/3b1b). The approach is similar, use entropy combined with a metric for how common a word is to rank guesses, but the implementation is different from what was shown in the video.

A list of possible answers and valid guesses from the official website is used.

The metric to determine how common a word is comes from [Lexipedia](https://en.lexipedia.org/), which provides word lists extracted from Wikipedia articles. Lexipedia gives us the frequency of the words in these wiki articles, it also lets you filter the length of the words you need, 5 in our case.

The word frequencies are then normalized and we keep only the common words between the valid guess list for Wordle. If a word is present in the valid word list but not in the Lexipedia dataset, we consider it's frequency to be 0.

Then the entropy is calculated for each word and normalized. A final score is calculated weighing the entropy and frequency values. When we sort the list of the first guesses by score, the best first guess turns out to be `FIRST`, kind of poetic.

Then for each possible outcome after the first guess, the score for the best second guess is computed. This saves a lot of time when solving the Wordles. For every guess after that the score is calculated on the fly, this doesn't take too long as the number of possible words is usually small.


# Stats

The bot was tested on all 2309 Wordle answer words and these are the results.

## Regular

A regular test run means the result was considered a failure if the bot could not solve the puzzle in 6 or fewer tries. The average score excludes the failed puzzles.

**Average:** 4.043

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
            <td>X</td>
            <td>74</td>
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
