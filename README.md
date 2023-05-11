# Wordle Solver

A solver for the [official Wordle game](https://www.nytimes.com/games/wordle/index.html) in hard mode. The daily Wordle solved below by the bot is updated and tweeted on [@SolverWordle](https://twitter.com/SolverWordle) automatically every day at 00:00 UTC.

## Today's Wordle

Wordle 691 4/6*

⬛⬛⬛🟨🟨 <br>
⬛⬛⬛🟨🟩 <br>
🟩🟨⬛⬛🟩 <br>
🟩🟩🟩🟩🟩 <br>

<details>
<summary>Solution [Spoilers]</summary>

<br> 

Answer: `SLIDE`
<pre>
T A R E S
H O U S E
S I N C E
S L I D E
</pre>
</details>

# Rules

-   The bot plays Wordle in hard mode, i.e. any information from a guess has to be used in the subsequent guesses.
-   The bot uses the list of all valid words + the list of answers from the official wordle website, a total of about 13k words.
-   The list of possible answers is not given any special treatment and is mixed with the list of valid words.

# Method used

The method used for this bot is inspired from a [video](https://www.youtube.com/watch?v=v68zYyaEmEA) made by [3b1b](https://github.com/3b1b). The approach is similar, use entropy combined with a metric for how common a word is to rank guesses, but the implementation is different from what was shown in the video. For starters, this bot plays exclusively on hard mode

The metric to determine how common a word is comes from [Lexipedia](https://en.lexipedia.org/), which provides word lists extracted from Wikipedia articles. Lexipedia gives us the frequency of the words in these wiki articles, it also lets you filter the length of the words you need, 5 in our case. An [English word frequency dataset](https://www.kaggle.com/rtatman/english-word-frequency) from Kaggle is also used in combination with the Lexipedia frequency

A list of possible answers and valid guesses from the official website is used. The word frequencies are then normalized and we keep only the common words in the valid guess list for Wordle. If a word is present in the valid word list but not in the combined frequency dataset, we consider it's frequency to be 0.

Then the entropy is calculated for each word and normalized. To compute the total score for a word a weighted sum of the entropy and the frequency metric is taken. When we sort the list of the first guesses by score, the best first guess turns out to be `TARES`.

Then for each possible outcome after the first guess, the score for the best second guess is computed. This saves a lot of time when solving the Wordles. For every guess after that the score is calculated on the fly, this doesn't take too long as the number of possible words is usually small.


# Stats

The bot was tested on all 2309 Wordle answer words and these are the results.

## Regular

A regular test run means the result was considered a failure if the bot could not solve the puzzle in 6 or fewer tries. The average score excludes the failed puzzles.

**Average:** 3.927

**Failure rate:** 2.6%

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
            <td>0</td>
            <td rowspan=7 align="center"><img src="https://github.com/Aveek-Saha/wordle-solver/blob/master/graphs/analysis.png" width="60%"></img></td>
        </tr>
        <tr>
            <td>2</td>
            <td>104</td>
        </tr>
        <tr>
            <td >3</td>
            <td>674</td>
        </tr>
        <tr>
            <td>4</td>
            <td>894</td>
        </tr>
        <tr>
            <td>5</td>
            <td>437</td>
        </tr>
        <tr>
            <td>6</td>
            <td>140</td>
        </tr>
        <tr>
            <td>X</td>
            <td>60</td>
        </tr>
    </tbody>
</table>

## Extended

Just to see how the bot performed, it was allowed to continue playing beyond 6 tries till it found a solution. Overall the solver never takes more than 9 attempts to solve a wordle.

**Average:** 4.013

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
            <td>0</td>
            <td rowspan=9 align="center"><img src="https://github.com/Aveek-Saha/wordle-solver/blob/master/graphs/analysis_unlimited.png" width="70%"></img></td>
        </tr>
        <tr>
            <td>2</td>
            <td>104</td>
        </tr>
        <tr>
            <td >3</td>
            <td>674</td>
        </tr>
        <tr>
            <td>4</td>
            <td>894</td>
        </tr>
        <tr>
            <td>5</td>
            <td>437</td>
        </tr>
        <tr>
            <td>6</td>
            <td>140</td>
        </tr>
        <tr>
            <td>7</td>
            <td>48</td>
        </tr>
        <tr>
            <td>8</td>
            <td>9</td>
        </tr>
        <tr>
            <td>9</td>
            <td>3</td>
        </tr>
    </tbody>
</table>
