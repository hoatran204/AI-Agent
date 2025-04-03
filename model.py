from llama_cpp import Llama

from common.config import Config


class LLM:
    def __init__(self, config: Config):
        self.config: Config = config
        # Initialize the Llama model
        self.model = Llama(
            model_path=self.config.MODEL_PATH,
            n_ctx=2048,  # Context window
            n_batch=512,  # Batch size for prompt processing
            verbose=False  # Set to True for detailed logs
        )
        
        # Store model parameters
        self.max_tokens = config.MAX_TOKENS
        self.temperature = config.TEMPERATURE
        self.top_p = config.TOP_P
    
    def generate(
        self,
        prompt: str,
        max_tokens: int = None,
        temperature: float = None,
        top_p: float = None
    ) -> str:
        """Generate a response to the given prompt"""
        # Use provided parameters or fall back to defaults
        max_tokens = max_tokens if max_tokens is not None else self.max_tokens
        temperature = temperature if temperature is not None else self.temperature
        top_p = top_p if top_p is not None else self.top_p
        
        response = self.model(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            echo=False  # Don't include the prompt in the response
        )
        
        # Extract the generated text from the response
        if isinstance(response, dict) and "choices" in response:
            return response["choices"][0]["text"].strip()
        
        # For streaming responses or other return types
        try:
            return response.strip()
        except AttributeError:
            # Handle case where response doesn't have strip method
            return str(response)