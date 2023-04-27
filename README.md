# chatgpt

### To install:

```
pip install git+https://github.com/aaronengland/chatgpt.git
```

Example:

```
import chatgpt.functions as gpt

# key
str_key = 'GET-SECRET-KEY-FROM-https://platform.openai.com/account/api-keys'

# initialize
cls_gpt = gpt.ChatGPT(
    str_key=str_key,
)

# create prompt
str_prompt = 'Using python, how do I group a data frame?'

# send prompt
str_response = cls_gpt.send_prompt(
    str_prompt=str_prompt,
)
print(str_response)
```