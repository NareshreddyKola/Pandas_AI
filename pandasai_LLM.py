import pandas as pd
import pandasai as pdai
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

#pdai.set_openai_key('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')
#pdai.api_key.set('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')
#pdai.config.api_key = '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'
df = pd.DataFrame({"Country":["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
                     "GDP": [20890000000000, 2670000000000, 2630000000000, 3850000000000, 1890000000000, 1280000000000, 1640000000000,1320000000000, 5060000000000, 14720000000000],
                     "Happiness Index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
                    })
#llm = OpenAI()
llm = OpenAI(api_token='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')
pandas_ai = PandasAI(llm, verbose=True, conversational=False)

pandas_ai = PandasAI(llm)
response = pandas_ai.run(df, prompt='Which are the 5 happiest countries?')
print(response)


