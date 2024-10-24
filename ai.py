from groq import Groq

def ai(a):
    b = a + "generate the response in 2 lines maximum"
    client = Groq(api_key="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")
    chatcomp = client.chat.completions.create(
        messages=[
            {"role": "user", "content": b}
        ], 
        model="llama3-8b-8192"
    )
    
    response = chatcomp.choices[0].message.content.split('\n')[:1]
    return '\n'.join(response)
