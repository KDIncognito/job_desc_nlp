## Extract salary from job descriptions

This is part of a two-part project. After harvesting content from any job-posting website, I used the below program to extract salaries and salary types. This piece of code gives the right results for about 70%-80% of the time, and there is a huge scope for improvement. It is a pain in the neck when it does not give expected results, and I tried to do what I could to include many possibilities to work with. I used a bit of NLP, and some regular expressions along with text manipulation techniques to get the job done.

### Dependencies
We will need the following modules:
1. Numpy
2. Pandas
3. Re
4. Math
5. Spacy

Please see the below example to get a brief summary of what this does.

```
Software engineer needed. Pay ranges between $70k-$80k an annum.

Candidate must know Ruby on Rails, Python/C# may be an added advantage
Work location: Remote
Additional benefits may include a $10,000.00 quarterly bonus
```
In the above example, there are two 'salary' entites. This program uses Spacy to identify all named entities, and the regular expressions isolate salary types like 'yearly', 'annual', 'weekly', 'daily', 'montly, 'hourly' and bonuses. Other text types of interest may also be added using regular expressions as you go on.

From the example, the expected output is ```$75000``` (takes the average annual income) and ```$10000``` (bonus)

Please refer to the ``` salary_extraction.py ``` file for the python code.

Good luck!
