from gptrussian import GPTLanguageModel, encode, decode, vocab_size, block_size, device
import torch

# Initialize model
model = GPTLanguageModel().to(device)
model.load_state_dict(torch.load("cursegpt-russian.pth", map_location=device))
model.eval()

# Chat loop
print("CurseGPT  готов! Обложите его хуями и нажмите Enter.")
while True:
    try:
        prompt = input("> ")
        prompt = ''.join([c for c in prompt if c.isalpha()])
        if prompt.strip() == "":
            context = torch.zeros((1, 1), dtype=torch.long, device=device)
        else:
            try: feed = encode(prompt)
            except: feed = encode('\n')
            context = torch.tensor([feed], dtype=torch.long, device=device)
        output = model.generate(context, max_new_tokens=100)
        print(decode(output[0].tolist()).split('\n')[1])
    except KeyboardInterrupt:
        break
