## Integration of LLMs with Symbolic Regression

- Symbolic Regression is the task of deriving the structure and coefficients of mathematical expressions directly from data – something like what Kepler did with his third law. This task requires relying on human intuition and expertise. 
- It is NP Hard according to research showing that no efficient polytime algorithm exists for this problem.
- Genetic algorithms are best suited to explore the large search space but they lack the “intuition” that a real scientist often has. 
- Previous research and talks by the writer of the PySR library (a widely used SR library written in Julia) outline how LLMs and other Deep Learning techniques could provide these inductive biases. 
- Thus, I wanted to explore how much LLMs could assist in this regard

## What I did 

Built a pipeline to evaluate the hypothesis by executing both proposed methods on the Feynman dataset and the on the hard bonus dataset. 
- Conducted three experiments: 
  - A baseline on PySR only 
  - the LLM seeds the search space with candidates given the dataset metadata and is then called at random 5% of the time.  
  - The LLM is called when stagnation is detected (it still seeds the search) 
- Traded compute time for better guesses by forcing the LLM to perform dimensional analysis and output its reasoning. 
- Added reprompting on syntax errors and insufficient improvement over current pareto-front. 
- Added noise to datasets and distractor variables. 
- Stress tested the pipeline on “bonus” (harder) equations. 

## Visuals
### LLM guidance was better than unguided
<img width="766" height="347" alt="image" src="https://github.com/user-attachments/assets/4676cf42-f395-4cf1-a328-853a114db41e" /> \
<img width="777" height="356" alt="image" src="https://github.com/user-attachments/assets/dafc74d1-6225-4296-b315-54b69a749d03" /> 
### LLM guidance was just as good as unguided
<img width="748" height="348" alt="image" src="https://github.com/user-attachments/assets/65be354e-7774-4c04-9560-3ce462335a3b" /> \
<img width="818" height="357" alt="image" src="https://github.com/user-attachments/assets/3635c74b-57ed-44e1-aed9-56f0aa5e3ef4" /> 
### LLM performance was worse than unguided
<img width="672" height="270" alt="image" src="https://github.com/user-attachments/assets/b3d5fbbc-fc35-4f69-bb75-5a7f81e84e6d" /> \
<img width="792" height="337" alt="image" src="https://github.com/user-attachments/assets/d4e49720-7933-4b80-aa5f-98718601856c" />

## More info
- The LLM outputs JSON of the type: `{‘reasoning’: str , ‘expressions’: list[str]}`
- The reasoning field is discarded and the `ast` module is used to parse the expressions and make sure it is valid Julia syntax. Since we are only dealing with expressions, we can use the ast module but replace the ` ^ ` in Julia with `**` before assessing and then convert back before passing it to the `fit()` function. 
- If the model uses the wrong variables or invents new ones, it is reprompted with the error sent back in the prompt. 
- In one of the runs for example, there was only 1 syntax related reprompt out of 110 LLM calls (0.91%), and the backend never crashed during any test. 

## Future work and limitations 

- It would be interesting to explore how larger models would work with this task – would they provide better skeletons or is there a ceiling to the quality? 
- While I did incorporate dimensionality constraints into the LLM, I did not quantify its benefit/lack thereof by comparing it with the version without it. 
- I could increase training data size or sample randomly from it instead of just taking the first 10,000 examples to make sure it isn’t prone to picking up local patterns. 
- It would be interesting to stress test the models’ reliance on feature names by renaming them to something completely irrelevant (like mass -> bicycle). The quality of outputs would depend on the models’ reasoning capacity and how strictly it can adhere to dimensional analysis.






