API_KEY = "<YOUR_OPENAI_API_KEY>"
openai_llm_name = "gpt-4-turbo"
prompt_template = '''
Annual Report

{uploaded_file}

Given above information, summarize the company's financial performance, operational segments and concerns in the company for the year. 
Divide the response in three sections. 
For Financial Performance focus on key metrics such as Revenue Growth Rate, Profit Margin, Net Income, Operating Margin, and Earnings per Share (EPS) on Year on Year level.
For Operational Segments, provide an overview of the company's operational segments or business units and their revenue mix.
For Concerns in the company, provide summary related to regulatory issue, market competition, supply chain constraints, any external geo political issues.
'''
