from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class Mistral7BLocal:
    def __init__(self, model_name_or_path: str = "mistral/mistral-7b-int4"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name_or_path,
            device_map="auto",
            load_in_4bit=True,
            torch_dtype=torch.float16,
            trust_remote_code=True,
        )
        self.model.eval()

    def generate_response(self, prompt: str, max_length: int = 512) -> str:
        # Add instruction tuning and domain-specific prompt enhancements here
        enhanced_prompt = (
            "You are Madhav, a highly intelligent personal assistant. "
            "Answer in Hindi or English as appropriate. "
            "Use domain-specific knowledge and coding expertise. "
            "Follow ethical guidelines strictly. "
            "Here is the user input:\n" + prompt
        )
        inputs = self.tokenizer(enhanced_prompt, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
